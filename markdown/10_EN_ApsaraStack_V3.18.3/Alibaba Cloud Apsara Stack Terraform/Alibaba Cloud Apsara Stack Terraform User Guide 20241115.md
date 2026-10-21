---
title: "Alibaba Cloud Apsara Stack Terraform User Guide 20241115"
product_version: "V3.18.3"
doc_version: "20241115"
pdf_pages: 229
source_pdf: "Alibaba Cloud Apsara Stack Terraform User Guide 20241115.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/3.18.3/Alibaba%20Cloud%20Apsara%20Stack%20Terraform%20User%20Guide%2020241115.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Terraform User Guide 20241115

## Table of Contents

- 1 Apsara Stack Terraform
  - 1.1 Terms
  - 1.2 Benefits
  - 1.3 Scenarios
  - 1.4 Supported services
- 2 Usage
  - 2.1 Initialize a runtime environment
  - 2.2 Initialize a working directory
    - 2.2.1 Use STS to call AlibabacloudStack Provider
  - 2.3 Use Terraform to destroy resources
  - 2.4 Create a VPC
  - 2.5 Create an ECS instance
  - 2.6 Create an SLB instance
  - 2.7 Create an OSS bucket
  - 2.8 Create an ApsaraDB RDS instance
  - 2.9 Create a RAM role
  - 2.10 Create a KMS key
  - 2.11 Create a Message Queue instance
  - 2.12 Create an ACK cluster
  - 2.13 Create Container Registry resources
  - 2.14 Create MaxCompute resources
  - 2.15 Create DataWorks resources
  - 2.16 Create API Gateway resources
  - 2.17 Create Message Queue for Apache Kafka resources
  - 2.18 Create AnalyticDB for MySQL resources
  - 2.19 Create an AnalyticDB for PostgreSQL instance
  - 2.20 Create a PolarDB-X V1.0 instance
  - 2.21 Create an EBS storage set
  - 2.22 Create Auto Scaling resources
  - 2.23 Create CloudMonitor resources
  - 2.24 Register a database instance and a user with DMS Enterprise
  - 2.25 Create a DNS domain name
  - 2.26 Create DTS resources
  - 2.27 Create a DBS backup schedule
  - 2.28 Create DataHub resources
  - 2.29 Create EDAS resources
  - 2.30 Create Express Connect resources
  - 2.31 Create an E-HPC job template
  - 2.32 Create an Elasticsearch cluster
  - 2.33 Create an ApsaraDB for HBase cluster
  - 2.34 Create a Simple Log Service project
  - 2.35 Create an ApsaraDB for MongoDB instance
  - 2.36 Create NAS resources
  - 2.37 Create OOS resources
  - 2.38 Create Quick BI resources
  - 2.39 Create ROS resources
  - 2.40 Create a KVStore for Redis instance
  - 2.41 Create Tablestore resources
  - 2.42 Create VPN Gateway resources
  - 2.43 Create an Apsara Stack disk

m

## 1 Apsara Stack Terraform

Terraform is an open source Infrastructure as Code (IaC) tool that can be used to build, preview, and change infrastructure in a secure and efficient manner. Terraform supports almost all cloud services available on the market. Alibaba Cloud Apsara Stack (hereinafter referred to as Apsara Stack) is an open, unified, and trusted cloud platform tailored for enterprise customers. Apsara Stack is developed based on the same distributed architecture as Alibaba Cloud public cloud. It uses provider templates to manage resources across multiple cloud platforms. Apsara Stack delivers powerful cloud services that can be easily managed. This helps customers improve O&M efficiency and reduce O&M costs.

**Terraform-based orchestration process**

Terraform can be used to orchestrate cloud resources across cloud platforms. After the service-specific code is integrated into the main code, API metadata is obtained from POP in the integration test phase. You can deploy and maintain the metadata of different versions of the service API in the POP metadata center. You can also plug in an automated test suite into the CI/CD pipeline to check for incompatible changes and generate an API change list. This way, the service-specific Terraform provider code can adapt to the changes. The Terraform provider code is open source. This way, you can integrate Terraform changes into your workflows in the integration test phase. The following figure shows the whole process.

**Architecture design**

Apsara Stack Terraform delivers required service capabilities based on the characteristics of public service institutions and enterprises. Cloud services migrated from Alibaba Cloud public cloud to Apsara Stack are first registered with the POP platform. Then, Apsara Uni-manager Management Console periodically pulls API information from POP and registers the information with Apsara Stack API (ASAPI). Apsara Stack Terraform calls ASAPI, ASAPI sends a message to POP, and then POP forwards the message to each cloud service.

### 1.1 Terms

**Background information**

IaC uses code management tools such as Git to manage and track changes to the infrastructure. IaC writes the configuration and deployment process of the infrastructure as code. This helps implement version control on the infrastructure and allows you to perform rollback operations in an efficient manner. You can also use automation tools such as Terraform, Ansible, and Chef to automate the deployment and management of the infrastructure. This helps improve efficiency and reduce human errors. AlibabacloudStack Provider supports 36 cloud services, 201 resource categories, and more than 800 operations.

**Terms**

**Standard terms**

Terraform is an open source IaC tool developed by HashiCorp. Terraform allows developers and O&M teams to define and manage the configurations of infrastructure resources such as virtual machines, storage, and network by using a declarative language. m

**OpenTofu**

On August 10, 2023, Hashicorp converted the Terraform license from Mozilla Public License (MPL) to Business Source License (BUSL) V1.1, which is a non-open source license. Hashicorp does not allow third-party companies to encapsulate Terraform to provide external services. To address this issue, the OpenTofu project was founded. OpenTofu is developed based on the last open source branch of Terraform and hosted under the Linux Foundation. OpenTofu has the following characteristics: Fully compatible with Terraform Support for MPL and continued openness Stable manpower input

**provider**

The Terraform provider is a core concept of Terraform and allows Terraform to interact with and manage different types of infrastructure, such as virtualization platforms and network devices, from various cloud service providers.

**Note**

> **Note:** If no cloud service provider is specified in the following Terraform-related topics, the Terraform provider refers to AlibabacloudStack Provider. AlibabacloudStack Provider is formerly known as ApsaraStack Provider. AlibabacloudStack Provider and ApsaraStack Provider are released to meet community operation requirements and customer compatibility requirements. They provide the same capabilities.

**infrastructure**

This term refers to the infrastructure that supports various cloud computing services. The infrastructure provides users with flexible, scalable, and highly available computing, storage, and network resources and services, such as Elastic Compute Service (ECS) and Pouch for computing, disks, Object Storage Service (OSS), and File Storage NAS (NAS) for storage, and virtual private clouds (VPCs), vSwitches, and VPN gateways for network connectivity.

**Agreed terms**

**working directory**

When you run a Terraform command, the command searches for and loads .tf files in the current directory for automatic orchestration. The command also generates temporary files such as status information, configuration information, and lock text. A directory contains information about an orchestration cluster. The directory is hereinafter referred to as a working directory.

**template file**

m A template file refers to a .tf file that conforms to Terraform HashiCorp Configuration Language (HCL) specifications. In a broad sense, a template file includes the definition of the provider information or the orchestration definition of at least one resource. In the same working directory, Terraform aggregates the content of all .tf files at the same time. Therefore, a working directory can contain multiple .tf files. By default, the provider information is defined in the providers.tf file. Therefore, the template file mentioned in the following Terraform-related topics contains only the definition of resources.

**status file**

After Terraform performs orchestration, a .tfstate status file is generated in the working directory. The status file is compared with the template file during the next automated orchestration to determine whether a change operation is required. If the status file is deleted, resource creation is performed during automated orchestration.

**environment variable**

> **Note:** To reduce the complexity of a document, the code in the following Terraform-related topics contains environment variables that you must configure in advance. You can configure environment variables in the $env:<KEY>=<Value> format in Windows PowerShell or in the export <KEY>=<Value> format in Linux or macOS.

**TF_BIN**

> **Note:** You can configure TF_BIN based on the release version of Terraform that you use.

If you use Terraform, set the value to terraform. If you use OpenTofu, set the value to tofu.

**Architecture**

m

### 1.2 Benefits

**Wide product coverage**

Apsara Stack Terraform V1.0 inherits the management capabilities of 37 cloud services across various categories such as computing, networking, storage, database, big data, container, middleware, application service, and cloud management, 353 functional modules, and 965 APIs.

**Support for multi-platform deployment**

The code for Apsara Stack is managed using a multi-branch technique, where each branch corresponds to a (major) version. This way, you can build multiple versions of an application in one build process and run the application across multiple platforms.

**Applicability to a wide range of sectors**

Apsara Stack Terraform can meet the multi-cloud and hybrid-cloud management requirements of Apsara Stacks customers in sectors such as finance, public service, power, insurance, and communications. m

**Improved test efficiency**

The implementation of Apsara Stack Terraform allows the Apsara Stack testing team to quickly build an automated testing framework to improve testing efficiency.

**Cost savings**

With Apsara Stack Terraform, you can create configuration templates to define and provision resources in a repeatable and predictable manner. You can also deploy the same template multiple times to create identical development, testing, and production environments. This reduces costs.

### 1.3 Scenarios

**Orchestration and management of cloud resources**

You can use Apsara Stack Terraform to manage a variety of cloud resources as code, such as adding, removing, modifying, and querying Elastic Compute Service (ECS), Virtual Private Cloud (VPC), Server Load Balancer (SLB), Object Storage Service (OSS), and ApsaraDB RDS applications.

**Management of multi-cloud environments**

Apsara Stack Terraform allows you to manage resources of different cloud providers at the same time. This simplifies the management and orchestration of large-scale, multi-cloud infrastructure, meets the common multi-cloud and hybrid cloud requirements of more customers, and reduces cloud management costs.

**Self-service**

Testing and O&M teams who often handle repeated cloud resource requests can use Apsara Stack Terraform to build self-service infrastructure modules. These modules can be repeatedly created and used to automatically generate new infrastructure requests.

### 1.4 Supported services

This topic provides the cloud services supported by AlibabacloudStack Provider.

**Supported services**

| Category | Hybrid cloud service | Resource |
|---|---|---|
|   |   | alibabacloudstack instance: _ ECS instance alibabacloudstack security g _ _ roup: security group alibabacloudstack security g _ _ roup rule: security group rule _ alibabacloudstack disk: cloud _ disk alibabacloudstack disk attac _ _ hment: disk attachment to ECS instance alibabacloudstack image: _ image creation |

m

|   |   | alibabacloudstack image ex _ _ port: image export |
|---|---|---|
| Elastic computing | Elastic Compute Service (ECS) | alibabacloudstack image co _ _ py: image copying alibabacloudstack image im _ _ port: image import alibabacloudstack image sh _ _ are permission: image _ sharing alibabacloudstack snapshot: _ snapshot alibabacloudstack snapshot _ _ policy: snapshot policy alibabacloudstack network i _ _ nterface: elastic network interface (ENI) alibabacloudstack network i _ _ nterface attachment: ENI _ bound to ECS instance alibabacloudstack key pair: _ _ SSH key pair alibabacloudstack key pair a _ _ _ ttachment: SSH key pair attachment to ECS instance alibabacloudstack ecs comm _ _ and: Cloud Assistant command alibabacloudstack ecs deplo _ _ yment set: deployment set _ alibabacloudstack ecs hpc cl _ _ _ uster: high performance computing (HPC) cluster alibabacloudstack ecs dedic _ _ ated host: dedicated host _ alibabacloudstack launch te _ _ mplate: launch template alibabacloudstack reserved i _ _ nstance: reserved instance alibabacloudstack ecs ebs st _ _ _ orage sets: storage set _ |

m

|   | Auto Scaling | alibabacloudstack ess alarm _ _ : event-triggered task alibabacloudstack ess attach _ _ ment: ECS instance association with scaling group alibabacloudstack ess lifecyc _ _ le hook: lifecycle hook _ alibabacloudstack ess notific _ _ ation: event notification alibabacloudstack ess scalin _ _ g group: scaling group _ alibabacloudstack ess scalin _ _ g rule: scaling rule _ alibabacloudstack ess scalin _ _ ggroup vserver groups: _ _ Server Load Balancer (SLB) vServer group addition to scaling group alibabacloudstack ess sched _ _ uled task: scheduled task _ alibabacloudstack ess scalin _ _ g configuration: scaling _ configuration |
|---|---|---|
|   | Container Service for Kubernetes (ACK) | alibabacloudstack cs kubern _ _ etes: ACK cluster alibabacloudstack cs kubern _ _ etes node pool: node pool _ _ |
|   | Container Registry | alibabacloudstack cr repo: _ _ Container Registry Enterprise Edition image repository alibabacloudstack cr names _ _ pace: image repository namespace |
|   | Elastic High Performance Computing (E-HPC) | alibabacloudstack ehpc job t _ _ _ emplate: job template |
|   | Resource Orchestration Service (ROS) | alibabacloudstack ros stack: _ _ stack alibabacloudstack ros templ _ _ ate: template |
| > Document Version: 20241115 | 1 |   |

m

|   | CloudOps Orchestration Service (OOS) | alibabacloudstack oos execu _ _ tion: execution alibabacloudstack oos templ _ _ ate: template |
|---|---|---|
| Storage | File Storage NAS (NAS) | alibabacloudstack nas file s _ _ _ ystem: file system alibabacloudstack nas moun _ _ t target: mount target _ alibabacloudstack nas acces _ _ s group: permission group _ alibabacloudstack nas acces _ _ s rule: permission group rule _ |
|   | Object Storage Service (OSS) | alibabacloudstack oss bucke _ _ t: bucket alibabacloudstack oss bucke _ _ t object: object _ alibabacloudstack oss bucke _ _ t kms: OSS server-side _ encryption |
|   | Tablestore | alibabacloudstack ots instan _ _ ce: Tablestore instance alibabacloudstack ots instan _ _ ce attachment: Tablestore _ instance binding to virtual private cloud (VPC) alibabacloudstack ots table: _ _ Tablestore table |

m

|   | VPC | alibabacloudstack vpc: VPC _ alibabacloudstack vpc ipv6 _ _ _ gateway: IPv6 gateway alibabacloudstack vpc ipv6 _ _ _ egress rule: IPv6 egress-only _ rule alibabacloudstack vpc ipv6 i _ _ _ nternet bandwidth: IPv6 _ Internet bandwidth alibabacloudstack route tabl _ _ e: route table alibabacloudstack route tabl _ _ e attachment: route table _ association with vSwitch alibabacloudstack route entr _ _ y: route entry alibabacloudstack router int _ _ erface: router interface alibabacloudstack router int _ _ erface connection: router _ interface connection alibabacloudstack vpn gate _ _ way: VPN gateway alibabacloudstack vpn custo _ _ mer gateway: customer _ gateway alibabacloudstack vpn route _ _ entry: destination-based _ route entry for VPN gateway alibabacloudstack vpn conn _ _ ection: IPsec-VPN connection alibabacloudstack network a _ _ cl: network access control list (ACL) alibabacloudstack network a _ _ cl attachment: network ACL _ association with vSwitch alibabacloudstack network a _ _ cl entries: network ACL rule _ alibabacloudstack nat gatew _ _ ay: NAT gateway alibabacloudstack snat entry _ _ : SNAT entry alibabacloudstack forward e _ _ ntry: DNAT entry |
|---|---|---|
|   | Elastic IP Address (EIP) | alibabacloudstack eip: EIP _ alibabacloudstack eip associ _ _ ation: EIP association |

m

| Networking |   |   |
|---|---|---|
|   | Apsara Stack DNS | alibabacloudstack dns doma _ _ in: domain name alibabacloudstack dns doma _ _ in attachment: domain name _ binding to DNS instance alibabacloudstack dns recor _ _ d: DNS record alibabacloudstack dns group _ _ : DNS group |
|   | Server Load Balancer (SLB) | alibabacloudstack slb: SLB _ instance alibabacloudstack slb acl: _ _ ACL alibabacloudstack slb backe _ _ nd server: SLB backend _ server alibabacloudstack slb ca cer _ _ _ tificate: certificate authority (CA) certificate alibabacloudstack slb domai _ _ n extension: domain _ extension alibabacloudstack slb listene _ _ r: listener alibabacloudstack slb maste _ _ r slave server group: _ _ _ primary/secondary server group alibabacloudstack slb rule: _ _ forwarding rule for HTTP or HTTPS listener alibabacloudstack slb server _ _ certificate: server certificate _ alibabacloudstack slb server _ _ group: server group _ |
|   | EIP Bandwidth Plan | alibabacloudstack common _ _ bandwidth package: EIP _ bandwidth plan alibabacloudstack common _ _ bandwidth package attachm _ _ ent: EIP association with EIP bandwidth plan |
|   | Express Connect | alibabacloudstack express c _ _ onnect physical connection: _ _ physical connection alibabacloudstack express c _ _ onnect virtual border router: _ _ _ virtual border router (VBR) |

m

| Database | AnalyticDB for MySQL | alibabacloudstack adb back _ _ up policy: backup policy _ alibabacloudstack adb accou _ _ nt: database account alibabacloudstack adb conn _ _ ection: public endpoint alibabacloudstack adb db cl _ _ _ uster (alibabacloudstack adb clust _ _ er): AnalyticDB for MySQL cluster |
|---|---|---|
|   | Data Management (DMS) | alibabacloudstack dms enter _ _ prise instance: enterprise _ database instance alibabacloudstack dms enter _ _ prise user: enterprise user _ |
|   | ApsaraDB for HBase | alibabacloudstack hbase inst _ _ ance: ApsaraDB for HBase instance |
|   | ApsaraDB for MongoDB | alibabacloudstack mongodb _ _ instance: replica set instance alibabacloudstack mongodb _ _ sharding instanc: sharded _ cluster instance |
|   | ApsaraDB RDS | alibabacloudstack db instan _ _ ce: ApsaraDB RDS instance alibabacloudstack db accoun _ _ t: database account alibabacloudstack db accoun _ _ t privilege: database account _ privilege alibabacloudstack db backu _ _ p policy: database backup _ policy alibabacloudstack db connec _ _ tion: public endpoint alibabacloudstack db databa _ _ se: ApsaraDB RDS database alibabacloudstack db read w _ _ _ rite splitting connection: _ _ read-only routing endpoint alibabacloudstack db readon _ _ ly instance: read-only _ instance |

m

|   | KVStore for Redis | alibabacloudstack kvstore in _ _ stance: KVStore for Redis instance alibabacloudstack kvstore a _ _ ccount: database account alibabacloudstack kvstore b _ _ ackup policy: backup policy _ alibabacloudstack kvstore c _ _ onnection: public endpoint |
|---|---|---|
|   | AnalyticDB for PostgreSQL | alibabacloudstack gpdb inst _ _ ance: AnalyticDB for PostgreSQL instance alibabacloudstack gpdb con _ _ nection: public endpoint alibabacloudstack gpdb acco _ _ unt: instance initial account |
|   | PolarDB for Xscale (PolarDB-X) 1.0 | alibabacloudstack drds insta _ _ nce: PolarDB-X 1.0 instance |
|   | Data Transmission Service (DTS) | alibabacloudstack dts subscr _ _ iption job: change tracking _ task alibabacloudstack dts synch _ _ ronization instance: data _ synchronization instance alibabacloudstack dts synch _ _ ronization job: data _ synchronization task |
|   | Database Backup (DBS) | alibabacloudstack dbs backu _ _ p plan: backup schedule _ |
|   | MaxCompute | alibabacloudstack maxcomp _ ute project: MaxCompute _ project alibabacloudstack maxcomp _ ute cu: quota group _ alibabacloudstack maxcomp _ ute user: task account _ |
|   | DataHub | alibabacloudstack datahub p _ _ roject: DataHub project alibabacloudstack datahub s _ _ ubscription: subscription alibabacloudstack datahub t _ _ opic: topic |

m

|   | DataWorks | alibabacloudstack data work _ _ s connection: connection _ alibabacloudstack data work _ _ s folder: folder _ alibabacloudstack data work _ _ s project: DataWorks project _ alibabacloudstack data work _ _ s remind: alert rule _ alibabacloudstack data work _ _ s user: DataWorks user _ alibabacloudstack data work _ _ s role binding: user role _ _ |
|---|---|---|
| Big data |   |   |
|   | Quick BI | alibabacloudstack quick bi u _ _ _ ser: organization user alibabacloudstack quick bi u _ _ _ ser group: user group _ alibabacloudstack quick bi _ _ _ workspace: workspace |
|   | Elasticsearch | alibabacloudstack elasticsea _ rch: Elasticsearch instance |

m

| Cloud management | ASCM | alibabacloudstack ascm logo _ _ n policy: access policy _ alibabacloudstack ascm org _ _ anization: organization alibabacloudstack ascm user _ _ : user alibabacloudstack ascm user _ _ role binding: role _ _ assignment to user alibabacloudstack ascm user _ _ group user: user addition to _ user group alibabacloudstack ascm user _ _ group: user group _ alibabacloudstack ascm user _ _ group resource set binding: _ _ _ _ resource set association with user group alibabacloudstack ascm user _ _ group role binding: role _ _ _ assignment to user group alibabacloudstack ascm pas _ _ sword policy: password _ policy for Apsara Uni- manager Management Console alibabacloudstack ascm quo _ _ ta: quota alibabacloudstack ascm reso _ _ urce group: resource set _ alibabacloudstack ascm ram _ _ policy: Resource Access _ Management (RAM) policy alibabacloudstack ascm ram _ _ role: RAM role _ alibabacloudstack ascm ram _ _ policy for role: RAM role _ _ _ policy alibabacloudstack ascm cust _ _ om role: custom role _ |
|---|---|---|
| Monitoring and O&M | CloudMonitor | alibabacloudstack cms alar _ _ m: threshold-triggered alert rule alibabacloudstack cms alar _ _ m contact: alert contact _ alibabacloudstack cms alar _ _ m contact group: alert _ _ contact group alibabacloudstack cms site _ _ _ monitor: site monitoring task |

m

| Middleware | Enterprise Distributed Application Service (EDAS) | alibabacloudstack applicatio _ n deployment: application _ deployment alibabacloudstack edas clust _ _ er: ECS cluster alibabacloudstack edas appli _ _ cation: ECS application alibabacloudstack edas insta _ _ nce cluster attachment: _ _ EDAS Agent installation with ECS Cloud Assistant alibabacloudstack edas k8s _ _ _ cluster: Kubernetes cluster alibabacloudstack edas k8s _ _ _ application: Kubernetes application alibabacloudstack edas appli _ _ cation scale: application _ scale-out alibabacloudstack edas depl _ _ oy group: application group _ |
|---|---|---|
|   | Message Queue (MQ) | alibabacloudstack ons group _ _ : group alibabacloudstack ons instan _ _ ce: MQ instance alibabacloudstack ons topic: _ _ MQ topic |
|   | ApsaraMQ for Kafka | alibabacloudstack alikafka s _ _ asl acl: permissions of _ Simple Authentication and Security Layer (SASL) users and clients to send and receive messages by using SDKs alibabacloudstack alikafka s _ _ asl user: SASL user _ alibabacloudstack alikafka t _ _ opic: message topic |
| Security | Key Management Service (KMS) | alibabacloudstack kms key: _ _ KMS key alibabacloudstack kms alias: _ _ key alias alibabacloudstack kms ciphe _ _ rtext: KMS encryption alibabacloudstack kms secre _ _ t: secret |
| > Document Version: 20241115 | 2 |   |

m

|   | RAM | alibabacloudstack ram role _ _ _ attachment: RAM role assignment to ECS instance |
|---|---|---|
| Application service | API Gateway | alibabacloudstack api gatew _ _ ay api API _ alibabacloudstack api gatew _ _ ay app: application _ alibabacloudstack api gatew _ _ ay group: API group _ alibabacloudstack api gatew _ _ ay app attachment: _ _ attachment of access permissions on multiple APIs to a specific application alibabacloudstack api gatew _ _ ay vpc access: VPC _ _ authorization |
|   | Simple Log Service | alibabacloudstack log projec _ _ t: Simple Log Service project alibabacloudstack log store: _ _ Logstore alibabacloudstack log store i _ _ _ ndex: Logstore index alibabacloudstack log machi _ _ ne group: machine group _ alibabacloudstack logtail att _ _ achment: Logtail configuration attachment to machine group alibabacloudstack logtail con _ _ fig: Logtail configuration |

## 2 Usage

### 2.1 Initialize a runtime environment

**environment**

Terraform is a mainstream CLI tool used in Infrastructure as Code (IaC) scenarios. Before you use Terraform, you must install and configure an executable file on your on-premises machine. Terraform Core

**Download Terraform Core**

AlibabacloudStack Provider supports Terraform and OpenTofu. You can download Terraform or OpenTofu from the official website based on your system and architecture. Official website of Terraform: official installation page

> **Note:** Terraform 1.5.7 is officially used for development and testing. Terraform ensures compatibility across versions. Therefore, you can download the latest version of Terraform.

OpenTofu GitHub: official installation page

> **Note:** OpenTofu is officially guaranteed to be fully compatible with Terraform. Therefore, you can download the latest version of OpenTofu.

**Configure environment variables**

**Windows operating systems**

Right-click the This PC icon and select Properties. On the page that appears, click Advanced system settings. In the System Properties dialog box, click Environment Variables on the Advanced tab to configure environment variables.

**Unix-like operating systems**

> For Linux, macOS, and BSD operating systems, you can refer to this section.

1. Global configurations
Open the terminal. If the Terraform file is stored in a custom directory, run the following commands to link the Terraform binary file to the /usr/bin directory:

```python
cd /usr/bin sudo ln -s /<foo>/<bar>/terraform
```

2. Current user configurations
If the Terraform file is stored in a custom directory, run the vi ~/.bash_profile command to create a configuration file. Run the following commands to write the directory of the Terraform file to the configuration file. Then, save the modification and exit.

```
TERRAFORM = <The directory in which the Terraform binary file is stored> PATH=$TERRAFORM:$PATH:. export PATH
```

Update the configuration file. Open the terminal and run the source ~/.bash_profile command to update the configuration file. Verify environment variables. Open the terminal and run the terraform command. If the following command output is returned, the environment variables are configured.

**AlibabacloudStack Provider**

**Download AlibabacloudStack Provider**

**(Recommended) Use Terraform to automatically download and**

**manage AlibabacloudStack Provider**

> **Note:** During the initialization of the working directory, AlibabacloudStack Provider is automatically downloaded from the official website or the image site without the need for other management operations.

**(Optional and recommended) Configure an Alibaba Cloud image**

**site**

> **Note:** You can configure an Alibaba Cloud image site to effectively resolve slow or failed download issues in the Chinese mainland.

Create a configuration file named `.terraformrc` or `terraform.rc` . The file location varies based on the operating system of your host.
**On a Windows operating system**, the file must be named `terraform.rc` and stored in
the %APPDATA% directory of the related user. The specific directory varies based on the Windows version and system configurations. You can run the $env:APPDATA command in PowerShell to find the file directory in your operating system.
**On all other operating systems**, the file must be named `.terraformrc` and stored in
the home directory of the related user. You can also use the `TF_CLI_CONFIG_FILE` environment variable to specify the directory of the configuration file for the Terraform CLI. The configuration file must follow the `*.tfrc` naming format.

```
provider_installation {
  network_mirror {
    url = "https://mirrors.aliyun.com/terraform/"
    // Only Alibaba Cloud-related providers can be downloaded from image sources in the
Chinese mainland.
    include = [
        "registry.terraform.io/aliyun/alibabacloudstack",
        "registry.terraform.io/hashicorp/alibabacloudstack",
```

`]` `}`

```
  direct {
    // All providers except Alibaba Cloud-related providers maintain the original downl
oad links.
    exclude = [
        "registry.terraform.io/aliyun/alibabacloudstack",
        "registry.terraform.io/hashicorp/alibabacloudstack",
```

`]` `}` `}`

**Manually download and manage AlibabacloudStack Provider**

**Use a default official directory**

Terraform scans and loads AlibabacloudStack Provider from multiple directories in sequence based on the operating system that you use.

| Windows operating systems: | %APPDATA%/terraform.d/plugins |   |
|---|---|---|
| %APPDATA%/HashiCorp/Terraform/plugins |   |   |

|   |   | , |   |
|---|---|---|---|
|   | /Library/Application Support/io.terraform/plugins |   |   |
| , and |   |   |   |

| systems : | $HOME/.terraform.d/plugins |   |
|---|---|---|
| /usr/local/share/terraform/plugins |   |   |
|   |   | , a |

| ~/.local/share/terraform/plugins |   |
|---|---|
| /usr/share/terraform/plugins |   |

To manually download AlibabacloudStack Provider, you must select one of the directories, create a directory structure in the specified format, and then decompress AlibabacloudStack Provider.

**Note**

> **Note:** An invalid directory structure prevents AlibabacloudStack Provider from being loaded.

```
XX(e.g. ./terraform.d/providers/) └── <hostname>(Use registry.terraform.io for Terraform Core and use registry.opentofu.org for OpenTofu.)
    └── <namespace>(e.g. hashicorp or aliyun)
        └── <type>(e.g. alibabacloudstack)
            └── <version>(e.g. 1.0.20)
                └── <your OS>(e.g. darwin_arm64)
                    └── <binary file>(e.g. terraform-provider-alibabacloudstack)
```

**Note**

> **Note:** At the namespace layer, we recommend that you use hashicorp for manual management. If you use aliyun, declare aliyun when you configure the provider information in subsequent steps. Common system architectures include windows_amd64, linux_amd64, linux_arm64, darwin_amd64, and darwin_arm64.

**Use a custom directory**

Select a directory, create a directory structure in the specified format by following the instructions in Use a default official directory, and then decompress AlibabacloudStack Provider. You must specify the directory during the initialization of the working directory.

### 2.2 Initialize a working directory

Terraform loads all .tf files in the same directory when Terraform is running. The directory is called a working directory. In most cases, orchestration content is split and stored in the following four files to facilitate management: provider dependency, provider information, orchestration template, and parameter template.

**(Optional and recommended) Declare the provider dependency**

> **Note:** If no dependency is declared, the latest version of provider is automatically downloaded or loaded from your on-premises machine based on the defined provider.

Create a file named required.tf, modify the file, and then save the file.

```
terraform {
  required_providers {
    alibabacloudstack = {
      source  = "aliyun/alibabacloudstack"
      version = ">= 1.0.27"
```

`}` `}` `}`

**Note**

> **Note:** If the provider is manually managed, the source information must be the same as the namespace and type in the directory structure. If you use the Alibaba Cloud image site, the source information can also be declared as hashicorp/alibabacloudstack.

**Declare the provider information**

Create a file named providers.tf, modify the file, and then save the file.

```
provider "apsarastack" {
   domain    =""
   access_key  =""
   secret_key = ""
   region   =""
   proxy   = ""
   protocol   =""
   insecure   ="true"
   resource_group_set_name =""
```

`}`

> **Note:** The current template contains only the provider parameters that are required by common resources. If you require gateway APIs for Security Token Service (STS) authentication or Object Storage Service (OSS) operations, you need to configure more parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|

| domain | The domain name of Apsara Stack API (ASAPI). | 1. Log on to the Apsara Infrastructure Management Console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column of asapi and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |
|---|---|---|
| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |
| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |

| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
|---|---|---|
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. The value true indicates that insecure HTTPS certificates can be ignored. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |

**Initialize a working directory**

> **Note:** You must configure TF_BIN based on whether you use Terraform or OpenTofu. If you use Terraform, set TF_BIN to terraform. If you use OpenTofu, set TF_BIN to tofu.

Initialize Terraform for the first time.

```
${TF_BIN} init
```

Initialize Terraform by specifying the provider directory.

```
${TF_BIN} init -plugin-dir=<provider directory>
```

Reinitialize Terraform after you modify the provider configurations or version.

```
${TF_BIN} init --upgrade
```

If the following output is returned, the initialization is successful.

**Verify the initialization**

```
${TF_BIN} version
```

Check whether the versions of Terraform and provider are correct.

#### 2.2.1 Use STS to call AlibabacloudStack Provider

**Provider**

This topic describes how to call AlibabacloudStack Provider after the Security Token Service (STS) authentication mode is enabled for an Apsara Stack service.

**STS overview**

STS allows you to manage temporary credentials for your Apsara Stack resources. Resource Access Management (RAM) provides RAM users and roles. A RAM role does not have permanent identity credentials. You can use a RAM role to access Apsara Stack resources only by using an STS token. When an STS token is issued, you can specify a validity period and access permissions for the STS token.

**Preparations**

1. Obtain the value of the role_arn parameter.
i. Use your account username and password to log on to the Apsara Uni-manager Management Console. ii. Click the cloud logo in the upper-right corner of the homepage and select User Information. iii. Click View Current Role Policy. iv. Obtain the RAM role information. Example: acs:ram::1567042650760225:role/ascm-role- 33-4-5509.
2. Obtain the value of the sts_endpoint parameter.
i. Log on to the Apsara Infrastructure Management Console 1.0. ii. In the top navigation bar, choose **Reports** > System Reports. iii. Click **Registration Vars of Services** in the Report column. iv. Click the filter icon next to Service, enter ram, and then click Apply Filter. v. Right-click the item in the Service Registration column of ram-ramService and select Show More. vi. Obtain the value of sts-openapi.endpoint. Example: sts.inter.env66.shuguang.com.

**Procedure**

1. Create a configuration file named terraform.tf and add the values of the role_arn and
sts_endpoint parameters to the configuration file.
2. Add the following code to the terraform.tf file:

```
provider "alibabacloudstack" {
 assume_role {}
```

`}` Example:

```bash
# Environment configuration
provider "alibabacloudstack" {
  domain="Domain name of ASAPI"
  access_key="Your AccessKey ID"
  secret_key="Your AccessKey secret"
  region="Region"
  proxy= "HTTP://<Proxy endpoint>"
  protocol="HTTP"
  insecure="true"
  resource_group_set_name ="Resource set name"
  sts_endpoint = "sts.inter*******"
  role_arn = "acs:ram::******"
  assume_role {}
```

`}`

### 2.3 Use Terraform to destroy resources

**resources**

This topic describes how to use Terraform to destroy created resources.

**Procedure**

To destroy a specified resource, run the `terraform destroy -target=<Resource name>` command. For example, if you want to destroy a virtual private cloud (VPC) created in Apsara Stack Enterprise V3.14, run the `terraform destroy -target=apsarastack_vpc.vpc` command and enter yes to confirm the operation. If you want to destroy a VPC created in Apsara Stack Enterprise V3.16 or later, run the `terraform destroy -target=alibabacloudstack_vpc.vpc` command and enter yes to confirm the operation. To destroy all created resources, run the `terraform destroy` command and enter yes to confirm the operation.

> **Note:** The name of a resource is the name that you specified when you created the resource.

### 2.4 Create a VPC

This topic describes how to use Apsara Stack Terraform to create a virtual private cloud (VPC).

**Create a template file**

Create a file named main.tf and define the required resources in the file.

```bash
# VPC variables
variable "create" {
  description = "Whether to create vpc. If false, you can specify an existing vpc by se
tting 'vpc_id'."
  type        = bool
  default     = true
```

`}`

```
variable "vpc_id" {
  description = "The vpc id used to launch several vswitches. If set, the 'create' will
be ignored."
  type        = string
  default     = ""
```

`}`

```
variable "vpc_name" {
  description = "The vpc name used to launch a new vpc."
  type        = string
  default     = "TF-VPC"
```

`}`

```
variable "vpc_description" {
  description = "The vpc description used to launch a new vpc."
  type        = string
  default     = "A new VPC created by Terrafrom module terraform-alicloud-vpc"
```

`}`

```
variable "vpc_cidr" {
  description = "The cidr block used to launch a new vpc."
  type        = string
  default     = "192.168.0.0/16"
```

`}`

```
variable "resource_group_id" {
  description = "The Id of resource group which the instance belongs."
```

`p` `g` `p` `g`

```
  type        = string
  default     = ""
```

`}`

```
variable "vpc_name_regex" {
  description = "(Deprecated) It has been deprecated from 1.5.0."
  type        = string
  default     = ""
```

`}`

```
variable "vpc_tags" {
  description = "The tags used to launch a new vpc. Before 1.5.0, it used to retrieve e
xisting VPC."
  type        = map(string)
  default     = {}
```

`}`

```bash
# Create a VPC.
resource "alibabacloudstack_vpc" "vpc" {
  count             = var.vpc_id != "" ?  0 : var.create ?  1 : 0
  vpc_name          = var.vpc_name
  cidr_block        = var.vpc_cidr
  description   = var.vpc_description
  tags = merge(
```

`{`

```
      "Name" = format("%s", var.vpc_name)
```

`},`

```
    var.vpc_tags,
```

`)` `}`

**Parameters**

**alibabacloudstack_vpc**

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| vpc name _ | The name of the VPC. | The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), and hyphens (- _ ). It must start with a letter and cannot start with http:// or https://. |

| cidr block _ | The CIDR block of the VPC. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, choose Products > Virtual Private Cloud. In the left- side navigation pane, click Virtual Private Clouds. On the Virtual Private Clouds page, obtain the CIDR block of the VPC. 2. You can define a new CIDR block for the VPC. |
|---|---|---|

**Execute orchestration**

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

**FAQ**

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.

> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.5 Create an ECS instance

This topic describes how to use Apsara Stack Terraform to create an Elastic Compute Service (ECS) instance.

**Create a template file**

Create a file named main.tf and define the required resources in the file.

```
variable "name" {
  default = "terraform_test"
```

`}`

```
data "alibabacloudstack_zones" "default" {
  available_resource_creation = "VSwitch"
```

`}`

```bash
# Create a VPC.
resource "alibabacloudstack_vpc" "vpc" {
  vpc_name = var.name
  cidr_block = "192.168.0.0/16" # The CIDR block of the VPC.
```

`}`

```bash
# Create a vSwitch.
resource "alibabacloudstack_vswitch" "vsw" {
  vpc_id = alibabacloudstack_vpc.vpc.id
  cidr_block = "192.168.0.0/16" # The CIDR block.
  availability_zone = data.alibabacloudstack_zones.default.zones.0.id # The zone ID.
```

`}`

```bash
# Create a security group.
resource "alibabacloudstack_security_group" "group" {
  name = var.name
  vpc_id = alibabacloudstack_vpc.vpc.id
```

`}`

```bash
# Create an ECS instance.
resource "alibabacloudstack_instance" "instance" {
  image_id = "centos_7_7_x64_20G_alibase_20211028.vhd"
  instance_type = "ecs.mn4.large"
  system_disk_category = "cloud_sperf"
  security_groups = [alibabacloudstack_security_group.group.id]
  instance_name = var.name
  vswitch_id = alibabacloudstack_vswitch.vsw.id
```

`}`

**Parameters**

**alibabacloudstack_vpc**

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| vpc name _ | The name of the VPC. | The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), and hyphens (- _ ). It must start with a letter and cannot start with http:// or https://. |

| cidr block _ | The CIDR block of the VPC. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, choose Products > Virtual Private Cloud. In the left- side navigation pane, click Virtual Private Clouds. On the Virtual Private Clouds page, obtain the CIDR block of the VPC. 2. You can define a new CIDR block for the VPC. |
|---|---|---|

**alibabacloudstack_instance**

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| vswitch id _ | The ID of the vSwitch. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, choose Products > Virtual Private Cloud. 2. In the left-side navigation pane, click VSwitches. Obtain the vSwitch ID from the VSwitches page. |
| availability zone _ | The zone ID of the ECS instance. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, choose Products > Elastic Compute Service. 2. In the left-side navigation pane, choose Instances & Images > Instances. Click Create Instance and obtain the zone ID. |
| image id _ | The image ID. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, choose Products > Elastic Compute Service. 2. In the left-side navigation pane, choose Instances & Images > Images. On the Images page, obtain the image ID. |

| instance type _ | The ECS instance type. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, choose Products > Elastic Compute Service. 2. In the left-side navigation pane, choose Instances & Images > Instances. On the Instances page, click Create Instance. On the Create Instance page, select an instance generation and obtain the instance type. |
|---|---|---|
| system disk category _ _ | The type of the system disk. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, choose Products > Elastic Compute Service. 2. In the left-side navigation pane, choose Instances & Images > Instances. On the Instances page, click Create Instance. On the Create Instance page, obtain the system disk type. |
| security groups _ | The security groups. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, choose Products > Elastic Compute Service. 2. In the left-side navigation pane, choose Network & Security > Security Groups. On the Security Groups page, obtain the security group information. |
| instance name _ | The name of the ECS instance. | The name must be 2 to 110 characters in length and can contain letters, digits, periods (.), underscores ( ), hyphens (- _ ), and colons (:). It must start with a letter. |

**Execute orchestration**

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

**FAQ**

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.
> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.6 Create an SLB instance

This topic describes how to use Apsara Stack Terraform to create a Server Load Balancer (SLB) instance in a virtual private cloud (VPC).

**Create a template file**

Create a file named main.tf and define the required resources in the file.

```
variable "name" {
  default = "terraform_slb"
```

`}`

```
data "alibabacloudstack_zones" "default" {
  available_resource_creation = "VSwitch"
```

`}`

```bash
# Create a VPC.
resource "alibabacloudstack_vpc" "default" {
  vpc_name   = var.name
  cidr_block = "172.16.0.0/12"
```

`}`

```bash
# Create a vSwitch.
resource "alibabacloudstack_vswitch" "default" {
  vpc_id            = alibabacloudstack_vpc.default.id
  cidr_block        = "172.16.0.0/21"
  availability_zone = data.alibabacloudstack_zones.default.zones.0.id
  name              = var.name
```

`}`

```bash
# Create an SLB instance.
resource "alibabacloudstack_slb" "default" {
  name          = var.name
  vswitch_id    = alibabacloudstack_vswitch.default.id
```

`}`

**Parameters**

**alibabacloudstack_vpc**

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| vpc name _ | The name of the VPC. | The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), and hyphens (- _ ). It must start with a letter and cannot start with http:// or https://. |

| cidr block _ | The CIDR block of the VPC. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, choose Products > Virtual Private Cloud. In the left- side navigation pane, click Virtual Private Clouds. On the Virtual Private Clouds page, obtain the CIDR block of the VPC. 2. You can define a new CIDR block for the VPC. |
|---|---|---|

**alibabacloudstack_vpc**

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| vpc name _ | The name of the VPC. | The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), and hyphens (- _ ). It must start with a letter and cannot start with http:// or https://. |
| cidr block _ | The CIDR block of the VPC. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, choose Products > Virtual Private Cloud. In the left- side navigation pane, click Virtual Private Clouds. On the Virtual Private Clouds page, obtain the CIDR block of the VPC. 2. You can define a new CIDR block for the VPC. |

**alibabacloudstack_slb**

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| name | The name of the SLB instance. | The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), and hyphens (- _ ). It must start with a letter and cannot start with http:// or https://. |

| vswitch id _ | The ID of the vSwitch. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, choose Products > Virtual Private Cloud. 2. In the left-side navigation pane, click VSwitches. Obtain the vSwitch ID from the VSwitches page. |
|---|---|---|

**Execute orchestration**

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

**FAQ**

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.

> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.7 Create an OSS bucket

This topic describes how to use Apsara Stack Terraform to create an Object Storage Service (OSS) bucket.

**Create a template file**

Create a file named main.tf and define the required resources in the file.

```bash
# Create an OSS bucket.
resource "alibabacloudstack_oss_bucket" "oss" {
  bucket = "test2"
  acl    = "public-read"
```

`}`

**Parameters**

**alibabacloudstack_oss_bucket**

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|

| bucket | The name of the bucket. | The bucket name must be 3 to 63 characters in length and can contain lowercase letters, digits, and hyphens (-). The bucket name must start and end with a lowercase letter or a digit. |
|---|---|---|
| acl | The access control list (ACL) of the bucket. | Valid values: private, public- read, and public-read-write. |

**Execute orchestration**

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

**FAQ**

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.

> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.8 Create an ApsaraDB RDS instance

**instance**

This topic describes how to use Apsara Stack Terraform to create an ApsaraDB RDS instance.

**Prerequisites**

A virtual private cloud (VPC) and a vSwitch are created.

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" { domain="Domain name of ASAPI" access_key="Your AccessKey ID" secret_key="Your AccessKey secret" region="Region" proxy= "HTTP://<Proxy endpoint>" protocol="HTTP" insecure="true" resource_group_set_name ="Resource set name"
```

`}`

```
variable "name" {
  default = "terraformtestslbconfig"
```

`}`

```
data "alibabacloudstack_zones" "default" {
  available_resource_creation = "VSwitch"
```

`}`

```bash
# Create a VPC.
resource "alibabacloudstack_vpc" "default" {
  vpc_name       = "${var.name}"
  cidr_block = "192.168.0.0/16"
```

`}`

```bash
# Create a vSwitch.
resource "alibabacloudstack_vswitch" "default" {
  vpc_id            = "${alibabacloudstack_vpc.default.id}"
  cidr_block        = "192.168.0.0/16"
  availability_zone = "${data.alibabacloudstack_zones.default.zones.0.id}"
  name              = "${var.name}"
```

`}`

```bash
# Create an ApsaraDB RDS instance.
resource "alibabacloudstack_db_instance" "default" {
  engine               = "MySQL"
  engine_version       = "5.6"
  instance_type        = "rds.mysql.s2.large"
  instance_storage     = "30"
  storage_type         = "local_ssd"
  instance_name        = "test_rds"
  vswitch_id           = "${alibabacloudstack_vswitch.default.id}"
  monitoring_period    = "60"
```

`}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|

| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |
|---|---|---|
| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |

| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |
|---|---|---|
| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |
| engine | The database engine that the instance runs. | Valid values: MySQL, SQLServer, PostgreSQL, and PPAS. |
| engine version _ | The version of the database engine. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, choose Products > ApsaraDB RDS. 2. Click Create Instance, and obtain the database engine version from the Create Instance page. |

| instance type _ | The instance type. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, choose Products > ApsaraDB RDS. 2. Click Create Instance, and obtain the instance type from the Create Instance page. |
|---|---|---|
| instance storage _ | The storage capacity of the instance. | Unit: GB. You can increase the storage capacity in increments of 5 GB. For information about the valid values, see the official Apsara Stack documentation at ApsaraDB for RDS Developer Guide. |
| storage type _ | The storage type of the instance. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, choose Products > ApsaraDB RDS. 2. Click Create Instance, and obtain the storage type from the Create Instance page. |
| instance name _ | The name of the instance. | The name must be 2 to 64 characters in length and can contain letters, digits, underscores ( ), hyphens (-), _ and colons (:). It must start with a letter and cannot start with http:// or https://. |

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.
> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.9 Create a RAM role

This topic describes how to use Apsara Stack Terraform to create a Resource Access Management (RAM) role.

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" { domain="Domain name of ASAPI" access_key="Your AccessKey ID" secret_key="Your AccessKey secret" region="Region" proxy= "HTTP://<Proxy endpoint>" protocol="HTTP" insecure="true" resource_group_set_name ="Resource set name"
```

`}`

```bash
# Create a RAM role.
resource "alibabacloudstack_ascm_ram_role" "default" {
  role_name = "TestingRamRole"
  description = "TestingRam"
  organization_visibility = "organizationVisibility.global"
```

`}`

```
output "ramrole" {
  value = alibabacloudstack_ascm_ram_role.default.*
```

`}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |

| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
|---|---|---|
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |
| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |
| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |

| role name _ | The name of the RAM role. | The name can be up to 64 characters in length. |
|---|---|---|
| description | The description of the RAM role. | Note that the description cannot contain spaces. |
| organization visibility _ | The organization visibility. | Valid values: organizationVisibility.organizati on, organizationVisibility.orgAndSu bOrgs, and organizationVisibility.global. |

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

### 2.10 Create a KMS key

This topic describes how to use Apsara Stack Terraform to create a Key Management Service (KMS) key. KMS keys can help protect data in transit.

**Create a template file**

Create a file named main.tf and define the required resources in the file.

```bash
# Create a KMS key.
resource "alibabacloudstack_kms_key" "key" {
  description             = "Hello KMS"
  pending_window_in_days  = "7"
  key_state               = "Enabled"
```

`}`

**Parameters**

**alibabacloudstack_kms_key**

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| pending window in days _ _ _ | The number of days to wait before the key is deleted after resources are destroyed. | Valid values: 7 to 30. Default value: 30. |
| key state _ | The status of the customer master key (CMK). | By default, the CMK is enabled. |

**Execute orchestration**

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

**FAQ**

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.
> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.11 Create a Message Queue instance

**instance**

This topic describes how to use Apsara Stack Terraform to create a Message Queue instance.

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" { domain="Domain name of ASAPI" access_key="Your AccessKey ID" secret_key="Your AccessKey secret" region="Region" proxy= "HTTP://<Proxy endpoint>" protocol="HTTP" insecure="true" resource_group_set_name ="Resource set name"
```

`}`

```bash
# Create a Message Queue instance.
resource "alibabacloudstack_ons_instance" "default" {
  tps_receive_max = 500
  tps_send_max = 500
  topic_capacity = 50
  cluster = "cluster1"
  independent_naming = "true"
  name = "Ons_Apsara_instance"
  remark = "Ons Instance"
```

`}`

```
output "inst" {
  value = alibabacloudstack_ons_instance.default.*
```

`}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |

| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
|---|---|---|
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |
| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |
| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |

| tps receive max _ _ | The maximum transactions per second (TPS) for subscribing to messages from a topic within a specific period of time. | Valid values: 500 to 3000. |
|---|---|---|
| tps send max _ _ | The maximum TPS for sending messages to a topic within a specific period of time. | Valid values: 500 to 3000. |
| topic capacity _ | The maximum number of topics. | Valid values: 10 to 5000. |
| cluster | The name of the cluster. | Specify a name for the cluster. |
| independent naming _ | Specifies whether the instance has a namespace. | Valid values: true and false. true: The instance has a separate namespace. Resource names must be unique within an instance but can be the same across different instances. false: The instance has no separate namespace. Resource names must be globally unique within and across all instances. |
| name | The name of the instance. | The name must be unique within the same account in the same region. The name must be 3 to 64 characters in length and can contain letters, digits, hyphens (-), and underscores ( ). _ |
| remark | The description of the instance. | Specify a concise description for the instance. It must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), hyphens (-), _ and colons (:). It must start with a letter and cannot start with http:// or https://. |

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

> **Important:** If the "The RAM user is not granted permissions on the resource or the API does not support the RAM user" message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.
> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call the Apsara Stack Terraform provider.

### 2.12 Create an ACK cluster

This topic describes how to use Apsara Stack Terraform to create a Container Service for Kubernetes (ACK) cluster.

**Prerequisites**

A virtual private cloud (VPC) and a vSwitch are created.

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" { domain="Domain name of ASAPI" access_key="Your AccessKey ID" secret_key="Your AccessKey secret" region="Region" proxy= "HTTP://<Proxy endpoint>" protocol="HTTP" insecure="true" resource_group_set_name ="Resource set name"
```

`}`

```bash
# Create an ACK cluster.
variable "name1" {
  default = "terraformtestslbconfig"
```

`}`

```
data "alibabacloudstack_zones" "default" {
  available_resource_creation = "VSwitch"
```

`}`

```
variable "name2" {
 default = "tf-testAccCsK8sConfigBasic9124020"
```

`}`

```
data "alibabacloudstack_zones" default {
  available_resource_creation = "VSwitch"
```

`}`

```
variable "k8s_number" {
  description = "The number of kubernetes cluster."
  default     = 1
```

`}`

```bash
# leave it to empty would create a new one
variable "vpc_id" {
  description = "Existing vpc id used to create several vswitches and other resources."
 default     = "vpc-bs1amyht0w3mdkumc2hf0"
```

`}`

```
variable "vpc_cidr" {
  description = "The cidr block used to launch a new vpc when 'vpc_id' is not specified
```

`."`

```
  default     = "172.31.0.0/16"
```

`}`

```bash
# leave it to empty then terraform will create several vswitches
variable "vswitch_ids" {
 description = "List of existing vswitch id."
 type        = list(string)
 default     = ["vsw-bs1xvmkkekuy8i7zlhv3j","vsw-bs1xvmkkekuy8i7zlhv3j","vsw-
bs1xvmkkekuy8i7zlhv3j"]
```

`}`

```
variable "vswitch_cidrs" {
  description = "List of cidr blocks used to create several new vswitches when 'vswitch
_ids' is not specified."
  type        = list(string)
  default     = ["172.31.0.0/16","172.31.0.0/16","172.31.0.0/16"]
```

`}`

```
variable "new_nat_gateway" {
  description = "Whether to create a new nat gateway. In this template, a new nat gatew
ay will create a nat gateway, eip and server snat entries."
  default     = "true"
```

`}`

```bash
# 3 masters is default settings,so choose three appropriate instance types in the avail
ability zones above. variable "master_instance_types" {
  description = "The ecs instance types used to launch master nodes."
  default     = ["ecs.e4.large","ecs.e4.large","ecs.e4.large"]
```

`}`

```
variable "worker_instance_types" {
  description = "The ecs instance types used to launch worker nodes."
  default     = ["ecs.e4.large"]
```

`}`

```bash
# options: between 24-28
variable "node_cidr_mask" {
  description = "The node cidr block to specific how many pods can run on single node."
  default     = 24
```

`}`

```
variable "enable_ssh" {
  description = "Enable login to the node through SSH."
  default     = true
```

`}`

```
variable "password" {
  description = "The password of ECS instance."
  default     = "**********"
```

`}`

```
variable "worker_number" {
  description = "The number of worker nodes in kubernetes cluster."
  default     = 3
```

`}`

```bash
# k8s_pod_cidr is only for flannel network
variable "pod_cidr" {
  description = "The kubernetes pod cidr block. It cannot be equals to vpc's or vswitch
's and cannot be in them."
  default     = "172.20.0.0/16"
```

`}`

```
variable "service_cidr" {
  description = "The kubernetes service cidr block. It cannot be equals to vpc's or vsw
itch's or pod's and cannot be in them."
  default     = "172.21.0.0/20"
```

`}`

```
variable "cluster_addons" {
  description = "Addon components in kubernetes cluster"
  type = list(object({
    name      = string
    config    = string
  }))
  default = [
```

`{`

```
      "name"     = "terway",
      "config"   = "",
```

`},` `{`

```
      "name"     = "csi-plugin",
      "config"   = "",
```

`},` `{`

```
      "name"     = "csi-provisioner",
      "config"   = "",
```

`},` `{`

```
      "name"     = "logtail-ds",
      "config"   = "
{\"IngressDashboardEnabled\":\"true\",\"sls_project_name\":\"alibaba-test\"}",
```

`},` `{`

```
      "name"     = "nginx-ingress-controller",
      "config"   = "{\"IngressSlbNetworkType\":\"internet\"}",
```

`}` `]` `}`

```
resource "alibabacloudstack_cs_kubernetes" "k8s" {
  pod_cidr = "${var.pod_cidr}"
workerdatadisks{
```

```
  worker_data_disks {
    category = "cloud_efficiency"
    size = "100"
    encrypted = "false"
```

`}`

```
  password = "${var.password}"
  master_count = "3"
  master_instance_types = "${var.master_instance_types}"
  worker_instance_types = "${var.worker_instance_types}"
  platform = "CentOS"
  timeout_mins = "25"
  master_disk_category = "cloud_efficiency"
  slb_internet_enabled = "true"
  new_nat_gateway = "true"
  proxy_mode = "ipvs"
  vpc_id = "${var.vpc_id}"
  version = "1.18.8-aliyun.1"
  node_cidr_mask = "${var.node_cidr_mask}"
  enable_ssh = "${var.enable_ssh}"
  worker_disk_category = "cloud_efficiency"
  master_vswitch_ids = "${var.vswitch_ids}"
  master_disk_size = "45"
  num_of_nodes = "${var.worker_number}"
  worker_disk_size = "30"
  name = "${var.name}"
  delete_protection = "false"
  os_type = "linux"
  service_cidr = "${var.service_cidr}"
```

`}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|

| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |
|---|---|---|
| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |
| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |

| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
|---|---|---|
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |
| vpc name _ | The name of the VPC. | The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). The name must start with a letter. |
| cidr block _ | The CIDR block of the VPC. | 1. In the top navigation bar of the Apsara Uni-manager Operation Console, choose Products > Virtual Private Cloud. In the left-side navigation pane, click Virtual Private Clouds. On the Virtual Private Clouds page, obtain the CIDR block of the VPC. 2. You can define a new CIDR block for the VPC. |
| vswitch id _ | The ID of the vSwitch. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, choose Products > Virtual Private Cloud. 2. In the left-side navigation pane, click VSwitches. Obtain the vSwitch ID from the VSwitches page. |
| name | The name of the ACK cluster. | The name must be 1 to 63 characters in length and can contain digits, letters, and hyphens (-). |

| version | The Kubernetes version. | We recommend that you use the latest Kubernetes version. If you do not specify this parameter, the latest Kubernetes version is used. |
|---|---|---|
| password | The password that is used to log on to a cluster node over SSH. | You must specify one of the password, key name, and _ kms encrypted password _ _ parameters. |
| enable ssh _ | Specifies whether to enable SSH logon to a node. | Default value: false. |
| proxy mode _ | The proxy mode. | Set the proxy mode for kube- proxy. Valid values: iptables and ipvs. Default value: ipvs. |
| user data _ | The user data. | Windows instances support batch and PowerShell scripts. If your script file is larger than 1 KB in size, we recommend that you upload the script file to an Object Storage Service (OSS) bucket and use the internal endpoint of the bucket to access the script file. |
| is enterprise security group _ _ _ | Specifies whether to automatically create an advanced security group. | You must set security group id _ _ or is enterprise security group. _ _ _ |
| pod cidr _ | The CIDR block of pods. | You must set this parameter to a valid private CIDR block. Make sure that the specified CIDR block does not overlap with the VPC CIDR block or the CIDR block used by an existing Kubernetes cluster in the VPC. |
| new nat gateway _ _ | Specifies whether to create a Network Address Translation (NAT) gateway when the Kubernetes cluster is created. | This parameter is optional. Default value: true. Not all Apsara Stack APIs are accessible over the internal network. Therefore, we recommend that you set this parameter to true. |

|   |   | password, key name, and _ |
|---|---|---|
| n to a cluster node over | kms encrypted password _ _ |   |

| service cidr _ | The service CIDR block. | This parameter is optional. Make sure that the specified CIDR block does not overlap with the VPC CIDR block or the CIDR block used by an existing Kubernetes cluster in the VPC. You cannot modify the CIDR block after the cluster is created. |
|---|---|---|
| node cidr mask _ _ | The prefix length of the node CIDR block. | This parameter determines the maximum number of pods that can run on a node. Valid values: 24 to 28. If you set this parameter to 24, each node can run a maximum of 255 pods. This number is calculated by using the following formula: Maximum number of pods on each node = 2 ^ (32 - 24) - 1. Default value: 24. |
| slb internet enabled _ _ | Specifies whether to create an Internet-facing Server Load Balancer (SLB) instance for the API server of the cluster. | Default value: true. |

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.
> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.13 Create Container Registry resources

**resources**

This topic describes how to use Apsara Stack Terraform to create a Container Registry Enterprise Edition image repository and an image repository namespace.

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" { domain="Domain name of ASAPI" access_key="Your AccessKey ID" secret_key="Your AccessKey secret" region="Region" proxy= "HTTP://<Proxy endpoint>" protocol="HTTP" insecure="true" resource_group_set_name ="Resource set name"
```

`}`

```bash
# Create an image repository namespace.
resource "alibabacloudstack_cr_namespace" "default" {
  name = "tf-testacc-cr-ns-9415539"
  auto_create = "false"
  default_visibility = "PUBLIC"
```

`}`

```bash
# Create a Container Registry Enterprise Edition image repository.
variable "name" {
 default = "tf-testacc-cr-repo-5702781"
```

`}`

```
resource "alibabacloudstack_cr_namespace" "default" {
 name = "${var.name}"
 auto_create = false
 default_visibility = "PRIVATE"
```

`}`

```
resource "alibabacloudstack_cr_repo" "default" {
  summary = "summary"
  repo_type = "PUBLIC"
  namespace = "${alibabacloudstack_cr_namespace.default.name}"
  name = "${var.name}"
```

`}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|

| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |
|---|---|---|
| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |
| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |

| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
|---|---|---|
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |
| name | The name of the namespace. | The name must be 2 to 30 characters in length and can contain lowercase letters, digits, hyphens (-), and underscores ( ). It cannot start _ or end with a hyphen (-) or an underscore ( ). It cannot _ contain consecutive hyphens (-) or underscores ( ). _ |
| summary | The summary. | The summary must be 1 to 100 characters in length. |
| repo type _ | The type of the repository. | Valid values: PUBLIC and PRIVATE. |
| namespace | The namespace to which the repository belongs. | The namespace must be 2 to 30 characters in length and can contain lowercase letters, digits, hyphens (-), and underscores ( ). It cannot start _ with a hyphen (-) or an underscore ( ). _ |

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.
> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.14 Create MaxCompute resources

**resources**

This topic describes how to use Apsara Stack Terraform to create a task account, a quota group, and a project of MaxCompute.

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" { domain="Domain name of ASAPI" access_key="Your AccessKey ID" secret_key="Your AccessKey secret" region="Region" proxy= "HTTP://<Proxy endpoint>" protocol="HTTP" insecure="true" resource_group_set_name ="Resource set name"
```

`}`

```bash
# Create a quota group.
resource "alibabacloudstack_maxcompute_cu" "default"{
  cu_name      = "tf_cu_wy"
  cu_num       = "1"
  cluster_name = "HYBRIDODPSCLUSTER-A-20210520-07B0"
```

`}`

```bash
# Create a task account.
resource "alibabacloudstack_maxcompute_user" "default"{
  user_name             = "tf_user_wy"
  description           = "TestAccApsaraStackMaxcomputeUser"
  lifecycle {
    ignore_changes = [
      organization_id,
```

`]` `}` `}`

```bash
# Create a MaxCompute project.
resource "alibabacloudstack_maxcompute_project" "default"{
  cluster        = "HYBRIDODPSCLUSTER-A-20210520-07B0"
  external_table = "false"
  quota_id       = "44"
  disk           = 10
  name           = "tf_project_wy"
  aliyun_account = "${alibabacloudstack_maxcompute_user.default.user_name}"
  pk = "1371730998580255"
```

`}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |
| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |

| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |
|---|---|---|
| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |
| cu name _ | The name of the quota group. | The name must be 3 to 32 characters in length and can contain letters, digits, and underscores ( ). It must start _ with a letter. |
| cu num _ | The number of quota groups. | Set this parameter to a value greater than 0. |
| cluster name _ | The name of the cluster. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, choose Products > MaxCompute. 2. In the left-side navigation pane, click Projects. On the Project management page, click Create Project. Then, obtain the cluster name. |

| user name _ | The name of the task account. | The name can contain only letters, digits, hyphens (-), periods (.), and underscores ( ). _ |
|---|---|---|
| description | The description of the task account. | The description must be 2 to 255 characters in length, and can contain letters, digits, underscores ( ), hyphens (-), _ periods (.), colons (:), and commas (,). It must start with a letter and cannot start with http:// or https://. |
| disk | The storage capacity. | Unit: GB. |
| aliyun account _ | The name of the Alibaba Cloud account. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, choose Products > MaxCompute. 3. In the left-side navigation pane, click Task Accounts. On the page that appears, obtain the account name. |
| pk | The alias of the Apsara Stack tenant account. | 1. Log on to the Apsara Uni- manager Management Console. Click the cloud logo in the upper-right corner of the homepage and select User Information. 2. On the Basic Information section, obtain the alias of the Apsara Stack tenant account. |

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.
> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.15 Create DataWorks resources

This topic describes how to use Apsara Stack Terraform to create a connection, a folder, an alert rule, a user, and a user role of DataWorks.

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" { domain="Domain name of ASAPI" access_key="Your AccessKey ID" secret_key="Your AccessKey secret" region="Region" proxy= "HTTP://<Proxy endpoint>" protocol="HTTP" insecure="true" resource_group_set_name ="Resource set name"
```

`}`

```bash
# Create a DataWorks connection.
resource "alibabacloudstack_data_works_connection" "default" {
  project_id = "10060"
  connection_type = "rds"
  content = {
              username = "test"
              database = "test_new"
              tag = "rds"
              password = "*****"
              instanceName = "rm-6cq93i8k9q0045i5t"
              rdsOwnerId = "1371730998580255"
```

`}`

```
  env_type = "1"
  sub_type = "mysql"
  name = "tf-testacccn-hohhot-ste3-d01dataworksconnection97435"
  description = "descriptiontf-testacccn-hohhot-ste3-d01dataworksconnection97435"
```

`}`

```bash
# Create a DataWorks folder.
resource "alibabacloudstack_data_works_folder" "example" {
  project_id  = "320687"
  folder_path = "Business Flow/tfTestAcc/folderDi/tftest1"
```

`}`

```bash
# Create a DataWorks alert rule.
resource "alibabacloudstack_data_works_remind" "default" {
  remind_type = "FINISHED"
  remind_unit = "PROJECT"
  project_id = "10060"
  alert_methods = "SMS"
  alert_unit = "OWNER"
  remind_name = "tf-testacccn-hohhot-ste3-d01dataworksremind87138"
```

`}`

```bash
# Create a DataWorks user.
resource "alibabacloudstack_data_works_user" "default" {
  user_id = "5225501456060119238"
  project_id = "10060"
```

`}`

```bash
# Create a DataWorks user role.
resource "alibabacloudstackdataworksuserrolebinding" "default" {
```

`_` `_` `_` `_` `_`

```
  project_id = "10060"
  user_id = "5225501456060119238"
  role_code = "role_project_guest"
```

`}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |
| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |

| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |
|---|---|---|
| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |
| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |

| project id _ | The ID of the workspace. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, choose Products > DataWorks. Select an organization and a region, and click Access as Administrator to go to the DataWorks homepage. 3. Click the Expand icon in the upper-left corner of the page to view all products. 4. Choose All Products > Data Integration. In the left-side navigation pane, choose Data Source > Data Sources. Click Workspace Management in the left-side navigation pane, and obtain the workspace ID from the Configuration page. |
|---|---|---|
| connection type _ | The connection type. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, choose Products > DataWorks. Select an organization and a region, and click Access as Administrator to go to the DataWorks homepage. 3. Click the Expand icon in the upper-left corner of the page to view all products. 4. Choose All Products > Data Integration. On the homepage of the Data Integration console, click Create Data Synchronization Solution. 5. Select the source for data synchronization from the Select Source drop-down list. The source is used as the connection type. |
| content | The details about the data source. | N/A |

| env type _ | The environment to which the data source belongs. | Valid values: 0 and 1. A value of 0 indicates the development environment, and a value of 1 indicates the production environment. |
|---|---|---|
| sub type _ | The subtype of the data source. | This parameter takes effect only if subtypes are available for a parent type. The following combinations are supported: Parent type: rds Sub-type: mysql, sqlserver, or postgresql |
| name | The name of the data source. | Specify a custom value. |
| description | The description of the connection. | Specify a custom value. |
| folder path _ | The path of the folder. | The folder path must be in the following format: Business Flow/{Business flow name}/[folderDi\|folderMaxCom pute\|folderGeneral\|folderJdbc\|fo lderUserDefined]/{Directory name}. The first part of the path must be Business Flow. The second part of the path must be the business flow name specified in the project. The third part of the path must be one of the following keywords: folderDi\|folderMaxCompute\|f olderGeneral\|folderJdbc\|folde rUserDefined. You can specify the last part of the folder path based on your needs. |
| remind type _ | The trigger condition. | Valid values: FINISHED, UNFINISHED, ERROR, CYCLE UNFINISHED, and _ TIMEOUT. |

| remind unit _ | The type of the object to which the custom alert rule is applied. | Valid values: NODE, BASELINE, PROJECT, and BIZPROCESS. A value of NODE indicates a node. A value of BASELINE indicates a baseline. A value of PROJECT indicates a workspace. A value of BIZPROCESS indicates a workflow. |
|---|---|---|
| alert methods _ | The alert notification methods. | Valid values: MAIL, SMS, and PHONE. The value PHONE is available only for DataWorks Professional Edition and more advanced editions. Separate multiple alert notification methods with commas (,). |
| remind name _ | The name of the custom alert rule. | The name can be up to 128 characters in length. |
| user id _ | The user ID. | 1. Log on to the Apsara Uni- manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain the UID. The parameter value is the UID prefixed with 5. |

| role code _ | The code of the role in the DataWorks workspace. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, choose Products > DataWorks. Select an organization and a region, and click Access as Administrator to go to the DataWorks homepage. 3. Click the Expand icon in the upper-left corner of the page to view all products. 4. Choose All Products > Data Integration. In the left-side navigation pane, choose Data Source > Data Sources. Click User Management in the left-side navigation pane. Click Add Member. In the Add Member dialog box, view the batch role settings and obtain the role information. |
|---|---|---|

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.
> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.16 Create API Gateway resources

**resources**

This topic describes how to use Apsara Stack Terraform to create an API and an API group of API Gateway.

**Create a template file**

Create a file named main.tf and define the required resources in the file.

```
variable "name" {
    default = "tf_testAccApiGatewayApi_7875290"
```

`}`

```
  variable "apigateway_group_description_test" {
    default = "tf_testAcc_api group description"
```

`}`

```bash
# Create an API group.
resource "alibabacloudstack_api_gateway_group" "default" {
  name = "${var.name}"
  description = "${var.apigateway_group_description_test}"
```

`}`

```bash
 # Create an API.
resource "alibabacloudstack_api_gateway_api" "default" {
  name = "${alibabacloudstack_api_gateway_group.default.name}"
  group_id = "${alibabacloudstack_api_gateway_group.default.id}"
  description = "tf_testAcc_api description"
  auth_type = "APP"
  request_config {
    protocol = "HTTP"
    method = "GET"
    path = "/test/path/vpc"
    mode = "MAPPING"
```

`}`

**Parameters**

**alibabacloudstack_api_gateway_api**

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| name | The name of the API group. | The group name must be globally unique. It must be 4 to 50 characters in length and can contain letters, digits, and underscores ( ). It must start _ with a letter. |

| group id _ | The ID of the API group. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, choose Products > API Gateway. 3. In the left-side navigation pane, choose Open API > API Groups. On the API Groups page, click the API group that you want to manage and obtain the group ID. |
|---|---|---|
| auth type _ | The authorization type. | Set the value to APP. |
| protocol | The protocol type supported by the API. | Valid values: HTTP, HTTPS, and WEBSOCKET. |
| method | The HTTP method. | Valid values: GET, POST, DELETE, PUT, HEADER, TRACE, PATCH, CONNECT, and OPTIONS. |
| path | The API path. | Specify a custom value. |
| mode | The request mode. | Valid values: MAPPING and PASSTHROUGH. |

**Execute orchestration**

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

**FAQ**

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.
> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.17 Create Message Queue for Apache Kafka resources

**Apache Kafka resources**

This topic describes how to use Apsara Stack Terraform to create a Message Queue for Apache Kafka topic, a Simple Authentication and Security Layer (SASL) user, and an access control list (ACL) that manages the permissions of SASL users and clients to send and subscribe to messages by using SDKs.

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" {
  domain="Domain name of ASAPI"
  access_key="Your AccessKey ID"
  secret_key="Your AccessKey secret"
  region="Region"
  proxy= "HTTP://<Proxy endpoint>"
  protocol="HTTP"
  insecure="true"
  resource_group_set_name ="Resource set name"
```

`}`

```bash
# Create a message topic.
variable "name" {
  default = "tf-testacc-alikafkatopicbasic8891523599366872118"
```

`}`

```
resource "alibabacloudstack_alikafka_topic" "default" {
  topic = "${var.name}"
  local_topic = "false"
  compact_topic = "false"
  partition_num = "12"
  remark = "alibabacloudstack_alikafka_topic_remark"
  instance_id = "cluster-private-paas-default"
```

`}`

```bash
# Create an SASL user.
variable "name" {
  default = "tf-testacc-alikafkasasluserbasic4735385763274477336"
```

`}`

```
resource "alibabacloudstack_alikafka_sasl_user" "default" {
  instance_id = "cluster-private-paas-default"
  username = "${var.name}"
  password = "inputYourCodeHere"
  type = "scram"
```

`}`

```bash
# Create an ACL that manages the permissions of SASL users and clients to send and subs
cribe to messages by using SDKs. variable "name" {
  default = "tf-testacc-alikafkasaslaclbasic6730947607669687899"
```

`}`

```
resource "alibabacloudstack_alikafka_topic" "default" {
  instance_id = "cluster-private-paas-default"
  topic = "${var.name}"
  remark = "topic-remark"
```

`}`

```
resource "alibabacloudstackalikafkasasluser" "default" {
```

`_` `_` `_`

```
  instance_id = "cluster-private-paas-default"
  username = "${var.name}"
  password = "password"
  type     = "scram"
```

`}`

```
resource "alibabacloudstack_alikafka_sasl_acl" "default" {
  acl_resource_pattern_type = "LITERAL"
  acl_operation_type = "Write"
  instance_id = "cluster-private-paas-default"
  username = "${alibabacloudstack_alikafka_sasl_user.default.username}"
  acl_resource_type = "Topic"
  acl_resource_name = "${alibabacloudstack_alikafka_topic.default.topic}"
```

`}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |
| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |

| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |
|---|---|---|
| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |
| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |
| topic | The name of the topic. | Two topics on a single instance cannot have the same name. The name can be up to 64 characters in length. |

| local topic _ | The type of storage used by the topic. | Valid values: false: The topic uses cloud storage. true: The topic uses local storage. |
|---|---|---|
| compact topic _ | The log cleanup policy that is used for the topic. This parameter is available only when local topic is set to true. _ | Valid values: false: The default log cleanup policy is used for the topic. true: The log compaction policy is used for the topic. |
| partition num _ | The number of partitions in the topic. | Valid values: 1 to 48. |
| remark | The description of the topic. | The description must be 3 to 64 characters in length. |
| instance id _ | The instance ID. | cluster-private-paas-default |
| username | The username of the SASL user. | The name must be 1 and 64 characters in length. The name can contain only letters, digits, underscores ( ), and hyphens (- _ ). |
| password | The password of the SASL user. | The password must be 1 to 64 characters in length and can contain letters, digits, and underscores ( ). You must _ specify one of the password and kms encrypted password _ _ parameters. |

| type | The SASL mechanism. | Valid values: plain: a simple mechanism that uses usernames and passwords to verify user identities. Message Queue for Apache Kafka provides an optimized PLAIN mechanism that allows you to dynamically create SASL users for an instance without the need to restart the instance. SCRAM: a mechanism that uses usernames and passwords to verify user identities. This mechanism provides better security protection than the PLAIN mechanism. Message Queue for Apache Kafka uses SCRAM-SHA-256. Default value: plain. |
|---|---|---|
| acl resource pattern type _ _ _ | The match mode. | Valid values: LITERAL: exact match PREFIXED: prefix match |
| acl operation type _ _ | The operation type. | Valid values: Write Read |
| acl resource type _ _ | The resource type. | Valid values: Topic Group |
| acl resource name _ _ | The name of the resource. | The value can be the name of a topic or a consumer group. You can use an asterisk (*) to represent the names of all topics or consumer groups. |

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.
> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.18 Create AnalyticDB for MySQL resources

**resources**

This topic describes how to use Apsara Stack Terraform to create an AnalyticDB for MySQL cluster, a database account, and a public endpoint.

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" {
  domain="Domain name of ASAPI"
  access_key="Your AccessKey ID"
  secret_key="Your AccessKey secret"
  region="Region"
  proxy= "HTTP://<Proxy endpoint>"
  protocol="HTTP"
  insecure="true"
  resource_group_set_name ="Resource set name"
```

`}`

```bash
# Create an AnalyticDB for MySQL cluster.
variable "name" {
  default = "tf-testacccn-wulan-env180-d01adbCluster81463"
```

`}`

```
resource "alibabacloudstack_vpc" "default" {
 name = "${var.name}"
 cidr_block = "172.16.0.0/16"
```

`}`

```
data "alibabacloudstack_zones" "default" {
 available_resource_creation = "ADB"
```

`}`

```
data "alibabacloudstack_vswitches" "default" {
 vpc_id = "${alibabacloudstack_vpc.default.id}"
 zone_id = "${data.alibabacloudstack_zones.default.zones.0.id}"
```

`}`

```
resource "alibabacloudstack_vswitch" "default" {
 name = "tf_testAccAdb_vpc"
 vpc_id = "${alibabacloudstack_vpc.default.id}"
 availability_zone = "${data.alibabacloudstack_zones.default.zones.0.id}"
 cidr_block = "172.16.0.0/24"
```

`}`

```
resource "alibabacloudstack_adb_db_cluster" "default" {
  vswitch_id = "${alibabacloudstack_vswitch.default.id}"
  cpu_type = "intel"
```

`t`

```
"8C 45GB"
```

```
  storage_resource = "8Core45GB"
  storage_type = "SSD"
  db_node_count = "2"
  compute_resource = "8Core40GB"
  description = "${var.name}"
  mode = "flexible"
  cluster_type = "AnalyticdbOnPanguHybrid"
  db_cluster_category = "cluster"
```

`}`

```bash
# Create a public endpoint.
resource "alibabacloudstack_vpc" "default" {
 name = "${var.name}"
 cidr_block = "172.16.0.0/16"
```

`}`

```
data "alibabacloudstack_zones" "default" {
 available_resource_creation = "ADB"
```

`}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |

| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
|---|---|---|
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |
| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |
| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |

| cpu type _ | The CPU type. | Set the value to Intel. |
|---|---|---|
| db node count _ _ | The number of nodes. | Valid values: 2 to 128. |
| compute resource _ | The specifications of computing resources that are used by the cluster in elastic mode. | The increase in resources can speed up queries. AnalyticDB for MySQL automatically scales computing resources on demand. |
| mode | The cluster mode. | Valid values: reserver and flexible. |
| cluster type _ | The cluster type. | Valid values: analyticdb and AnalyticdbOnPanguHybrid. |
| db cluster category _ _ | The cluster category. | Valid values: Basic, Cluster, and MixedStorage. |
| db cluster class _ _ | The cluster specifications. | Valid values: C8 C32 |
| db node storage _ _ | The storage capacity of a node. | Unit: GB. Valid values: Valid values when db cluster class is set to C8: _ _ 100 to 1000 Valid values when db cluster class is set to _ _ C32: 100 to 8000 |
| db cluster version _ _ | The version of the AnalyticDB for MySQL Data Warehouse Edition cluster. | Set the value to 3.0. Default value: 3.0. |
| db cluster id _ _ | The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, choose Products > AnalyticDB for MySQL 3.0. 3. In the left-side navigation pane, click Clusters. Then, obtain the cluster ID. |

| account name _ | The name of the database account. | The name can be up to 16 characters in length and can contain lowercase letters, digits, and underscores ( ). It _ must start with a letter. |
|---|---|---|
| account password _ | The password of the database account. | The password must be 6 to 32 characters in length and can contain letters, digits, and underscores ( ). _ |

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

### 2.19 Create an AnalyticDB for PostgreSQL instance

**PostgreSQL instance**

This topic describes how to use Apsara Stack Terraform to create an AnalyticDB for PostgreSQL instance.

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" {
  domain="Domain name of ASAPI"
  access_key="Your AccessKey ID"
  secret_key="Your AccessKey secret"
  region="Region"
  proxy= "HTTP://<Proxy endpoint>"
  protocol="HTTP"
  insecure="true"
  resource_group_set_name ="Resource set name"
```

`}`

```bash
# Create an instance.
data "alibabacloudstack_zones" "default" {
      available_resource_creation = "Gpdb"
```

`}`

```
resource "alibabacloudstack_gpdb_instance" "default" {
  engine = "gpdb"
  engine_version = "4.3"
  instance_class = "gpdb.group.segsdx2"
  instance_group_count = "2"
  description = "tf-testAccGpdbInstance_new"
  availability_zone = "${data.alibabacloudstack_zones.default.zones.0.id}"
```

`}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |

| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
|---|---|---|
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |
| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |
| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |

| engine | The database engine. | Default value: gpdb. |
|---|---|---|
| engine version _ | The engine version. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, choose Products > AnalyticDB for PostgreSQL. 3. Click Create Instance and obtain the engine version. |
| instance class _ | The instance type. | For more information, seeInstance types. |
| instance group count _ _ | The number of compute nodes in the AnalyticDB for PostgreSQL instance. | Valid values: 2, 4, 8, 16, and 32. |
| description | The description of the instance. | Set this parameter to a string that is 2 to 256 characters in length. |
| availability zone _ | The zone ID of the instance. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, choose Products > AnalyticDB for PostgreSQL. 3. Click Create Instance and obtain the zone ID. |

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

### 2.20 Create a PolarDB-X V1.0 instance

**instance**

This topic describes how to use Apsara Stack Terraform to create a PolarDB-X V1.0 instance.

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" {
  domain="Domain name of ASAPI"
  access_key="Your AccessKey ID"
  secret_key="Your AccessKey secret"
  region="Region"
  proxy= "HTTP://<Proxy endpoint>"
  protocol="HTTP"
  insecure="true"
  resource_group_set_name ="Resource set name"
```

`}`

```bash
# Create an instance.
provider "alibabacloudstack" {
  assume_role {}
```

`}`

```
  variable "name" {
    default = "tf-testacccn-qingdao-env66-d01Drdsdatabase-8541692170859304796"
```

`}`

```
  data "alibabacloudstack_zones" "default" {
    available_resource_creation = "VSwitch"
```

`}`

```
  variable "instance_series" {
    default = "drds.sn2.4c16g"
```

`}`

```
  resource "alibabacloudstack_vpc" "default" {
    name       = "${var.name}"
    cidr_block = "172.16.0.0/16"
```

`}`

```
  resource "alibabacloudstack_vswitch" "default" {
    vpc_id            = "${alibabacloudstack_vpc.default.id}"
    cidr_block        = "172.16.0.0/24"
    availability_zone = "${data.alibabacloudstack_zones.default.zones.0.id}"
    name              = "${var.name}"
```

`}`

```
resource "alibabacloudstack_drds_instance" "default" {
  zone_id = "${alibabacloudstack_vswitch.default.availability_zone}"
  instance_series = "${var.instance_series}"
  instance_charge_type = "drdsPost"
  vswitch_id = "${alibabacloudstack_vswitch.default.id}"
  specification = "drds.sn2.4c16g.8C32G"
  description = "${var.name}"
```

`}` The following table describes the parameters.

| 03 |   | > Document Version: 2024111 |
|---|---|---|

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |
| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |

| region | Region | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |
|---|---|---|
| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |
| zone id _ | The zone ID. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, choose Products > PolarDB-X V1.0. 3. Click Create Instance, and obtain the zone ID from the Create PolarDB-X Instance page. |
| instance series _ | The instance series. | Valid values: drds.sn2.4c16g: Starter Edition drds.sn2.8c32g: Standard Edition drds.sn2.16c64g: Enterprise Edition |

| instance charge type _ _ | The billing method. | Valid values: PrePaid and PostPaid. Default value: PostPaid. |
|---|---|---|
| vswitch id _ | The ID of the vSwitch. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, choose Products > Virtual Private Cloud. 2. In the left-side navigation pane, click VSwitches. Obtain the vSwitch ID from the VSwitches page. |
| specification | The instance type. | The value consists of the instance series and the specific instance specifications. For example, you can set the value to drds.sn2.4c16g.8c32g. |

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

**Important**

> If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.
> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.21 Create an EBS storage set

This topic describes how to use Apsara Stack Terraform to create an Elastic Block Storage (EBS) storage set.

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" {
  domain="Domain name of ASAPI"
  access_key="Your AccessKey ID"
  secret_key="Your AccessKey secret"
  region="Region"
  proxy= "HTTP://<Proxy endpoint>"
  protocol="HTTP"
  insecure="true"
  resource_group_set_name ="Resource set name"
```

`}`

```bash
# Create a storage set.
variable "name" {
 default = "tf-testAcccn-qingdao-env17-d01AlibabacloudStackEcsCommand49708"
```

`}`

```
data "alibabacloudstack_zones" "default" {} resource "alibabacloudstack_ecs_ebs_storage_set" "default" {
  storage_set_name = "tf-testAcccn-qingdao-env17-d01AlibabacloudStackEcsCommand49708"
  maxpartition_number = "2"
  zone_id = "${data.alibabacloudstack_zones.default.zones.0.id}"
```

`}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |

| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
|---|---|---|
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |
| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |
| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |

| storage set name _ _ | The name of the storage set. | The name must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https:// . It can contain letters, digits, colons (:), underscores ( ), and hyphens (- _ ). |
|---|---|---|
| maxpartition number _ | The maximum number of partitions in the storage set. | The value must be greater than or equal to 2. Default value: 2. |
| zone id _ | The zone ID of the storage set. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, choose Products > Elastic Compute Service. In the left-side navigation pane, choose Storage & Snapshots > Disks. 3. Click Create Disk, and obtain the zone ID from the Create Disk page. |

|   | http:// |
|---|---|
| https:// |   |

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.
> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.22 Create Auto Scaling resources

**resources**

This topic describes how to use Apsara Stack Terraform to create a scaling group, a scaling rule, and a scaling configuration of Auto Scaling.

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" {
  domain="Domain name of ASAPI"
  access_key="Your AccessKey ID"
  secret_key="Your AccessKey secret"
  region="Region"
  proxy= "HTTP://<Proxy endpoint>"
  protocol="HTTP"
```

```
  insecure="true"
  resource_group_set_name ="Resource set name"
```

`}`

```
data "alibabacloudstack_zones" "default" {
  available_resource_creation = "VSwitch"
```

`}`

```
data "alibabacloudstack_instance_types" "default" {
  availability_zone = data.alibabacloudstack_zones.default.zones[0].id
  cpu_core_count    = 2
  sorted_by         = "Memory"
```

`}`

```
 locals {
  instance_type_id = sort(data.alibabacloudstack_instance_types.default.ids)[0]
```

`}`

```
data "alibabacloudstack_images" "default" {
  name_regex  = "^ubuntu_18.*64"
  most_recent = true
  owners      = "system"
```

`}`

```bash
# Create a virtual private cloud (VPC).
resource "alibabacloudstack_vpc" "default" {
  vpc_name       = "${var.name}"
  cidr_block = "172.16.0.0/16"
```

`}`

```bash
# Create a vSwitch.
resource "alibabacloudstack_vswitch" "default" {
  vpc_id            = "${alibabacloudstack_vpc.default.id}"
  cidr_block        = "172.16.0.0/24"
  availability_zone = "${data.alibabacloudstack_zones.default.zones.0.id}"
  name              = "${var.name}"
```

`}`

```bash
# Create a security group.
resource "alibabacloudstack_security_group" "default" {
  name   = "${var.name}"
  vpc_id = "${alibabacloudstack_vpc.default.id}"
```

`}`

```bash
# Create a security group rule.
resource "alibabacloudstack_security_group_rule" "default" {
    type = "ingress"
    ip_protocol = "tcp"
    nic_type = "intranet"
    policy = "accept"
    port_range = "22/22"
    priority = 1
    security_group_id = "${alibabacloudstack_security_group.default.id}"
```

```
    cidr_ip = "172.16.0.0/24"
```

`}`

```
  variable "name" {
    default = "tf-testAccEssScalingRule-591939"
```

`}`

```bash
# Create a scaling group.
  resource "alibabacloudstack_ess_scaling_group" "default" {
    min_size = 1
    max_size = 1
    scaling_group_name = "${var.name}"
    vswitch_ids = ["${alibabacloudstack_vswitch.default.id}"]
    removal_policies = ["OldestInstance", "NewestInstance"]
```

`}`

```bash
# Create a scaling configuration.
  resource "alibabacloudstack_ess_scaling_configuration" "default" {
    scaling_group_id = "${alibabacloudstack_ess_scaling_group.default.id}"
    image_id = "${data.alibabacloudstack_images.default.images.0.id}"
    instance_type = "${local.instance_type_id}"
    security_group_id = "${alibabacloudstack_security_group.default.id}"
    force_delete = "true"
```

`}`

```bash
# Create a scaling rule.
  resource "alibabacloudstack_ess_scaling_rule" "default" {
    scaling_group_id = "${alibabacloudstack_ess_scaling_group.default.id}"
    adjustment_type = "TotalCapacity"
    adjustment_value = "1"
    cooldown = 0
```

`}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|

| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |
|---|---|---|
| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |
| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |

| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
|---|---|---|
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |
| min size _ | The minimum number of Elastic Compute Service (ECS) instances in the scaling group. | If the number of ECS instances in the scaling group is less than the value of the MinSize parameter, Auto Scaling automatically creates ECS instances until the number of instances is equal to the value of the MinSize parameter. |
| max size _ | The maximum number of ECS instances in the scaling group. | If the number of ECS instances in the scaling group is greater than the value of the MaxSize parameter, Auto Scaling automatically removes ECS instances from the scaling group until the number of instances is equal to the value of the MaxSize parameter. |
| scaling group name _ _ | The name of the scaling group. | The name of a scaling group must be unique in a region. The name must be 2 to 64 characters in length, and can contain letters, digits, underscores ( ), hyphens (-), _ and periods (.). The name must start with a letter or a digit. The default value is the value of ScalingGroupId. |

| removal policies _ | The instance removal policies. | Valid values: OldestInstance: removes ECS instances that are added to the scaling group at the earliest point in time. NewestInstance: removes ECS instances that are most recently added to the scaling group. OldestScalingConfiguration: removes ECS instances that are created based on the earliest scaling configuration. CustomPolicy: removes ECS instances based on the custom scale-in policy (Function). |
|---|---|---|
| scaling group id _ _ | The ID of the scaling group. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, choose Products > Auto Scaling. 3. In the left-side navigation pane, click Scaling Groups. On the Scaling Groups page, obtain the ID of the scaling group. |
| image id _ | The ID of the image file. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, choose Products > Auto Scaling. 3. In the left-side navigation pane, click Scaling Groups to view the list of scaling groups. 4. Click the ID of the scaling group that you want to manage to go to the scaling group details page. 5. Click the Instance Configuration Sources tab and click Create Scaling Configuration. Then, obtain the image ID. |

| instance type _ | The ECS instance type. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, choose Products > Auto Scaling. 3. In the left-side navigation pane, click Scaling Groups to view the list of scaling groups. 4. Click the ID of the scaling group that you want to manage to go to the scaling group details page. 5. Click the Instance Configuration Sources tab and click Create Scaling Configuration. Then, obtain the ECS instance type. |
|---|---|---|
| security group id _ _ | The ID of the security group to which the ECS instance belongs. | ECS instances in the same security group can access each other. |
| force delete _ | Specifies whether to forcibly delete the last scaling configuration and its scaling group. | Default value: false. |
| adjustment type _ | The method used by the scaling rule to adjust the number of instances. | This parameter is required and applicable only to simple scaling rules. Valid values: QuantityChangeInCapacity: adds or removes the specified number of ECS instances to or from the scaling group. PercentChangeInCapacity: adds or removes the specified percentage of ECS instances to or from the scaling group. TotalCapacity: adjusts the number of ECS instances in the scaling group to a specified number. |

| adjustment value _ | The number of ECS instances to be adjusted by the scaling rule. | This parameter is required and applicable only to simple scaling rules. The number of ECS instances to be adjusted in a single scaling activity cannot exceed 500. Valid values if adjustment type is set to _ QuantityChangeInCapacity: - 500 to 500 Valid values if adjustment type is set to _ PercentChangeInCapacity: - 100 to 10000 Valid values if adjustment type is set to _ TotalCapacity: 0 to 1000 |
|---|---|---|
| cooldown | The amount of time to wait after a scaling activity completes and before the next scaling activity can start. | This parameter is applicable only to simple scaling rules. Valid values: 1 to 86400. Unit: seconds. This parameter is empty by default. If you do not set this parameter, the return value is 0, which is the default value of the Integer data type. |

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.
> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.23 Create CloudMonitor resources

**resources**

This topic describes how to use Apsara Stack Terraform to create a threshold-triggered alert rule, an alert contact, an alert contact group, and a site monitoring task of CloudMonitor.

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" {
  domain="Domain name of ASAPI"
  access_key="Your AccessKey ID"
  secret_key="Your AccessKey secret"
  region="Region"
  proxy= "HTTP://<Proxy endpoint>"
  protocol="HTTP"
```

```
  insecure="true"
  resource_group_set_name ="Resource set name"
```

`}`

```bash
 # Create a threshold-triggered alert rule.
resource "alibabacloudstack_slb" "basic" {
 name          = "terraform_omega_1"
```

`}`

```
resource "alibabacloudstack_cms_alarm" "default" {
  name    = "TfAccCmsAlarm_omega_1"
  project = "acs_slb_dashboard"
  metric  = "ActiveConnection"
  dimensions = {
    instanceId = alibabacloudstack_slb.basic.id
```

`}`

```
  escalations_critical {
    statistics = "Average"
    comparison_operator = "<="
    threshold = 35
    times = 2
```

`}`

```
  enabled =      true
  contact_groups     = ["test-group"]
  effective_interval = "0:00-2:00"
```

`}`

```bash
# Create an alert contact.
variable "name" {
 default = "tf-testAcccn-qingdao-env17-d01CmsAlarmContactzhangsan3465898"
```

`}`

```
resource "alibabacloudstack_cms_alarm_contact" "default" {
  describe = "For-test"
  channels_mail = "h***@aaa.com"
  lifecycle {
    ignore_changes = [
                       "channels_mail"
```

`]` `}`

```
  alarm_contact_name = "${var.name}"
```

`}`

```bash
# Create an alert contact group.
variable "name" {
 default = "tf-testAcccn-qingdao-env17-d01CmsAlarmContactGrouptf-test2591317"
```

`}`

```
resource "alibabacloudstack_cms_alarm_contact" "default" {
  alarm_contact_name = "${var.name}-1"
  describe           = "For Test 1234567"
  channels_mail      = "h***@aaa.com"
  lifecycle {
    ignore_changes = [channels_mail]
```

`}` `}`

```
resource "alibabacloudstack_cms_alarm_contact" "default0" {
  alarm_contact_name = "${var.name}-0"
  describe           = "For Test 1234567"
  channels_mail      = "h***@aaa.com"
  lifecycle {
    ignore_changes = [channels_mail]
```

`}` `}`

```
resource "alibabacloudstack_cms_alarm_contact_group" "default" {
  alarm_contact_group_name = "${var.name}"
```

`}`

```bash
# Create a site monitoring task.
resource "alibabacloudstack_cms_site_monitor" "basic" {
   address = "http://www.alibabacloud.com"
   task_name = "tf-testAccCmsSiteMonitor_basic"
   task_type = "HTTP"
   interval = 5
   isp_cities {
    city = "546"
    isp = "465"
```

`}` `}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |

| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
|---|---|---|
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |
| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |
| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |

| name | The name of the alert rule. | Specify a custom value. |
|---|---|---|
| project | The name of the monitoring project. | Examples: acs ecs dashboard _ _ and acs rds dashboard. _ _ |
| metric | The name of the metric corresponding to the project. | Examples: CPUUtilization and networkin rate. _ |
| dimensions | The resources associated with the alert rule. | Set this parameter to a set of key-value pairs. Examples of keys: instanceId, device, and port. The value of each key must be a string. Separate multiple key-value pairs with commas (,). |
| escalations critical _ | The critical-level alert configurations. | Specify a custom value. |
| enabled | Specifies whether to enable the alert rule. | Default value: true. |
| contact groups _ | The contact groups to which the alert rule is applied. | Set this parameter to the contact groups that have been created in the console. |
| effective interval _ | The interval at which the alert rule takes effect. | Specify this parameter in the hh:mm-hh:mm format, such as 0:00-4:00. Default value: 00:00- 23:59. |
| describe | The description of the alert contact. | Specify a custom value. |
| channels mail _ | The email address of the alert contact. | After an email address is added or modified, the recipient receives an email that contains an activation link. The system adds the recipient to the alert contact list only after the email address is activated. |
| alarm contact name _ _ | The name of the alert contact. | Specify a custom value. |

| alarm contact group name _ _ _ | The name of the alert contact group. | Specify a custom value. |
|---|---|---|
| address | The URL or IP address monitored by the site monitoring task. | Example: https://www.aliyun.com. |
| task name _ | The name of the site monitoring task. | The name must be 4 to 100 characters in length and can contain letters, digits, and underscores ( ). _ |
| task type _ | The protocol that is used by the site monitoring task. | Protocols such as HTTP, PING, TCP, UDP, DNS, SMTP, POP3, and FTP can be used for site monitoring. |
| interval | The monitoring interval of the site monitoring task. | Unit: minutes. Valid values: 1, 5, and 15. Default value: 1. |
| isp cities _ | The detection points in the JSON array format. | Example: [{"city":"546", "isp":"465"}, {"city":"572", "isp":"465"}, {"city":"738", "isp":"465"}]. The three city codes respectively represent Beijing, Hangzhou, and Qingdao. |

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.
> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.24 Register a database instance and a user with DMS Enterprise

**and a user with DMS Enterprise**

This topic describes how to use Apsara Stack Terraform to register a database instance and a user with Data Management (DMS) Enterprise.

**Prerequisites**

An ApsaraDB RDS instance, a database account, and an Apsara Uni-manager Management Console user are created.

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file. `#``E` `i` `t` `fi` `ti`

|   | # Environment configuration provider "alibabacloudstack" { domain="Domain name of ASAPI" access key="Your AccessKey ID" _ secret key="Your AccessKey secret" _ region="Region" proxy= "HTTP://<Proxy endpoint>" protocol="HTTP" insecure="true" resource group set name ="Resource set name" _ _ _ } # Register a database instance for your enterprise. variable "name" { default = "tf-testAccDmsEnterpriseInstance1304" } data "alibabacloudstack account" "current" { _ } resource "alibabacloudstack db instance" "instance" { _ _ engine = "MySQL" engine version = "5.6" _ instance type = "rds.mysql.t1.small" _ instance storage = "10" _ instance name = "${var.name}" _ security ips = ["0.0.0.0/0"] _ storage type = "local ssd" _ _ } resource "alibabacloudstack db account" "account" { _ _ instance id = "${alibabacloudstack db instance.instance.id}" _ _ _ name = "tftest123" password = "inputYourCodeHere" type = "Normal" } resource "alibabacloudstack ascm user" "user" { _ _ cellphone number = "13900000000" _ email = "t***@gmail.com" display name = "C2C-DELTA" _ organization id = 33 _ mobile nation code = "91" _ _ login name = "User Dms ${var.name}" _ _ _ login policy id = 1 _ _ } resource "alibabacloudstack dms enterprise user" "default" { _ _ _ uid = alibabacloudstack ascm user.user.user id _ _ _ user name = alibabacloudstack ascm user.user.login name _ _ _ _ mobile = "15910799999" role names = ["ADMIN"] _ } resource "alibabacloudstack dms enterprise instance" "default" { _ _ _ use dsql = "0" |   |
|---|---|---|

```
  use_dsql = 0
  instance_alias = "tf-testAccDmsEnterpriseInstance1304"
  ecs_region = "cn-qingdao-env17-d01"
  env_type = "test"
  tid = "1"
  instance_source = "RDS"
  dba_uid = "${alibabacloudstack_dms_enterprise_user.default.uid}"
  network_type = "CLASSIC"
  database_user = "${alibabacloudstack_db_account.account.name}"
  export_timeout = "2000"
  safe_rule = "Flexible Management"
  data_link_name = ""
  ddl_online = "0"
  query_timeout = "70"
  instance_type = "mysql"
  host = "${alibabacloudstack_db_instance.instance.connection_string}"
  port = "3306"
  database_password = "${alibabacloudstack_db_account.account.password}"
```

`}`

```bash
# Register a user for your enterprise.
resource "alibabacloudstack_ascm_organization" "default" {
  name = "Test_binder124"
  parent_id = "1"
```

`}`

```
 resource "alibabacloudstack_ascm_user" "user" {
  cellphone_number = "13900000000"
  email = "a***@ascm.com"
  display_name = "admin"
  organization_id = alibabacloudstack_ascm_organization.default.org_id
  mobile_nation_code = "91"
  login_name = "User_Role_Testtf-testAccDmsEnterpriseUser5343882"
  login_policy_id = 1
```

`}`

```
resource "alibabacloudstack_dms_enterprise_user" "default" {
  role_names = [
                 "DBA"
```

`]`

```
  uid = "${alibabacloudstack_ascm_user.user.user_id}"
  nick_name = "tf-testAccDmsEnterpriseUser5343882"
```

`}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|

| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |
|---|---|---|
| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |

| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |
|---|---|---|
| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |
| use dsql _ | Specifies whether to enable cross-instance query. | Valid values: 0: disables cross-instance query. 1: enables cross-instance query. |
| instance alias _ | The name of the database instance. | Specify a name that uniquely distinguishes the instance. |

| ecs region _ | The region of the Elastic Compute Service (ECS) instance. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, choose Products > Elastic Compute Service. 3. In the left-side navigation pane, choose Instances & Images > Instances. On the Instances page, click Create Instance. Then, obtain the region information from the Create Instance wizard page. |
|---|---|---|
| env type _ | The environment type. | Valid values: product: production environment dev: development environment pre: pre-release environment test: test environment sit: system integration test environment uat: user acceptance test environment pet: stress testing environment stag: staging environment |
| tid | The tenant ID. | Example: 1. |
| instance source _ | The source of the database instance. | Valid values: PUBLIC OWN, _ RDS, ECS OWN, and VPC IDC. _ _ |
| dba uid _ | The unique ID (UID) of the database administrator (DBA) for the database instance. | Specify the UID of the DBA for the database instance. |
| network type _ | The network type. | Valid values: CLASSIC and VPC. |

| database user _ | The database account. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, choose Products > ApsaraDB RDS. 3. In the left-side navigation pane, click Instances. On the Instances page, find the instance that you want to manage and click Manage in the Actions column. 4. In the left-side navigation pane, click Accounts. Then, obtain the account information. |
|---|---|---|
| export timeout _ | The timeout period for exporting data from the database instance. | Unit: seconds. |
| safe rule _ | The security rule for the database instance. | Set this parameter to the name of the security rule in your enterprise. |
| data link name _ _ | The name of the data link for cross-database query. | Cross-database query is not supported for instances whose control mode is Flexible Management or Stable Change. |
| ddl online _ | Specifies whether to enable the online data definition language (DDL) service. | This parameter is available only for MySQL and PolarDB. Valid values: 0: The service is disabled. 1: The native online DDL service prevails. 2: The lock-free schema change feature of DMS prevails. |
| query timeout _ | The timeout period for querying data in the database instance. | Unit: seconds. |
| instance type _ | The database type. | Valid values: MySQL, SQLServer, PostgreSQL, Oracle, DRDS, OceanBase, Mongo, and Redis. |
| host | The endpoint of the database instance. | Example: dmstest.rds.aliyun.com. |

| port | The port used to connect to the database instance. | Example: 3306. |
|---|---|---|
| database password _ | The logon password of the database instance. | Specify a custom value. |
| role names _ | The role of the user. | Valid values: USER DBA ADMIN SECURITY ADMIN _ |
| uid | The UID of the user to be added. | 1. Use the username and password of the user account to log on to the Apsara Uni- manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain the UID of the user. |
| nick name _ | The name of the user. | Specify a custom value. |

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.
> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.25 Create a DNS domain name

This topic describes how to use Apsara Stack Terraform to create a DNS domain name.

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" {
  domain="Domain name of ASAPI"
  access_key="Your AccessKey ID"
  secret_key="Your AccessKey secret"
  region="Region"
  proxy= "HTTP://<Proxy endpoint>"
  protocol="HTTP"
  insecure="true"
  resource_group_set_name ="Resource set name"
```

`}`

```bash
# Create a DNS domain name.
resource "alibabacloudstack_dns_domain" "default" {
  domain_name     = "starmove."
  remark   =  "testing Domain"
```

`}`

```
output "dns" {
  value = alibabacloudstack_dns_domain.default.*
```

`}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |

| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
|---|---|---|
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |
| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |
| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |

| domain name _ | The domain name. | The domain name must meet the following requirements: 1. The domain name can be up to 220 characters in length. This includes the period (.) at the end. 2. The domain name can contain multiple domain name segments that are separated by periods (.). A domain name segment can be up to 63 characters in length. The domain name cannot contain consecutive periods (.). 3. The domain name can contain only letters, digits, hyphens (-), and underscores ( ). _ 4. The domain name is not case-sensitive. 5. The domain name must end with a period (.). |
|---|---|---|
| remark | The description of the domain name. | Specify a custom value. |

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.
> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.26 Create DTS resources

This topic describes how to use Apsara Stack Terraform to create a change tracking task, a data synchronization instance, and a data synchronization task of Data Transmission Service (DTS).

**Prerequisites**

A virtual private cloud (VPC), a vSwitch, an ApsaraDB RDS instance, an ApsaraDB RDS database, and a database account are readily available, and required permissions are granted to the database account.

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" {
  domain="Domain name of ASAPI"
  access_key="Your AccessKey ID"
  secretkey="Your AccessKey secret"
```

`_`

```
  region="Region"
  proxy= "HTTP://<Proxy endpoint>"
  protocol="HTTP"
  insecure="true"
  resource_group_set_name ="Resource set name"
```

`}`

```bash
 # Create a change tracking task.
variable "name" {
  default = "tf-testaccdtstf-testacccn-qingdao-env17-d01dtssubscriptionjob90581"
```

`}`

```
variable "creation" {
  default = "Rds"
```

`}`

```
data "alibabacloudstack_zones" "default" {
  available_resource_creation = var.creation
```

`}`

```
resource "alibabacloudstack_vpc" "default" {
  vpc_name       = var.name
  cidr_block     = "172.16.0.0/16"
```

`}`

```
resource "alibabacloudstack_vswitch" "default" {
  vpc_id            = alibabacloudstack_vpc.default.id
  cidr_block        = "172.16.0.0/24"
  availability_zone           = data.alibabacloudstack_zones.default.zones[0].id
  name      = var.name
```

`}`

```
data "alibabacloudstack_db_zones" "default"{
```

`}`

```
resource "alibabacloudstack_db_instance" "instance" {
  engine           = "MySQL"
  engine_version   = "5.6"
  instance_type        = "rds.mysql.s2.large"
  instance_storage     = "30"
  vswitch_id       = alibabacloudstack_vswitch.default.id
  instance_name    = var.name
  storage_type         = "local_ssd"
```

`}`

```
resource "alibabacloudstack_db_database" "db" {
  count       = 2
  instance_id = alibabacloudstack_db_instance.instance.id
  name        = "tfaccountpri_${count.index}"
  description = "from terraform"
  character_set = "UTF8"
```

`}`

```
resource "alibabacloudstack_db_account" "account" {
  instance_id      = alibabacloudstack_db_instance.instance.id
  name        = "tftestprivilege"
  password    = "inputYourCodeHere"
  description = "from terraform"
```

`}`

```
resource "alibabacloudstack_db_account_privilege" "privilege" {
  instance_id  = alibabacloudstack_db_instance.instance.id
  account_name = alibabacloudstack_db_account.account.name
  privilege    = "ReadWrite"
  db_names     = alibabacloudstack_db_database.db.*.name
```

`}`

```
resource "alibabacloudstack_vpc" "default1" {
  vpc_name       = var.name
  cidr_block     = "10.0.0.0/8"
```

`}`

```
resource "alibabacloudstack_vswitch" "default1" {
  vpc_id            = alibabacloudstack_vpc.default1.i
   account_name = alibabacloudstack_db_account.account.name
  privilege    = "ReadWrite"
  db_names     = alibabacloudstack_db_database.db.*.name
```

`}`

```
resource "alibabacloudstack_vpc" "default1" {
  vpc_name       = var.name
  cidr_block     = "10.0.0.0/8"
```

`}`

```
resource "alibabacloudstack_vswitch" "default1" {
  vpc_id            = alibabacloudstack_vpc.default1.id
  cidr_block        = "10.1.0.0/16"
  availability_zone           = data.alibabacloudstack_zones.default.zones[0].id
  name      = var.name
```

`}`

```
resource "alibabacloudstack_vpc" "default2" {
  vpc_name       = var.name
  cidr_block     = "172.16.0.0/16"
```

`}`

```
resource "alibabacloudstack_vswitch" "default2" {
  vpc_id            = alibabacloudstack_vpc.default2.id
  cidr_block        = "172.16.0.0/24"
  availability_zone           = data.alibabacloudstack_zones.default.zones[0].id
  name      = var.name
```

`}`

```
resource "alibabacloudstack_dts_subscription_job" "default" {
  source_endpoint_instance_type = "RDS"
  source_endpoint_password = "inputYourCodeHere"
  subscription_instance_network_type = "vpc"
  payment_type = "PayAsYouGo"
  source_endpoint_database_name = "tfaccountpri_0"
  source_endpoint_user_name = "tftestprivilege"
```

```
  db_list = "{\"tfaccountpri_0\":
{\"name\":\"tfaccountpri_0\",\"all\":true,\"state\":\"normal\"}}"
  source_endpoint_engine_name = "MySQL"
  source_endpoint_region = "cn-hangzhou"
  subscription_instance_vswitch_id = "${alibabacloudstack_vswitch.default1.id}"
  source_endpoint_instance_id = "${alibabacloudstack_db_instance.instance.id}"
  subscription_instance_vpc_id = "${alibabacloudstack_vpc.default1.id}"
  dts_job_name = "tf-testAccCase"
```

`}`

```bash
# Create a data synchronization instance.
variable "name" {
  default = "tf-testacccn-qingdao-env17-d01dtssynchronizationinstance33135"
```

`}`

```
resource "alibabacloudstack_dts_synchronization_instance" "default" {
  sync_architecture = "bidirectional"
  payment_type = "PostPaid"
  source_endpoint_engine_name = "MySQL"
  source_endpoint_region = "cn-qingdao-env17-d01"
  destination_endpoint_engine_name = "MySQL"
  destination_endpoint_region = "cn-qingdao-env17-d01"
  instance_class = "small"
```

`}`

```bash
# Create a data synchronization task.
variable "name" {
  default = "tf-testacccn-qingdao-env17-d01dtssynchronizationjob63487"
```

`}`

```
variable "creation" {
  default = "Rds"
```

`}`

```
data "alibabacloudstack_zones" "default" {
 available_resource_creation = "VSwitch"
```

`}`

```
resource "alibabacloudstack_vpc" "default" {
  vpc_name       = var.name
  cidr_block     = "172.16.0.0/16"
```

`}`

```
resource "alibabacloudstack_vswitch" "default" {
  vpc_id            = alibabacloudstack_vpc.default.id
  cidr_block        = "172.16.0.0/24"
  availability_zone  = "${data.alibabacloudstack_zones.default.zones.0.id}"
  name      = var.name
```

`}`

```
resource "alibabacloudstack_db_instance" "dsinstance" {
  engine           = "MySQL"
  engine_version   = "5.6"
  instance_type        = "rds.mysql.s2.large"
  instance_storage     = "30"
  vswitch_id       = alibabacloudstack_vswitch.default.id
  instance_name    = var.name
  storage_type         = "local_ssd"
```

`}` `}`

```
resource "alibabacloudstack_db_instance" "rsinstance" {
  engine           = "MySQL"
  engine_version   = "5.6"
  instance_type        = "rds.mysql.s2.large"
  instance_storage     = "30"
  vswitch_id       = alibabacloudstack_vswitch.default.id
  instance_name    = var.name
  storage_type         = "local_ssd"
```

`}`

```
resource "alibabacloudstack_db_database" "db" {
  count       = 2
  instance_id = alibabacloudstack_db_instance.dsinstance.id
  name        = "tfaccountpri_${count.index}"
  description = "from terraform"
  character_set =  "UTF8"
```

`}`

```
resource "alibabacloudstack_db_account" "account" {
  instance_id      = alibabacloudstack_db_instance.dsinstance.id
  name        = "tftestdts"
  password    = "inputYourCodeHere"
  description = "from terraform"
```

`}`

```
resource "alibabacloudstack_db_account_privilege" "privilege" {
  instance_id  = alibabacloudstack_db_instance.dsinstance.id
  account_name = alibabacloudstack_db_account.account.name
  privilege    = "ReadWrite"
  db_names     = alibabacloudstack_db_database.db.*.name
```

`}`

```
resource "alibabacloudstack_db_database" "db_r" {
  count       = 2
  instance_id = alibabacloudstack_db_instance.rsinstance.id
  name        = "tfaccountpri_${count.index}"
  description = "from terraform"
character_set = "UTF8"
```

`}`

```
resource "alibabacloudstack_db_account" "account_r" {
  instance_id      =alibabacloudstack_db_instance.rsinstance.id
  name        = "tftestdts"
  password    = "inputYourCodeHere"
  description = "from terraform"
```

`}`

```
resource "alibabacloudstack_db_account_privilege" "privilege_r" {
  instance_id  = alibabacloudstack_db_instance.rsinstance.id
  account_name = alibabacloudstack_db_account.account_r.name
  privilege    = "ReadWrite"
  db_names     = alibabacloudstack_db_database.db_r.*.name
```

`}` `}`

```
resource "alibabacloudstack_dts_synchronization_instance" "default" {
  payment_type                        = "PostPaid"
  source_endpoint_engine_name         = "MySQL"
  source_endpoint_region              = "cn-qingdao-env17-d01"
  destination_endpoint_engine_name    = "MySQL"
  destination_endpoint_region         = "cn-qingdao-env17-d01"
  instance_class                      = "small"
  sync_architecture                   = "oneway"
```

`}`

```
resource "alibabacloudstack_dts_synchronization_job" "default" {
  source_endpoint_instance_id = "${alibabacloudstack_db_instance.rsinstance.id}"
  source_endpoint_engine_name = "MySQL"
  destination_endpoint_database_name = "tfaccountpri_0"
  destination_endpoint_password = "inputYourCodeHere"
  source_endpoint_instance_type = "RDS"
  destination_endpoint_instance_type = "RDS"
  destination_endpoint_engine_name = "MySQL"
  structure_initialization = "true"
  dts_job_name = "tf-testAccCase"
  data_initialization = "true"
  data_synchronization = "true"
  destination_endpoint_instance_id = "${alibabacloudstack_db_instance.dsinstance.id}"
  db_list = "{\"tfaccountpri_0\":
{\"name\":\"tfaccountpri_0\",\"all\":true,\"state\":\"normal\"}}"
  source_endpoint_database_name = "tfaccountpri_0"
  source_endpoint_user_name = "tftestdts"
  destination_endpoint_user_name = "tftestdts"
  source_endpoint_password = "inputYourCodeHere"
  dts_instance_id = "${alibabacloudstack_dts_synchronization_instance.default.id}"
```

`}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|

| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |
|---|---|---|
| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |
| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |

| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
|---|---|---|
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |
| source endpoint instance type _ _ _ | The type of the source instance. | Valid values: RDS, PolarDB, DRDS, LocalInstance, ECS, Express, CEN, and dg. |
| source endpoint password _ _ | The password of the database account used to connect to the source instance. | Specify a custom value. |
| subscription instance network _ _ _ type | The network type for the change tracking task. | Valid values: classic and vpc. |
| payment type _ | The resource billing method. | Valid values: Subscription and PayAsYouGo. |
| source endpoint database na _ _ _ me | The name of the source database. | Specify a custom value. |
| source endpoint user name _ _ _ | The username of the database account used to connect to the source instance. | Specify a custom value. |
| db list _ | The list of databases whose data you want to track. | Set this parameter to a JSON string. |
| source endpoint engine name _ _ _ | The type of the source database. | Valid values: MySQL and Oracle. |

| source endpoint region _ _ | The region where the source database resides. | Example: cn-hangzhou. |
|---|---|---|
| subscription instance vswitch i _ _ _ d | The ID of the vSwitch for the change tracking task. | 1. Log on to the Apsara Uni- manager Management Console. In the top navigation bar, choose Products > Virtual Private Cloud. 2. In the left-side navigation pane, click VSwitches. Obtain the vSwitch ID from the VSwitches page. |
| source endpoint instance id _ _ _ | The ID of the source instance. | ApsaraDB RDS is used as an example in the following steps: 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, choose Products > ApsaraDB RDS. 3. View the instance list and obtain the ID of the instance that you want to manage. |
| subscription instance vpc id _ _ _ | The ID of the VPC for the change tracking task. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, choose Products > Virtual Private Cloud. 3. View the VPC list and obtain the ID of the VPC that you want to manage. |
| dts job name _ _ | The name of the change tracking task. | Specify a value that is 0 to 128 characters in length. |
| sync architecture _ | The synchronization mode. | Valid values: bidirectional and oneway. |
| payment type _ | The resource billing method. | Valid values: Subscription and PayAsYouGo. |

| destination endpoint engine n _ _ _ ame | The type of the destination database. | Valid values: ADS, DB2, DRDS, DataHub, Greenplum, MSSQL, MySQL, PolarDB, PostgreSQL, Redis, Tablestore, as400, clickhouse, kafka, mongodb, odps, oracle, polardb o, _ polardb pg, and tidb. _ |
|---|---|---|
| destination endpoint region _ _ | The region where the destination instance resides. | Example: cn-hangzhou. |
| instance class _ | The instance type. | Valid values: large, medium, micro, small, xlarge, and xxlarge. |
| destination endpoint database _ _ name _ | The name of the destination database. | Specify a custom value. |
| destination endpoint password _ _ | The password of the database account. | Specify a custom value. |
| destination endpoint instance _ _ _ type | The type of the destination instance. | Valid values: ads, CEN, DATAHUB, DG, ECS, EXPRESS, GREENPLUM, MONGODB, OTHER, PolarDB, POLARDBX20, and RDS. |
| destination endpoint instance i _ _ _ d | The ID of the destination instance. | ApsaraDB RDS is used as an example in the following steps: 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, choose Products > ApsaraDB RDS. 3. View the instance list and obtain the ID of the instance that you want to manage. |
| destination endpoint user nam _ _ _ e | The username of the database account used to connect to the destination instance. | Specify a custom value. |
| dts instance id _ _ | The ID of the data synchronization instance. | Set this parameter to the ID of the alibabacloudstack dts synchro _ _ nization instance resource. _ |

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.
> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.27 Create a DBS backup schedule

**schedule**

This topic describes how to use Apsara Stack Terraform to create a Database Backup (DBS) backup schedule.

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" {
  domain="Domain name of ASAPI"
  access_key="Your AccessKey ID"
  secret_key="Your AccessKey secret"
  region="Region"
  proxy= "HTTP://<Proxy endpoint>"
  protocol="HTTP"
  insecure="true"
  resource_group_set_name ="Resource set name"
```

`}`

```bash
 # Create a DBS backup schedule.
variable "name" {
  default = "tf-testacccn-qingdao-env66-d01dbsbackupplan42328"
```

`}`

```
resource "alibabacloudstack_dbs_backup_plan" "default" {
  database_type = "MySQL"
  instance_class = "large"
  backup_method = "logical"
  backup_plan_name = "tf-testacccn-qingdao-env66-d01dbsbackupplan42328"
```

`}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|

| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |
|---|---|---|
| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |
| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |

| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
|---|---|---|
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |
| database type _ | The database type. | Valid values: MySQL Oracle MariaDB PostgreSQL PPAS DRDS MongoDB Redis File |
| instance class _ | The instance type. | Valid values: micro: basic specifications small: low-end specifications medium: medium-end specifications large: high-end specifications xlarge: high-end specifications with no upper limit on the amount of backup data |
| backup method _ | The backup method. | Valid values: logical: logical backup physical: physical backup duplication: dump backup |

| backup plan name _ _ | The name of the backup schedule. | Specify a value that is 0 to 128 characters in length. |
|---|---|---|

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.

> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.28 Create DataHub resources

This topic describes how to use Apsara Stack Terraform to create a project, a topic, and a subscription of DataHub.

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" {
  domain="Domain name of ASAPI"
  access_key="Your AccessKey ID"
  secret_key="Your AccessKey secret"
  region="Region"
  proxy= "HTTP://<Proxy endpoint>"
  protocol="HTTP"
  insecure="true"
  resource_group_set_name ="Resource set name"
```

`}`

```bash
 # Create a project.
resource "alibabacloudstack_datahub_project" "default" {
  name = "tf_testaccdatahubproject746387"
```

`}`

```bash
 # Create a topic.
variable "name" {
    default = "tf_testacc_datahub_785475"
```

`}`

```
  resource "alibabacloudstack_datahub_project" "default" {
    name = "${var.name}"
    comment = "project for basic."
```

`}`

```
resource "alibabacloudstack_datahub_topic" "default" {
  record_schema = {
                    createtopic = "STRING"
```

`}`

```
  name = "tf_testacc_datahub_785475"
  project_name = "${alibabacloudstack_datahub_project.default.name}"
```

`}`

```bash
 # Create a subscription.
variable "project_name" {
    default = "tf_testacc_datahub_project957780"
```

`}`

```
  variable "topic_name" {
    default = "tf_testacc_datahub_topic"
```

`}`

```
  variable "record_type" {
    default = "BLOB"
```

`}`

```
  resource "alibabacloudstack_datahub_project" "basic" {
    name = "${var.project_name}"
    comment = "project for basic."
```

`}`

```
  resource "alibabacloudstack_datahub_topic" "basic" {
    project_name = "${alibabacloudstack_datahub_project.basic.name}"
    name = "${var.topic_name}"
    record_type = "${var.record_type}"
    shard_count = 3
    life_cycle = 7
    comment = "topic for basic."
```

`}`

```
resource "alibabacloudstack_datahub_subscription" "default" {
  project_name = "${alibabacloudstack_datahub_project.basic.name}"
  topic_name = "${alibabacloudstack_datahub_topic.basic.name}"
```

`}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |

| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
|---|---|---|
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |
| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |
| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |

| name | The name of the project. | The name must be 3 to 32 characters in length and can contain letters, digits, and underscores ( ). The name is _ case-insensitive. |
|---|---|---|
| comment | The description of the project. | The description can be up to 255 characters in length. |
| record schema _ | The schema of the topic. | This parameter takes effect only on TUPLE topics. The following data types (case- insensitive) are supported: BIGINT STRING BOOLEAN DOUBLE TIMESTAMP |
| record type _ | The type of the topic. | Valid values: BLOB and TUPLE. In a BLOB topic, the data is organized into binary records and encoded in Base64. In a TUPLE topic, the data has a fixed schema. Default value: TUPLE. |
| shard count _ | The number of shards contained in the topic. | Valid values: 1 to 10. Default value: 1. |
| life cycle _ | The lifecycle of the topic. | Valid values: 1 to 7. Default value: 3. |

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.
> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.29 Create EDAS resources

This topic describes how to use Apsara Stack Terraform to create an Elastic Compute Service (ECS) cluster and an ECS application of Enterprise Distributed Application Service (EDAS).

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define the required resources in the file.

```bash
# Create an ECS application.
variable "name" {
      default = "tf-testacc-edasapplicationbasic2123"
```

`}`

```
resource "alibabacloudstack_vpc" "default" {
  cidr_block = "172.16.0.0/12"
  name       = "${var.name}"
```

`}`

```
resource "alibabacloudstack_edas_cluster" "default" {
  cluster_name = "${var.name}"
  cluster_type = 2
  network_mode = 2
  vpc_id       = "${alibabacloudstack_vpc.default.id}"
```

`}`

```java
resource "alibabacloudstack_edas_application" "default" {
  application_name = "${var.name}"
  package_type = "WAR"
  cluster_id = "${alibabacloudstack_edas_cluster.default.id}"
  component_id = "7"
```

`}`

**Parameters**

**alibabacloudstack_vpc**

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| vpc name _ | The name of the VPC. | The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), and hyphens (- _ ). It must start with a letter and cannot start with http:// or https://. |
| cidr block _ | The CIDR block of the VPC. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, choose Products > Virtual Private Cloud. In the left- side navigation pane, click Virtual Private Clouds. On the Virtual Private Clouds page, obtain the CIDR block of the VPC. 2. You can define a new CIDR block for the VPC. |

**alibabacloudstack_edas_cluster**

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| network mode _ | The network type of the cluster. | Valid values: 1: classic network 2: virtual private cloud (VPC) |
| cluster name _ | The name of the cluster. | The name can be up to 64 characters in length and can contain letters, digits, underscores ( ), and periods (.). _ |
| cluster type _ | The type of the cluster. | Valid values: 2: ECS cluster |

**alibabacloudstack_edas_application**

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| application name _ | The name of the EDAS application. | The name can be up to 36 characters in length and can contain letters, digits, underscores ( ), and hyphens (- _ ). |
| package type _ | The type of the deployment package for the application. | Valid values: WAR and JAR. |
| cluster id _ | The cluster ID of the application. | If you do not configure this parameter, the default cluster ID is used. |

| component id _ | The ID of the component in the container in which the application is deployed. | If you do not configure the runtime environment when you create and deploy an application, you can set this parameter to fellow. The first time you use a WAR package to deploy a native Dubbo or Spring Cloud application, you must specify the version number of the Apache Tomcat component based on the deployed application. You can call the ListClusterOperation operation to query the component ID. The first time you use a WAR package to deploy a non-native Dubbo or Spring Cloud application, you do not need to configure this parameter. |
|---|---|---|

**Execute orchestration**

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

**FAQ**

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.
> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.30 Create Express Connect resources

**resources**

This topic describes how to use Apsara Stack Terraform to create a connection over an Express Connect circuit and create a virtual border router (VBR).

**Create a template file**

Create a file named main.tf and define required resources in the file.

```bash
# Create a connection over an Express Connect circuit.
variable "name" {
  default = "tf-testacccn-qingdao-env17-d01expressconnectphysicalconnection96283"
```

`}`

```
resource "alibabacloudstack_express_connect_physical_connection" "default" {
  device_name = "CSW-VM-VPC-G1.AMTEST17"
  type = "VPC"
  description = "${var.name}"
  access_point_id = "ap-cn-qingdao-env17-d01-amtest17"
  line_operator = "CO"
  peer_location = "testacc12345"
  port_type = "10GBase-LR"
  bandwidth = "5"
  circuit_code = "longtel001"
  physical_connection_name = "tf-testacccn-qingdao-env17-
d01expressconnectphysicalconnection96283"
```

`}`

```bash
# Create a VBR.
variable "name" {
  default = "tf-testacccn-qingdao-env17-d01expressconnectvirtualborderrouter1876"
```

`}`

```
resource "alibabacloudstack_express_connect_virtual_border_router" "default" {
  peer_gateway_ip = "10.0.0.2"
  peering_subnet_mask = "255.255.255.252"
  virtual_border_router_name = "tf-testAcc-PrT1AqAjKvGgLQpbygetjH6f"
  description = "tf-testAcc-llZJhorzazsS81mf2PVyFEAA"
  physical_connection_id = "pc-9wdbvb1hkf44szgqvgnor"
  vlan_id = "1876"
  local_gateway_ip = "10.0.0.1"
```

`}`

**Parameters**

**alibabacloudstack_express_connect_physical_connection**

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|

| device name _ | The name of the access device. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, choose Products > Express Connect. 3. In the left-side navigation pane, click Physical Connection. On the Physical Connection page, click Apply for Physical Connection. 4. Select an access point and obtain the name of the access device. |
|---|---|---|
| type | The type of the Express Connect circuit. | Default value: VPC. |
| description | The description of the Express Connect circuit. | The description must be 2 to 256 characters in length and can contain letters, digits, underscores ( ), hyphens (-), _ periods (.), commas (,), and colons (:). It must start with a letter and cannot start with http:// or https://. |
| access point id _ _ | The ID of the access point. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, choose Products > Express Connect. 3. In the left-side navigation pane, click Physical Connection. On the Physical Connection page, click Apply for Physical Connection. 4. Obtain the access point ID from the Leased line configuration section. |
| line operator _ | The Internet service provider (ISP). | Valid values: CT: China Telecom CU: China Unicom CM: China Mobile CO: other ISPs in China Equinix Others: other ISPs outside China |

| peer location _ | The peer address. | Enter the address of the peer data center connected by using the Express Connect circuit. |
|---|---|---|
| port type _ | The port type. | Valid values: 100Base-T: fast electrical port 1000Base-T: Gigabit electrical port 1000Base-LX: 10 km Gigabit single-mode optical port 10GBase-T: Gigabit electrical port 10GBase-LR: 10 km Gigabit single-mode optical port 40GBase-LR: 40 Gigabit single-mode optical port 100GBase-LR: 100,000 Gigabit single-mode optical port |
| bandwidth | The bandwidth of the port. | Unit: Mbit/s. Valid values: 2 to maximum bandwidth of the port type. |
| physical connection name _ _ | The name of the Express Connect circuit. | The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), and hyphens (- _ ). It must start with a letter and cannot start with http:// or https://. |
| peer gateway ip _ _ | The IPv4 address of the gateway at the customer side. | The value cannot be the same as the IPv4 address of the gateway at the Alibaba Cloud side. |
| peering subnet mask _ _ | The IPv4 subnet mask. | Set this parameter to the subnet mask of the IPv4 addresses that you specify for the VBR and the gateway device in the data center. |
| virtual border router name _ _ _ | The name of the VBR. | The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), and hyphens (- _ ). It must start with a letter. |

| physical connection id _ _ | The ID of the Express Connect circuit. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, choose Products > Express Connect. 3. In the left-side navigation pane, click Physical Connection. On the Physical Connection page, obtain the ID of the Express Connect circuit. |
|---|---|---|
| vlan id _ | The VLAN ID of the VBR. | Valid values: 0 to 2999. The value 0 indicates that no VLAN is configured. |
| local gateway ip _ _ | The IPv4 address of the gateway at the Alibaba Cloud side. | The value cannot be the same as the IPv4 address of the gateway at the customer side. |

**alibabacloudstack_express_connect_virtual_border_router**

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| peer gateway ip _ _ | The IPv4 address of the gateway at the customer side. | The value cannot be the same as the IPv4 address of the gateway at the Alibaba Cloud side. |
| peering subnet mask _ _ | The IPv4 subnet mask. | Set this parameter to the subnet mask of the IPv4 addresses that you specify for the VBR and the gateway device in the data center. |
| virtual border router name _ _ _ | The name of the VBR. | The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), and hyphens (- _ ). It must start with a letter. |

| physical connection id _ _ | The ID of the Express Connect circuit. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, choose Products > Express Connect. 3. In the left-side navigation pane, click Physical Connection. On the Physical Connection page, obtain the ID of the Express Connect circuit. |
|---|---|---|
| vlan id _ | The VLAN ID of the VBR. | Valid values: 0 to 2999. The value 0 indicates that no VLAN is configured. |
| local gateway ip _ _ | The IPv4 address of the gateway at the Alibaba Cloud side. | The value cannot be the same as the IPv4 address of the gateway at the customer side. |

**Execute orchestration**

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

**FAQ**

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.
> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.31 Create an E-HPC job template

**template**

This topic describes how to use Apsara Stack Terraform to create an Elastic High Performance Computing (E-HPC) job template.

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" {
  domain="Domain name of ASAPI"
  access_key="Your AccessKey ID"
  secret_key="Your AccessKey secret"
  region="Region"
  proxy= "HTTP://<Proxy endpoint>"
  protocol="HTTP"
  insecure="true"
  resource_group_set_name ="Resource set name"
```

`}`

```bash
# Create a job template.
variable "name" {
  default = "tf-testacccn-qingdao-env17-d01ehpcjobtemplate81705"
```

`}`

```
resource "alibabacloudstack_ehpc_job_template" "default" {
  job_template_name = "JobTemplateNameT"
  command_line = "./LammpsTest/lammps.pbs"
```

`}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |

| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
|---|---|---|
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |
| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |
| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |

| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |
|---|---|---|
| job template name _ _ | The name of the job template. | The name must be 2 to 64 characters in length and can contain only letters, digits, hyphens (-), and underscores ( ). It must start with a letter. _ |
| command line _ | The job execution command. | N/A |

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

**Important**

> If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.
> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.32 Create an Elasticsearch cluster

**cluster**

This topic describes how to use Apsara Stack Terraform to create an Elasticsearch cluster.

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" {
  domain="Domain name of ASAPI"
  access_key="Your AccessKey ID"
  secret_key="Your AccessKey secret"
  region="Region"
  proxy= "HTTP://<Proxy endpoint>"
  protocol="HTTP"
  insecure="true"
  resource_group_set_name ="Resource set name"
```

`}`

```bash
# Create an Elasticsearch cluster.
resource "alibabacloudstack_elasticsearch_instance" "instance" {
  instance_charge_type = "PostPaid"
  data_node_amount     = "2"
  data_node_spec       = "elasticsearch.sn2ne.large"
  data_node_disk_size  = "20"
  data_node_disk_type  = "cloud_ssd"
  client_node_amount   = "2"
  client_node_spec     = "elasticsearch.sn2ne.large"
  protocol             = "HTTPS"
  vswitch_id           = "some vswitch id"
  password             = "Your password"
  version              = "5.5.3_with_X-Pack"
  description          = "description"
  zone_count           = "2"
  tags = {
    "key1" = "value1"
    "key2" = "value2"
```

`}` `}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|

| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |
|---|---|---|
| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |
| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |

| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
|---|---|---|
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |
| instance charge type _ _ | The billing method of the cluster. | Valid values: PrePaid and PostPaid. Default value: PostPaid. |
| data node amount _ _ | The number of warm nodes in the Elasticsearch cluster. | Valid values: 2 to 50. |
| data node spec _ _ | The specifications of data nodes in the Elasticsearch cluster. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, choose Products > Elasticsearch. 3. Select an organization and a region, and then click the access button below to go to the Elasticsearch homepage. 4. On the Overview page, click Create Cluster. Then, obtain the data node specifications. |

| data node disk size _ _ _ | The storage space of each data node. | The value depends on the disk type. Unit: GiB. If the disk type is SSD cloud disk, the maximum value of this parameter is 2048 GiB or 2 TB. If the disk type is ultra disk, the maximum value of this parameter is 5120 GiB or 5 TB. If the volume of the data that you want to store exceeds 2,048 GiB, you can set this parameter to 2560, 3072, 3584, 4096, 4608, or 5120. If the storage space of the disk for a purchased cluster is less than 2,048 GiB, you can resize the disk to a maximum of 2,048 GiB. |
|---|---|---|
| data node disk type _ _ _ | The storage type. | Valid values: cloud ssd and _ cloud efficiency. _ |
| client node amount _ _ | The number of client nodes in the Elasticsearch cluster. | Valid values: 2 to 25. |
| client node spec _ _ | The client node specifications. | If this parameter is specified, a client node is created. |
| protocol | The protocol for the Elasticsearch cluster. | Valid values: HTTP and HTTPS. Default value: HTTP. |
| vswitch id _ | The ID of the vSwitch. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, choose Products > Virtual Private Cloud. 2. In the left-side navigation pane, click VSwitches. Obtain the vSwitch ID from the VSwitches page. |

| password | The password of the Elasticsearch cluster. | The password must be 8 to 32 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include ! @ # $ % ^ & * ( ) + - _ = |
|---|---|---|
| version | The version of the Elasticsearch cluster. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, choose Products > Elasticsearch. 3. Select an organization and a region, and then click the access button below to go to the Elasticsearch homepage. 4. On the Overview page, click Create Cluster. Then, obtain the version information. |
| description | The description of the cluster. | Set this parameter to a string that is 0 to 30 characters in length. |
| zone count _ | The number of zones supported by the Elasticsearch cluster. | Valid values: 1 to 3. The data node amount value must _ _ be an integer multiple of the zone count value. _ |

| tags | The tags to assign to resources. | key: A key can be up to 128 characters in length. It cannot start with acs: or aliyun. It cannot contain http:// or https://. It cannot be an empty string. value: A value can be up to 128 characters in length. It cannot contain http:// or https://. It can be an empty string. |
|---|---|---|

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

### 2.33 Create an ApsaraDB for HBase cluster

**HBase cluster**

This topic describes how to use Apsara Stack Terraform to create an ApsaraDB for HBase cluster.

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" {
  domain="Domain name of ASAPI"
  access_key="Your AccessKey ID"
  secret_key="Your AccessKey secret"
  region="Region"
  proxy= "HTTP://<Proxy endpoint>"
  protocol="HTTP"
  insecure="true"
  resource_group_set_name ="Resource set name"
```

`}`

```bash
# Create an ApsaraDB for HBase cluster.
data "alibabacloudstack_hbase_zones" "default" {} variable "name" {
  default = "tf-testAcccn-qingdao-env66-d01Vpc2660572"
```

`}`

```
data "alibabacloudstack_zones" "default" {} data "alibabacloudstack_vpcs" "default" {
  name_regex = "default-NODELETING"
```

`}`

```
resource "alibabacloudstack_vpc" "default" { name = var.name cidr_block = "172.16.0.0/16"
```

`}`

```
resource "alibabacloudstack_vswitch" "default" {
  vpc_id            = "${alibabacloudstack_vpc.default.id}"
  cidr_block        = "172.16.0.0/24"
  availability_zone = data.alibabacloudstack_hbase_zones.default.ids.0
  name              = "${var.name}"
```

`}`

```
resource "alibabacloudstack_security_group" "default" {
  count = 2
  vpc_id = alibabacloudstack_vpc.default.id
  name = var.name
```

`}`

```
resource "alibabacloudstack_hbase_instance" "default" {
  cold_storage_size = "900"
  password = "inputYourCodeHere"
  immediate_delete_flag = "true"
  vswitch_id = "${alibabacloudstack_vswitch.default.id}"
  account = "adminu"
  maintain_end_time = "16:00Z"
  zone_id = "${data.alibabacloudstack_zones.default.zones.0.id}"
  coreinstancetype = "hbase.sn1.large"
```

`_`

```
_yp
```

`g`

```
  security_groups = [
                      "${alibabacloudstack_security_group.default.0.id}",
                      "${alibabacloudstack_security_group.default.1.id}"
```

`]`

```
  master_instance_type = "hbase.sn1.large"
  engine_version = "2.0"
  name = "tf-testAcccn-qingdao-env66-d01Vpc2660572"
  deletion_protection = "false"
  core_disk_type = "cloud_efficiency"
  maintain_start_time = "14:00Z"
  tags = {
           Created = "TF-update"
           For = "acceptance test 123"
```

`}`

```
  core_disk_size = "480"
  ip_white = "192.168.1.2"
```

`}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |
| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |

| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |
|---|---|---|
| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |
| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |
| cold storage size _ _ | The cold storage capacity of the cluster. | Unit: GB. Valid values: 0: indicates that cold storage is disabled. 800 to 1000000: indicates that cold storage is enabled. |

| password | The password of the account used to connect to the cluster. | The password must be 0 to 128 characters in length. |
|---|---|---|
| immediate delete flag _ _ | Specifies whether to immediately delete the cluster. | A value of true specifies to immediately delete the cluster. A value of false specifies to delay the deletion of the cluster. |
| account | The username of the account used to connect to the cluster. | The username must be 0 to 128 characters in length. |
| maintain end time _ _ | The end time of the instance maintenance window. | Specify the time in the HH:mmZ format, such as 02:00Z. The time must be in UTC. |
| core instance type _ _ | The core node specifications. | For more information, visitNode specifications. |
| master instance type _ _ | The master node specifications. | For more information, visit Node specifications . |
| engine version _ | The database engine version of the cluster. | Valid values when the engine type is set to hbase: 1.1 and 2.0. Valid value when the engine type is set to hbaseue: 2.0. Valid value when the engine type is set to bds: 1.0. |
| name | The name of the ApsaraDB for HBase cluster. | The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). |
| deletion protection _ | Specifies whether to enable deletion protection for the cluster. | A value of true specifies to enable deletion protection. A value of false specifies to disable deletion protection. If you want to delete a cluster, you must set this parameter to false. |
| core disk type _ _ | The disk type. | Valid values: cloud efficiency, _ cloud ssd, local hdd pro, and _ _ _ local ssd pro. When the engine _ _ type is set to bds, you do not need to specify the disk type. |

| maintain start time _ _ | The start time of the instance maintenance window. | Specify the time in the HH:mmZ format, such as 02:00Z. The time must be in UTC. |
|---|---|---|
| tags | The tags to assign to resources. | N/A |
| core disk size _ _ | The disk size of a core node. | Unit: GB. |
| ip white _ | The IP address whitelist. | If you add 127.0.0.1 to the whitelist, no IP addresses are allowed to access the cluster. If you add CIDR blocks such as 192.168.0.0/24 to the whitelist, all IP addresses that are in the 192.168.0.X format are allowed to access the cluster. Separate multiple IP addresses with commas (,). |

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

### 2.34 Create a Simple Log Service project

**project**

This topic describes how to use Apsara Stack Terraform to create a Simple Log Service project.

**Create a template file**

Create a file named main.tf and define the required resources in the file.

```
variable "name" {
 description = "The specification of moduele name."
 type = string
 default = "iac-tf-log-project"
```

`}`

```
variable description {
 description = "The specification of moduele description ."
 type = string
 default = "create-iac-tf-log-project"
```

`}`

```
resource "alibabacloudstack_log_project" "default" {
 name = var.name
 description = var.description
```

`}`

**Parameters**

**alibabacloudstack_log_project**

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|

| name | The name of the Simple Log Service project. | 1. The name can contain lowercase letters, digits, and hyphens (-). 2. The name must start and end with a lowercase letter or a digit. 3. The name must be 3 to 63 characters in length. |
|---|---|---|
| description | The description of the Simple Log Service project. | The description cannot contain angle brackets <>, apostrophes ('), backslashes (\), double quotation marks ("), or double backslashes (\\). It can be up to 64 characters in length. |

**Execute orchestration**

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

**FAQ**

**Important**

> If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.
> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.35 Create an ApsaraDB for MongoDB instance

**MongoDB instance**

This topic describes how to use Apsara Stack Terraform to create ApsaraDB for MongoDB replica set and sharded cluster instances.

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" {
  domain="Domain name of ASAPI"
  access_key="Your AccessKey ID"
  secret_key="Your AccessKey secret"
  region="Region"
  proxy= "HTTP://<Proxy endpoint>"
  protocol="HTTP"
  insecure="true"
  resource_group_set_name ="Resource set name"
```

`}`

```
#Createareplicasetinstance
```

```bash
# Create a replica set instance.
data "alibabacloudstack_zones" "default" {
```

`}`

```
provider "alibabacloudstack" {
  assume_role {}
```

`}`

```
resource "alibabacloudstack_mongodb_instance" "default" {
  zone_id             = data.alibabacloudstack_zones.default.zones[0].id
  engine_version      = "3.4"
  db_instance_storage = 30
  db_instance_class   = "dds.mongo.standard"
  name                = "tf-testAccMongoDBInstance_test_together"
  account_password    = "inputYourCodeHere"
  security_ip_list    = ["10.168.1.12", "10.168.1.13"]
  backup_period       = ["Tuesday", "Wednesday"]
  backup_time         = "10:00Z-11:00Z"
  ssl_action          = "Open"
```

`}`

```bash
# Create a sharded cluster instance.
provider "alibabacloudstack" {
  assume_role {}
```

`}`

```
data "alibabacloudstack_zones" "default" {
  available_resource_creation = "MongoDB"
```

`}`

```
resource "alibabacloudstack_mongodb_sharding_instance" "default" {
  zone_id        = "${data.alibabacloudstack_zones.default.zones.0.id}"
  engine_version = "3.4"
  shard_list {
    node_class   = "dds.shard.mid"
    node_storage = 10
```

`}`

```
  shard_list {
    node_class   = "dds.shard.standard"
    node_storage = 20
```

`}`

```
  shard_list {
    node_class   = "dds.shard.standard"
    node_storage = 20
```

`}`

```
  mongo_list {
    node_class = "dds.mongos.mid"
```

`}`

```
  mongo_list {
    node_class = "dds.mongos.mid"
```

`}`

```
   mongo_list {
    node_class = "dds.mongos.mid"
```

`}`

```
  name             = "tf-testAccMongoDBShardingInstance_test_together"
  account_password = "inputYourCodeHere"
  backupperiod    = ["Tuesday", "Wednesday"]
```

```
p_p
```

`y``,` `y`

```
  backup_time      = "10:00Z-11:00Z"
  security_ip_list = ["10.168.1.12", "10.168.1.13"]
```

`}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |
| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |

| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |
|---|---|---|
| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |
| engine version _ | The database engine version. | Valid values: 6.0 5.0 4.4 4.2 4.0 |
| db instance storage _ _ | The instance storage capacity. | Unit: GB. Valid values: 10 to 3000. The value must be a multiple of 10. |
| db instance class _ _ | The instance type. | For more information about specific instance specifications, see the following topics: Replica set instance types Sharded cluster instance types |

| name | The name of the instance. | The name must be 2 to 256 characters in length. |
|---|---|---|
| account password _ | The password of the root account. | The password must meet the following requirements: The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include ! # $ % ^ & * ( ) + - = _ The password must be 8 to 32 characters in length. |
| security ip list _ _ | The IP address whitelist of the instance. | Separate multiple IP addresses with commas (,). Ensure that each IP address is unique in a whitelist. The following types of values are supported: 0.0.0.0/0 IP addresses, such as 10.23.12.24. CIDR blocks, such as 10.23.12.0/24. In this case, 24 indicates that the prefix of each IP address is 24-bit long. You can replace 24 with a value within the range of 1 to 32. |
| backup period _ | The day of a week on which to back up data of the ApsaraDB for MongoDB instance. | This parameter is required if backup time is specified. Valid _ values: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, and Sunday. |
| backup time _ | The backup window of the ApsaraDB for MongoDB instance. | This parameter is required if backup period is specified. _ Specify the window in the HH:mmZ-HH:mmZ format. Set the time interval to 1 hour. If this parameter is not specified, the system returns a default value, such as 23:00Z-24:00Z. |

| SSL action _ | The operation on the SSL feature. | Valid values: Open: enables SSL encryption. Close: disables SSL encryption. Update: updates the SSL certificate. |
|---|---|---|
| shard list _ | The number of available shard nodes. | Valid values: 2 to 32. |
| node class _ | The node type. | For more information about the specifications of shard or mongos nodes, see the following topics: Replica set instance types Sharded cluster instance types |
| node storage _ | The storage capacity of a node. | Valid values: 10 to 1000. |
| mongo lis _ | The number of available mongos nodes. | Valid values: 2 to 32. |

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

### 2.36 Create NAS resources

This topic describes how to use Apsara Stack Terraform to create a file system, a mount target, a permission group, and a permission group rule of Apsara File Storage NAS (NAS).

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" {
  domain="Domain name of ASAPI"
  access_key="Your AccessKey ID"
  secret_key="Your AccessKey secret"
  region="Region"
  proxy= "HTTP://<Proxy endpoint>"
  protocol="HTTP"
  insecure="true"
  resource_group_set_name ="Resource set name"
```

`}`

```bash
# Create a permission group.
resource "alibabacloudstack_nas_access_group" "foo" {
  access_group_name = "tf-NasConfigName"
  access_group_type = "Classic"
  description       = "test_AccessG"
```

`}`

```bash
# Create a permission group rule.
resource "alibabacloudstack_nas_access_rule" "foo" {
  access_group_name = alibabacloudstack_nas_access_group.foo.access_group_name
  source_cidr_ip    = "xxx.xxx.1.0/16"
  rw_access_type    = "RDWR"
  user_access_type  = "no_squash"
  priority          = 2
```

`}`

```bash
# Create a file system.
resource "alibabacloudstack_nas_file_system" "example" {
  protocol_type = "NFS"
  storage_type  = "Capacity"
```

`}`

```bash
# Create a mount target.
variable "name" {
  default = "tf-testAcccn-wulan-env180-d01AlibabacloudStackNasMountTarget74221"
```

`}`

```
variable "name1" {
```

```
  default = "tf-testAcccn-wulan-env180-d01AlibabacloudStackNasMountTarget74221change"
```

`}`

```
data "alibabacloudstack_nas_protocols" "example" {
  type = "Performance"
```

`}`

```
resource "alibabacloudstack_vpc" "default" {
  cidr_block = "172.16.0.0/16"
  name = "${var.name}"
```

`}`

```
data "alibabacloudstack_nas_zones" "default" {
```

`}`

```
data "alibabacloudstack_zones" "default" {
  available_resource_creation = "VSwitch"
```

`}`

```
resource "alibabacloudstack_vswitch" "default" {
  vpc_id = "${alibabacloudstack_vpc.default.id}"
  cidr_block = "172.16.0.0/21"
  availability_zone = "${data.alibabacloudstack_zones.default.zones.0.id}"
  name = "${var.name}"
```

`}`

```
resource "alibabacloudstack_security_group" "example" {
  name = var.name
  vpc_id = "${alibabacloudstack_vpc.default.id}"
```

`}`

```
resource "alibabacloudstack_nas_file_system" "example" {
  protocol_type = "${data.alibabacloudstack_nas_protocols.example.protocols.0}"
  storage_type = "Capacity"
```

`}`

```
resource "alibabacloudstack_nas_access_group" "example" {
  access_group_name = "${var.name}"
  access_group_type = "Vpc"
```

`}`

```
resource "alibabacloudstack_nas_mount_target" "default" {
  access_group_name = "${alibabacloudstack_nas_access_group.example.access_group_name}"
  file_system_id = "${alibabacloudstack_nas_file_system.example.id}"
  vswitch_id = "${alibabacloudstack_vswitch.default.id}"
  security_group_id = "${alibabacloudstack_security_group.example.id}"
```

`}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|

| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |
|---|---|---|
| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |

| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |
|---|---|---|
| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |
| access group name _ _ | The name of the permission group. | The name must be 3 to 64 characters in length and can contain letters, digits, and hyphens (-). |
| access group type _ _ | The type of the permission group. | Valid values: Vpc and Classic. |
| source cidr ip _ _ | The IP address or CIDR block of the authorized object. | You can specify only a single IP address or CIDR block, such as 10.10.1.123 or 192.168.3.0/24. |
| rw access type _ _ | The read/write permission type. | Valid values: RDWR and RDONLY. Default value: RDWR. |
| user access type _ _ | The type of access permissions for different types of users. | Valid values: no squash, _ root squash, and all squash. _ _ Default value: no squash. _ |

| priority | The priority. | Valid values: 1 to 100. Default value: 1. |
|---|---|---|
| protocol type _ | The protocol type of the file system. | Valid values: NFS and SMB. The value SMB is available when file system type is set to _ _ standard. |
| storage type _ | The storage type of the file system. | Valid values: Performance: This value is available when file system type is set to _ _ standard. Capacity: This value is available when file system type is set to _ _ standard. standard: This value is available when file system type is set to _ _ extreme. advance: This value is available when file system type is set to _ _ extreme. |
| file system type _ _ | The type of the file system. | Valid values: standard and extreme. Default value: standard. Note that extreme is available only for file systems in virtual private clouds (VPCs). |

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the execution plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.
> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.37 Create OOS resources

This topic describes how to use Apsara Stack Terraform to create an execution and a template of Operation Orchestration Service (OOS).

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" {
  domain="Domain name of ASAPI"
  access_key="Your AccessKey ID"
  secret_key="Your AccessKey secret"
  region="Region"
```

`g` `g`

```
  proxy= "HTTP://<Proxy endpoint>"
  protocol="HTTP"
  insecure="true"
  resource_group_set_name ="Resource set name"
```

`}`

```bash
# Create an execution.
resource "alibabacloudstack_oos_template" "default" {
  content       = <<EOF
```

`{`

```json
    "FormatVersion": "OOS-2019-06-01",
    "Description": "Update Describe instances of given status",
    "Parameters":{
      "Status":{
        "Type": "String",
        "Description": "(Required) The status of the Ecs instance."
```

`}` `},`

```json
    "Tasks": [
```

`{`

```json
        "Properties" :{
          "Parameters":{
            "Status": "{{ Status }}"
```

`},`

```json
          "API": "DescribeInstances",
          "Service": "Ecs"
```

`},`

```json
        "Name": "foo",
        "Action": "ACS::ExecuteApi"
```

`}]` `}`

```
  EOF
  template_name = "test-name"
  version_name  = "test"
  tags = {
    "Created" = "TF",
    "For"     = "acceptance Test"
```

`}` `}`

```json
resource "alibabacloudstack_oos_execution" "example" {
  template_name = alibabacloudstack_oos_template.default.template_name
  description   = "From TF Test"
  parameters    = <<EOF
            {"Status":"Running"}
         EOF
```

`}`

```bash
# Create a template.
resource "alicloud_oos_template" "example" {
  content       = <<EOF
```

`{`

```json
    "FormatVersion": "OOS-2019-06-01",
    "Description": "Update Describe instances of given status",
```

```json
    "Parameters":{
      "Status":{
        "Type": "String",
        "Description": "(Required) The status of the Ecs instance."
```

`}` `},`

```json
    "Tasks": [
```

`{`

```json
        "Properties" :{
          "Parameters":{
            "Status": "{{ Status }}"
```

`},`

```json
          "API": "DescribeInstances",
          "Service": "Ecs"
```

`},`

```json
        "Name": "foo",
        "Action": "ACS::ExecuteApi"
```

`}]` `}`

```
  EOF
  template_name = "test-name"
  version_name  = "test"
  tags = {
    "Created" = "TF",
    "For"     = "acceptance Test"
```

`}` `}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |

| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
|---|---|---|
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |
| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |
| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |

| Description | The description of the OOS execution. | The description can be up to 200 characters in length. |
|---|---|---|
| Parameters | The parameters required by the template. | Default value: {}. |
| template name _ | The name of the template. | The name can be up to 128 characters in length, and can contain letters, digits, hyphens (-), and underscores ( ). It _ cannot start with ALIYUN, ACS, ALIBABA, or ALICLOUD. |
| version name _ | The name of the template version. | Specify a custom value. |
| tags | The tags to assign to the resources. | Specify a custom value. |

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

**Important**

> If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.
> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.38 Create Quick BI resources

This topic describes how to use Apsara Stack Terraform to create an organization user, a user group, and a workspace of Quick BI.

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" {
  domain="Domain name of ASAPI"
  access_key="Your AccessKey ID"
  secret_key="Your AccessKey secret"
  region="Region"
  proxy= "HTTP://<Proxy endpoint>"
  protocol="HTTP"
  insecure="true"
  resource_group_set_name ="Resource set name"
```

`}`

```bash
# Create an organization user.
resource "alibabacloudstack_quick_bi_user" "example" {
  account_name    = "example_value"
  admin_user      = false
  auth_admin_user = false
  nick_name       = "example_value"
  user_type       = "Analyst"
```

`}`

```bash
# Create a user group.
resource "alibabacloudstack_quick_bi_user_group" "example" {
  user_group_name = "example_value"
  user_group_description = "example_value"
  parent_user_group_id = "-1"
```

`}`

```bash
# Create a workspace.
resource "alibabacloudstack_quick_bi_workspace" "default" {
  workspace_name = "example_value"
  workspace_desc = "example_value"
  use_comment = "false"
  allow_share = "false"
  allow_publish = "false"
```

`}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|

| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |
|---|---|---|
| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |
| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |

| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
|---|---|---|
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |
| account name _ | The name of the Apsara Stack tenant account. | The name cannot contain colons (:). |
| admin user _ | Specifies whether the user is an administrator. | Valid values: true and false. |
| auth admin user _ _ | Specifies whether the user is a permission administrator. | Valid values: true and false. |
| nick name _ | The alias of the user. | The alias can contain only letters, digits, underscores ( ), _ hyphens (-), forward slashes (/), backslashes (\), vertical bars (\|), parentheses (), and brackets []. The alias can contain a maximum of 50 characters in length. |
| user type _ | The type of the user. | Valid values: Analyst, Developer, and Visitor. |
| user group name _ _ | The name of the user group. | Specify a custom value. |
| user group description _ _ | The description of the user group. | Specify a custom value. |
| parent user group id _ _ _ | The ID of the parent user group. | You can add new user groups to this group. If you enter -1, a newly created user group is added to the root directory. |

| workspace name _ | The name of the workspace. | Specify a custom value. |
|---|---|---|
| workspace desc _ | The description of the workspace. | Specify a custom value. |
| use comment _ | Specifies whether to use table comments. | Valid values: true and false. |
| allow share _ | Specifies whether the work can be shared. | Valid values: true and false. |
| allow publish _ | Specifies whether the work can be published. | Valid values: true and false. |

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.

> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.39 Create ROS resources

This topic describes how to use Apsara Stack Terraform to create a stack and a custom template of Resource Orchestration Service (ROS).

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" {
  domain="Domain name of ASAPI"
  access_key="Your AccessKey ID"
  secret_key="Your AccessKey secret"
  region="Region"
  proxy= "HTTP://<Proxy endpoint>"
  protocol="HTTP"
  insecure="true"
  resource_group_set_name ="Resource set name"
```

`}`

```bash
# Create an ROS stack.
resource "alibabacloudstack_ros_stack" "example" {
  stack_name        = "tf-testaccstack"
  template_body     = <<EOF
```

`{`

```json
       "ROSTemplateFormatVersion": "2015-09-01"
```

`}`

```
    EOF
  stack_policy_body = <<EOF
```

`{`

```json
       "Statement": [{
          "Action": "Update:Delete",
          "Resource": "*",
          "Effect": "Allow",
          "Principal": "*"
```

`}]` `}`

```
    EOF
```

`}`

```bash
# Create an ROS custom template.
resource "alibabacloudstack_ros_template" "example" {
  template_name = "example_value"
  template_body = <<EOF
```

`{`

```json
       "ROSTemplateFormatVersion": "2015-09-01"
```

`}`

```
    EOF
```

`}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|

| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |
|---|---|---|
| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |
| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |

| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
|---|---|---|
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |
| stack name _ | The name of the stack. | The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores ( ). It must _ start with a digit or letter. |
| template body _ | The template body. | The template body must be 1 to 524,288 bytes in length. If the template body is longer than required, we recommend that you add parameters to the HTTP POST request body to avoid request failures due to excessive length of URLs. |
| stack policy body _ _ | The stack policy body. | The stack policy body must be 1 to 16,384 bytes in length. |
| template name _ | The name of the template. | The name can be up to 255 characters in length, and can contain digits, letters, hyphens (-), and underscores ( ). It must _ start with a digit or letter. |

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.
> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.40 Create a KVStore for Redis instance

**instance**

This topic describes how to use Apsara Stack Terraform to create a KVStore for Redis instance.

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" {
  domain="Domain name of ASAPI"
  access_key="Your AccessKey ID"
  secret_key="Your AccessKey secret"
  region="Region"
  proxy= "HTTP://<Proxy endpoint>"
  protocol="HTTP"
  insecure="true"
  resource_group_set_name ="Resource set name"
```

`}`

```bash
# Create a KVStore for Redis instance.
variable "creation" {
  default = "KVStore"
```

`}`

```
variable "name" {
  default = "kvstoreinstancevpc"
```

`}`

```
data "alibabacloudstack_zones" "default" {
  available_resource_creation = "${var.creation}"
```

`}`

```
resource "alibabacloudstack_vpc" "default" {
  name       = "${var.name}"
  cidr_block = "172.16.0.0/16"
```

`}`

```
resource "alibabacloudstack_vswitch" "default" {
  vpc_id            = "${alibabacloudstack_vpc.default.id}"
  cidr_block        = "172.16.0.0/24"
  availability_zone = "${data.alibabacloudstack_zones.default.zones.0.id}"
  name              = "${var.name}"
```

`}`

```
resource "alibabacloudstack_kvstore_instance" "default" {
  instance_class = "redis.master.stand.default"
  instance_name  = "${var.name}"
  vswitch_id     = "${alibabacloudstack_vswitch.default.id}"
  private_ip     = "172.16.0.10"
  security_ips   = ["10.0.0.1"]
  instance_type  = "Redis"
```

`}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |
| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |

| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |
|---|---|---|
| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |
| instance class _ | The instance type. | You can query the instance type from the alibabacloudstack kvstore inst _ _ ance classes data source. _ |
| instance name _ | The name of the instance. | The name must be 2 to 128 characters in length and can contain letters, digits, underscores ( ), and hyphens (- _ ). It must start with a letter. |
| private ip _ | The private IP address. | Specify a value such as 172.16.0.***. |
| security ips _ | The IP address whitelist. | To allow all IP addresses to access the instance, add 0.0.0.0/0 to the whitelist. To block access from all IP addresses, add 127.0.0.1 to the whitelist. Separate multiple IP addresses with commas (,). |

| instance type _ | The instance category. | Valid values: Redis and Memcache. Default value: Redis. |
|---|---|---|

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.

> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.41 Create Tablestore resources

This topic describes how to use Apsara Stack Terraform to create a Tablestore instance, bind a Tablestore instance to a virtual private cloud (VPC), and create a Tablestore table.

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" {
  domain="Domain name of ASAPI"
  access_key="Your AccessKey ID"
  secret_key="Your AccessKey secret"
  region="Region"
  proxy= "HTTP://<Proxy endpoint>"
  protocol="HTTP"
  insecure="true"
  resource_group_set_name ="Resource set name"
```

`}`

```bash
# Create a Tablestore instance.
resource "alibabacloudstack_ots_instance" "foo" {
  name        = "my-ots-instance"
  description = "for table"
  accessed_by = "Vpc"
  tags = {
    Created = "TF"
    For     = "Building table"
```

`}` `}`

```bash
# Bind a Tablestore instance to a VPC.
resource "alibabacloudstack_ots_instance" "foo" {
  name        = "my-ots-instance"
  description = "for table"
  accessed_by = "Vpc"
  tags = {
    Created = "TF"
    For     = "Building table"
```

`}` `}`

```
data "alibabacloudstack_zones" "foo" {
  available_resource_creation = "VSwitch"
```

`}`

```
resource "alibabacloudstack_vpc" "foo" {
  cidr_block = "172.16.0.0/16"
  name       = "for-ots-instance"
```

`}`

```
resource "alibabacloudstack_vswitch" "foo" {
  vpc_id            = alibabacloudstack_vpc.foo.id
  vswitch_name      = "for-ots-instance"
  cidr_block        = "172.16.1.0/24"
  zone_id           = data.alibabacloudstack_zones.foo.zones[0].id
```

`}`

```
resource "alibabacloudstack_ots_instance_attachment" "foo" {
  instance_name = alibabacloudstack_ots_instance.foo.name
  vpc_name      = "attachment1"
  vswitch_id    = alibabacloudstack_vswitch.foo.id
```

`}`

```bash
# Create a Tablestore table.
variable "name" {
  default = "terraformtest"
```

`}`

```
resource "alibabacloudstack_ots_instance" "foo" {
  name        = var.name
  description = var.name
  accessed_by = "Any"
  tags = {
    Created = "TF"
    For     = "acceptance test"
```

`}` `}`

```
resource "alibabacloudstack_ots_table" "basic" {
  instance_name = alibabacloudstack_ots_instance.foo.name
  table_name    = var.name
  primary_key {
    name = "pk1"
    type = "Integer"
```

`}`

```
  primary_key {
    name = "pk2"
    type = "String"
```

`}`

```
  primary_key {
    name = "pk3"
    type = "Binary"
```

`}`

```
timetolive =-1
```

```
  time_to_live                   1
  max_version                   = 1
  deviation_cell_version_in_sec = 1
```

`}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |
| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |

| region | The region. | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |
|---|---|---|
| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |
| name | The name of the Tablestore instance. | The name must be 3 to 16 characters in length and can contain letters, digits, and hyphens (-). It can start with a letter and cannot start with case-insensitive string ali or ots. |
| description | The description of the instance. | The description must be 0 to 256 characters in length. |

| accessed by _ | The networks over which you can access the instance. | Valid values: Any: allows access to the instance over any network. Vpc: allows access to the instance only over the VPC bound to the instance. ConsoleOrVpc: allows access to the instance over the KVStore for Redis console or the VPC bound to the instance. |
|---|---|---|
| tags | The tags to assign to the instance. | Specify a custom value. |
| vpc name _ | The name of the VPC. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, choose Products > Virtual Private Cloud. In the left- side navigation pane, click Virtual Private Clouds. Then, obtain the name of the VPC. |
| vswitch id _ | The ID of the vSwitch. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, choose Products > Virtual Private Cloud. 2. In the left-side navigation pane, click VSwitches. Obtain the vSwitch ID from the VSwitches page. |
| table name _ | The name of the table in the Tablestore instance. | 1. The name can contain only letters, digits, and underscores ( ). _ 2. The name must start with a letter or underscore ( ). _ The name must be 1 to 255 characters in length. |

| primary key _ | The primary keys of the table. | A table can have a maximum of four primary keys. 1. A primary key can contain only letters, digits, and underscores ( ). _ 2. A primary key must start with a letter or underscore ( ). _ 3. A primary key must be 1 to 255 characters in length. 4. A primary key cannot be modified after it is created. |
|---|---|---|
| primary key (type) _ | The type of the primary key. | Valid values: Integer, String, and Binary. |
| time to live _ _ | The time-to-live (TTL) of data. | The TTL must be at least 86,400 seconds (one day) or -1. A value of -1 specifies that the data never expires. |
| max version _ | The maximum number of versions of data. | Data versions cannot be 0. |
| deviation cell version in sec _ _ _ _ | The maximum version offset of data. | Valid values: 1 to 9223372036854775807. Default value: 86400. |

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.
> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.

### 2.42 Create VPN Gateway resources

**resources**

This topic describes how to use Apsara Stack Terraform to create a VPN gateway and a customer gateway.

**Procedure**

**Create a Terraform template file**

Create a file named terraform.tf and define required resources in the file.

```bash
# Environment configuration
provider "alibabacloudstack" {
  domain="Domain name of ASAPI"
  access_key="Your AccessKey ID"
  secret_key="Your AccessKey secret"
  region="Region"
  proxy= "HTTP://<Proxy endpoint>"
  protocol="HTTP"
  insecure="true"
  resource_group_set_name ="Resource set name"
```

`}`

```bash
# Create a virtual private cloud (VPC).
resource "alibabacloudstack_vpc" "vpc" {
  name       = "tf_test_foo"
  cidr_block = "172.16.0.0/12"
```

`}`

```bash
# Create a vSwitch.
resource "alibabacloudstack_vswitch" "vsw" {
  vpc_id            = alibabacloudstack_vpc.vpc.id
  cidr_block        = "172.16.0.0/21"
  availability_zone = "cn-wulan-env180-amtest180001-a"
```

`}`

```bash
# Create a VPN gateway.
resource "alibabacloudstack_vpn_gateway" "foo" {
  name                 = "vpnGatewayConfig"
  vpc_id               = alibabacloudstack_vpc.vpc.id
  bandwidth            = "10"
  enable_ssl           = true
  instance_charge_type = "PostPaid"
  description          = "test_create_description"
  vswitch_id           = alibabacloudstack_vswitch.vsw.id
```

`}`

```bash
# Create a customer gateway.
resource "alibabacloudstack_vpn_customer_gateway" "foo" {
  name        = "vpnCgwNameExample"
  ip_address  = "xxx.xxx.xxx.xxx"
  description = "vpnCgwDescriptionExample"
```

`}` The following table describes the parameters.

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|

| domain | The domain name of ASAPI. | 1. Log on to the Apsara Infrastructure Management console 1.0. 2. In the top navigation bar, choose Reports > System Reports. 3. Click Registration Vars of Services in the Report column. 4. Click the filter icon next to Service, enter asapi, and then click Apply Filter. 5. Right-click the item in the Service Registration column corresponding to asapi, and select Show More. 6. View the details to obtain the value of asapi.gateway.endpoint. |
|---|---|---|
| access key _ | Your AccessKey ID. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey ID. |
| secret key _ | Your AccessKey secret. | 1. Use your account username and password to log on to the Apsara Uni-manager Management Console. 2. Click the cloud logo in the upper-right corner of the homepage and select User Information. 3. Obtain your AccessKey secret. |

| region | Region | 1. Log on to the Apsara Uni- manager Management Console. 2. In the top navigation bar, click Enterprise. Then, choose Resources > Regions in the left-side navigation pane. 3. Select the organization that you want to manage and obtain the name of the region. |
|---|---|---|
| proxy | The proxy endpoint that is used to access the environment. | If you do not need to use a proxy endpoint to access the environment, you do not need to configure this parameter. |
| insecure | Specifies whether to ignore insecure HTTPS certificates. | Valid values: true and false. A value of true specifies to ignore insecure HTTPS certificates. |
| resource group set name _ _ _ | The name of the resource set. | 1. In the top navigation bar of the Apsara Uni-manager Management Console, click Enterprise. 2. Choose Resources > Resource Sets in the left-side navigation pane, and obtain the name of the resource set. |
| name | The name of the VPN gateway. | The name must be 2 to 100 characters in length and can contain letters, digits, underscores ( ), and hyphens (- _ ). It must start with a letter and cannot start with http:// or https://. |
| instance charge type _ _ | The billing method. | Valid values: PostPaid and PrePaid. Default value: PostPaid. |
| bandwidth | The bandwidth. | Valid values: 5, 10, 20, 50, and 100. |

| enable ssl _ | Specifies whether to enable SSL-VPN. | Valid values: true and false. Default value: false. |
|---|---|---|
| ip address _ | The IP address of the customer gateway. | Specify a custom value. |

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

### 2.43 Create an Apsara Stack disk

This topic describes how to use Apsara Stack Terraform to create a disk.

**Create a template file**

Create a file named main.tf and define the required resources in the file.

```
variable "name" {
 description = "Name used on all disks as prefix. Like TF_ECS_Disk-1, TF_ECS_Disk-2."
 default = "TF_ECS_Disk"
```

`}`

```
variable "disk_count" {
 description = "Number of disks to launch."
 default = 1
```

`}`

```
variable "category" {
 description = "The data disk category used to launch one or more data disks.such as cl
oud_efficiency,cloud_pperf"
 default = "cloud_pperf"
```

`}`

```
// ECS Disk Resource for Module module "disk" {
 source = "./terraform-alibabacloudstack-disk"
 name = var.name
 category = var.category
 count = var.disk_count
```

`}` Create a file named main.tf in the terraform-alibabacloudstack-disk/ directory and define the required resources in the file.

```
// Zones data source for availability_zone data "alibabacloudstack_zones" "this" {
  available_resource_creation  = "Instance"
  enable_details               = true
```

`}`

```
// ECS Disk Resource for Module resource "alibabacloudstack_disk" "this" {
  availability_zone     = data.alibabacloudstack_zones.this.zones[0].id
  name                  = var.disk_count < 2 ?  var.name : format("%s%s", var.name, form
at("%02d", count.index + 1))
  category              = var.category
  size                  = var.size
  encrypted             = var.encrypted
  count                 = var.disk_count
  tags = merge(
```

`{`

```
      "Name" = format("%s", var.name)
```

`},`

```
    var.tags,
```

`)` `}` Create a file named variables.tf in the terraform-alibabacloudstack-disk/ directory and define the required resources in the file.

```bash
# Disk variables
variable "name" {
  description = "Name used on all disks as prefix. Like TF_ECS_Disk-1, TF_ECS_Disk-2."
  default     = "TF_ECS_Disk"
```

`}`

```
variable "category" {
  description = "The data disk category used to launch one or more data disks."
  default     = "cloud_pperf"
```

`}`

```
variable "size" {
  description = "The data disk size used to launch one or more data disks."
  default     = "40"
```

`}`

```
variable "tags" {
  description = "Used to mark specified ecs data disks. Name will be merged into tags a
utomactially."
  type        = map(string)
  default = {
    created_by   = "Terraform"
    created_from = "module-terraform-alicloud-disk"
```

`}` `}`

```
variable "encrypted" {
  description = "Whether to encrypt the disks"
  default     = false
```

`}`

```
variable "disk_count" {
  description = "Number of disks to launch."
  default     = 1
```

`}`

**Parameters**

**alibabacloudstack_disk**

| Parameter | Description | Method to obtain the parameter value |
|---|---|---|
| availability zone _ | The zone. | This parameter specifies the zone in which a disk is created. |

| name | The name of the disk. | The name can be 2 to 128 characters in length and can contain only letters, hyphens (- ), periods (.), and underscores ( ). It cannot start or end with a _ hyphen (-), http://, or https://. Default value: null. |
|---|---|---|
| category | The category of the disk. | Valid values: cloud, cloud efficiency, and cloud ssd. _ _ Default value: cloud. |
| size | The size of the disk. | When you resize a disk, the new size must be greater than the original size. Otherwise, the error message "InvalidDiskSize.TooSmall" is returned. |
| encrypted | Specifies whether to encrypt a disk. | If you set this parameter to true, the disk is encrypted. |
| disk count _ | The number of disks. | This parameter specifies the number of disks that you want to start. |
| tag | The tag of the disk. | This parameter is used to tag a specific ECS data disk. The name is automatically incorporated into the tag. |

**Execute orchestration**

**Initialize your Terraform configuration**

Before you run the terraform.tf template, you must initialize your Terraform configuration. For more information, see Initialize your Terraform configuration.

**View the Terraform plan**

View the planned resources in the terraform.tf file. Procedure:
1. Run the `terraform plan` command.
2. View information about the planned resources in the terraform.tf file.

**Run the Terraform template**

Execute the Terraform plan in the terraform.tf file to create resources. Procedure:
1. Run the `terraform apply` command to create resources specified in the terraform.tf file.
2. Enter `yes` to confirm the operations in the Terraform plan.
3. If the resources are created, the "Apply complete!" message is returned. If the resources
fail to be created, check the error message and modify the terraform.tf file.

**View results**

Run the `terraform show` command to view the created resources.

**Use Terraform to destroy resources**

If you need to release resources, run the terraform destroy command to destroy the created resources. For more information, see Use Terraform to destroy resources.

**FAQ**

> **Important:** If the "用户无资源授权，或者该API不支持RAM"(The RAM user is not granted permissions on the resource or the API does not support the RAM user) message is returned when the terraform apply command is run, check whether the Security Token Service (STS) authentication mode is enabled for the service.
> Perform the following operations to check whether the STS authentication mode is enabled for a service:

1. Log on to the Apsara Uni-manager Management Console with a superuser account.
2. In the top navigation bar, click **Configurations**. In the left-side navigation pane, click
**Authentication Mode**.
3. If a service is checked, the authentication mode is enabled for the service.
For information about the operations that you can perform after the STS authentication mode is enabled, see Use STS to call AlibabacloudStack Provider.
