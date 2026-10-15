---
title: "Cloud Linux 产品简介"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 36
source_pdf: "01_产品简介_product-introduction.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/alinux/zh/product-introduction.pdf"
converter: line-classifier (PyMuPDF)
---

# Cloud Linux 产品简介

统

## 什么是阿里云服务器操作系统

**概述**

阿里云服务器操作系统是一款由阿里云自主研发的Linux服务器操作系统。阿里云服务器操作系统适应虚拟化、云计算、大数据时代对操作系统性能、安全、稳定性的要求，提供全面高可用性、深度云原生支持以及丰富的国产软硬件生态。可部署在公有云、私有云和混合云等各种环境，在政府、金融、电力、通信运营商、交通、制造等行业得到广泛应用。阿里云服务器操作系统满足国产化合规要求，可以提供高等级服务和长达13年的生命周期维护，为对稳定性有较高要求的用户提供业务连续性保障。

**发展历史及应用**

阿里云服务器操作系统历经十余年发展，产品于2014年实现了对阿里云数据中心HostOS的100%覆盖， 在阿里数据中心内自用服务器操作系统场景实现CentOS全面替代，于2022年底在阿里云ECS云服务器 GuestOS装机量上超越CentOS，成为云上装机量占比第一的服务器操作系统。 产品支撑阿里云达到全球第三、亚太第一的市场规模，并依托云计算产业发展得到广泛应用，在全球范围内累计服务超过数十万用户，部署规模累计超过百万台物理机和千万台虚拟机，位居国内操作系统领域第一梯队。 产品通过阿里云深度服务关键信息基础设施行业IT建设和数字化创新，支撑国家部委多个云平台、覆盖全国30个省市区、数百个城市的政务云平台和大数据项目，在政务、金融、电信、能源、交通、医疗、教育、零售、互联网等行业广泛应用。

**生命周期**

阿里云服务器操作系统 V3 和 V4 在其生命周期内提供了以下三个阶段的支持：

| 阶段 | 生命周期 |  | 说明 |
|---|---|---|---|
|  | V3 | V4 |  |
| 开发支持阶段 | 2021-04～2026- 03 | 2025.07～ 2030.06 | 该阶段接受新硬件的支持、重大新特性的实现及特性增强的需求，同时提供缺陷修复和安全漏洞修复等相关支持。 |
| 维护支持阶段 | 2026-04～2031- 03 | 2030.07～ 2035.06 | 该阶段不再接受新的硬件支持需求、重大特性支持或特性增强请求。仅提供缺陷修复及安全漏洞修复等相关支持。 |
| 扩展支持阶段 | 2031-04～2034- 03 | 2035.07～ 2038.06 | 该阶段提供阿里云评估后认可的高优先级缺陷修复和高危、超危安全漏洞修复支持。 |

## 产品优势

基于十余年来阿里集团使用实践验证，阿里云服务器操作系统兼容软硬软件生态，具备良好的国产适配、技术生态繁荣以及更优的AI支持等优势。

**千锤百炼**

阿里集团14年技术积淀，历经多条线“安全+性能”验证。阿里云服务器操作系统自诞生之日起就针对云计算、大数据的场景不断试错、不断打磨、不断精进，历经十余年不断迭代后，为促进自主原生技术路线和生态发展于2020年以龙蜥开源社区的方式对外开放。时至今日龙蜥体系的OS已经是云上装机量最大的服务器操作系统，也是针对不同的芯片服务器平均性能最优的操作系统。

**生态兼容**

阿里云服务器操作系统依托于云上丰富的生产实践，在服务器操作系统领域构建强大的生态。除兼容开源软件生态之外，在数据库、中间件、大数据、云原生、人工智能等领域，阿里云也积累了许多先进的产品和开源项目。在CentOS停服的背景下，阿里云服务器操作系统兼容支持国产硬件（国产CPU、网卡、RAID卡、 AI加速卡等）和国产软件（数据库、中间件等），在严格遵循POSIX标准协议，为不同平台的软硬件生态提供兼容一致的开发和运行接口，全面实现对CentOS等技术体系的整体国产化替代。阿里云服务器操作系统通过产品顶层设计，保障内核KAPI/KABI、核心组件API/ABI高度兼容，为用户的应用稳定开发及生态长续发展提供制度保障。除此以外，阿里云服务器操作系统 V3提供额外的企业级特性和云原生支持，如 Dragonwell 云原生 Java 运行时，这使得阿里云服务器操作系统 V3成为一个既适合传统企业环境也适应云原生和多架构计算场景的选择。

**深度国产化**

充分兼容适配国产化软硬件，持续构建完善的国产化生态体系。随着国产化产业蓬勃发展，兼容国产化软硬件成为阿里云服务器操作系统最重要的设计目标之一。一直以来，阿里云服务器操作系统积极适配国产芯片的，全面支持倚天、飞腾、鲲鹏、海光、兆芯、申威等国产芯片，并围绕芯片构建了数据库、大数据等业内完整的应用生态。在国产化领域不仅通过了安全评测的认证，还跟主流的国产化软硬件进行了相互的兼容性认证和定制优化。

**自主可控**

坚持开源与自研相结合，确保阿里云服务器操作系统的技术可控与自主演进。基于“分层分类”来指导软件包的自主选型，建设开源软件供应链安全体系；通过系统安全能力和质量保障体系来“用好开源，确保广泛开源技术可控”；在内核通用功能、编译器与编程语言等领域“做深开源，实现重要开源技术可定制”；在内核竞争力特性、云计算容器基础模块、大规模系统运维、智能性能调优等领域实现“自研创新，关键核心技术自研替代”。

**面向未来**

从面向 AI 软件栈优化设计、 AI 技术辅助用户使用操作系统、拥抱开放的 AI 生态更好地服务用户。阿里云服务器操作系统面向 AI 软件栈优化设计，更好地让 AI 运行在操作系统平台上，为 AI 软件栈做更多的优化、协同，从而让 AI 负载跑得更好，与操作系统形成协同优化效应。AI 技术辅助用户使用，阿里云服务器操作系统利用 AI 在操控领域的智能调优，或运维操作的自主决策等，给操作系统用户提供更好的体验。拥抱开放的 AI 生态，阿里云践行人工智能开源开放发展策略，积极与huggingface、modelscope等大模型开放社区合作，在操作系统层面解决 AI 镜像服务的安全性问题和兼容性问题。

## 产品架构

阿里云服务器操作系统V3向下承接硬件的适配支持，向上支撑应用层的软件部署及开发，主要由内核软件 kernel和核外软件集合baseOS组成，通过体系化顶层架构设计为用户带来易用、好用的操作体验。 内核层采用了经典的UNIX内核架构，按照经典操作系统模块分类，包括了内存、调度、存储、网络、体系结构和驱动等子系统。同时，阿里云服务器操作系统内核通过实现开源内核所不具备的从计算资源、存储资源、网络资源等全链路的隔离及自适应调度能力，最大限度的提高了整机资源利用率。最后，阿里云服务器操作系统内核全面支持诸如X86_64、AArch64等多芯片架构，自研芯片和硬件的使能，通过软硬协同优化，帮助用户屏蔽硬件层的差异，提供统一的内核接口。 baseOS层提供了服务器操作系统通用功能。阿里云服务器操作系统 V3 针对阿里云基础设施进行深度优化，并在云原生、大数据、人工智能等丰富场景的需求驱动下，不断打磨和积累核心研发能力，在云计算容器、编译器编程语言、基础库、基础服务、基础工具、性能调优、运维及系统安全等重点领域进行开源修改定制和深度自研，在保障兼容性的同时，为用户提供了丰富的系统基础服务能力及调用接口。在此基础之上，实现了阿里云服务器操作系统对上层数据库、中间件、云原生应用等应用软件地充分适配与支持。 技术架构图如下：

## 功能特性

阿里云服务器操作系统是阿里云研发的稳定、安全、高性能的服务器操作系统，可以为用户应用部署在Web 服务、云原生应用、大数据、数据库、AI等场景中提供系统软件维护、安全加固、性能优化、多架构支持、 内核热补丁等操作系统服务。 操作系统是一种由多个子系统组成的复杂系统，由数千软件包构成，是一个典型的System of Systems。 阿里云服务器操作系统的设计主要考虑子系统和系统模块的合理划分。作为与业界主流Linux操作系统标准对齐的操作系统发行版，在功能设计上首先要遵循业界规范，提供通用操作系统功能，特别是在CentOS停服的背景下，要打造与传统CentOS的在功能层兼容的系统，以保障业务的平滑迁移，通用功能点详细说明见下表：

| 功能点 | 详细说明 |
|---|---|
| 内核管理和优化 | 提供强大的内核管理和优化功能，支持多种硬件架构和处理器类型，并提供各种内核参数和调整选项，以优化系统性能和稳定性。 |
| 文件系统管理和维护 | 支持多种文件系统，包括Ext4、XFS等，提供强大的文件系统管理和维护工具，如fdisk、mkfs、fsck等，以管理磁盘分区、格式化文件系统和修复文件系统错误。 |
| 网络配置和管理 | 提供灵活的网络配置和管理功能，支持多种网络协议和服务，如TCP/IP、 DNS、DHCP、NTP、FTP等，以实现网络连接、通信和共享。 |
| 安全性和身份验证 | 提供高级的安全性和身份验证功能，包括访问控制、身份认证、加密通信、密钥管理、SELinux安全模块等，以保护系统和数据的安全性和完整性。 |
| 软件包管理和更新 | 提供强大的软件包管理和更新功能，支持RPM，YUM软件包管理工具，可以方便地安装、升级和卸载软件包，并提供自动更新和依赖性解决功能，以保证系统的稳定性和安全性。 |
| 应用程序支持和管理 | 提供广泛的应用程序支持和管理功能，包括Web服务器、数据库、虚拟化、云计算、容器化、DevOps等，以满足企业级应用程序的需求和要求。 |
| IPv4/IPv6 双栈支持 | 全面支持 IPv4/IPv6 双栈网络模式。 |

除此之外，阿里云结合云业务需求场景，重点关注未来技术演进趋势，并在特定领域重点布局，持续增加改进功能，完善以下产品特性，详细说明见下表：

| 产品特性 | 详细说明 |
|---|---|
| 硬件故障屏蔽 | 作为阿里云基础设施的HOST OS，改进mcelog或引入增强的rasdaemon降低硬件故障对GuestOS的影响。 |
| 一云多芯支持 | 作为阿里云基础设施的HOST OS，承载一云多芯的需求，支持x86之外的如 AArch64等架构。 |

| 硬件外设适配 | 作为阿里云基础设施的HOST OS，满足各式各样的硬件设备接入需求，提供完善的，兼容的接口以及接入手册确保OOT扩展以及OS版本迭代对外设模块的兼容性。 |
|---|---|
| 软硬协同优化 | 支持ToC业务对提供网络资源利用率的需求，以及帮助业务释放神龙架构eRDMA 的大规模加速能力，需要持续增强阿里云服务器操作系统高性能内核网络协议栈 SMC的性能、稳定性和产品力。 |
| 网络性能优化 | 作为需要部署在大规模IDC的HOST OS，降低网卡等硬件故障对业务的影响，例如通过支持网络去堆叠技术提高网络连接的稳定性。 |
| 池化调度增强 | 支持业务借助统一资源池提高资源利用率的需求，例如通过增加/改进内核调度来支持在线和离线业务混合部署。 |
| 极至弹性伸缩 | 支持业务云原生架构改造的需求，完善或改进容器隔离技术，例如开发安全容器技术满足业务对隔离，资源利用和弹性扩缩的整体权衡。 |
| 系统启动加速 | 作为IaaS上面的GuestOS，改进GuestOS启动方式，满足客户对GuestOS快速启动的需求。 |
| 持续安全修复 | 作为一个应用于企业服务器场景的OS，满足业务对OS安全的严苛需求，提供完善高效的CVE漏洞修复能力。 |
| 热补丁升级 | 阿里云服务器操作系统引入内核热补丁技术，保障用户在无需重启服务器和任何业务相关的任务进程、无需用户注销登录、无需进行业务迁移的前提下，平滑且快速地为内核更新高危安全漏洞或重要错误修复的补丁。 |

## 应用场景

**云原生应用**

用户如果需要向云原生场景演进，只需要在创建ACK集群时选择默认的阿里云服务器操作系统，即可获得操作系统为ACK提供的稳定性、性能、安全增强能力。

**快速弹性场景**

用户如果要提升弹性扩容速度，可以选择阿里云服务器操作系统快速启动版镜像，该镜像与ECS深度结合优化，可以极大地减少实例创建时间从而提升弹性扩容速度。

**安全合规场景**

用户如果要满足中国信息安全测评中心的安全可靠测评要求，可以直接选择阿里云服务器操作系统V3创建实例，该操作系统已经通过中国信息安全测评中心的安全可靠测评，用户无需特殊配置，开箱即用。

## 附录

### Alibaba Cloud Linux 3软件兼容性

**列表**

本文为Alibaba Cloud Linux3操作系统的软件兼容清单，通过阿里云服务器操作系统兼容性认证测试的软件将会发布到本清单中。

| 软件类型 | 软件名称 | 软件版本 | 软件厂商 |
|---|---|---|---|
| 中间件 | 宝兰德应用服务器软件 | V9.5 | 北京宝兰德软件股份有限公司 |
| 中间件 | 东方通应用服务器软件 | V7.0 | 北京东方通科技股份有限公司 |
| 中间件 | 金蝶天燕Apusic应用服务器软件 | V9.0 | 深圳市金蝶天燕云计算股份有限公司 |
| 中间件 | 中创应用服务器软件 | V10 | 山东中创软件商用中间件股份有限公司 |
| 中间件 | Alibaba Dragonwell | 8.15.16.372 | 开源组件 |
| 中间件 | Alibaba Dragonwell | 11.0.21.18.9 | 开源组件 |
| 中间件 | Alibaba Dragonwell | 17.0.9.0.10.9 | 开源组件 |
| 中间件 | apache http server | 2.4.37 | 开源组件 |
| 中间件 | Grafana | 9.2.10 | 开源组件 |
| 中间件 | keepalived | 2.2.8 | 开源组件 |
| 中间件 | Nginx | 1.23.3 | 开源组件 |
| 中间件 | openjdk | 1.8.0.422 | 开源组件 |
| 中间件 | openjdk | 11.0.23.0.9 | 开源组件 |

| 中间件 | openjdk | 17.0.11.0.9 | 开源组件 |
|---|---|---|---|
| 中间件 | tengine | 2.4.0 | 开源组件 |
| 开发环境/框架 | qt-creator | 8.0.2 | 开源组件 |
| 开发环境/框架 | vscode | 1.68.0 | 开源组件 |
| 数据库 | 阿里云PolarDB数据库管理软件 | v2.0 | 阿里云计算有限公司 |
| 数据库 | 达梦数据库管理系统 | V7 | 武汉达梦数据库有限公司 |
| 数据库 | 南大通用安全数据库管理系统 | V8.8 | 天津南大通用数据技术股份有限公司 |
| 数据库 | GoldenDB分布式数据库 | V6 | 金篆信科有限责任公司 |
| 数据库 | MariaDB | 10.5.22 | 开源组件 |
| 数据库 | MongoDB | 3.6.8 | 开源组件 |
| 数据库 | MySQL | 8.0.36 | 开源组件 |
| 数据库 | PostgreSQL | 13.16 | 开源组件 |
| 数据库 | Redis | 6.2.7 | 开源组件 |
| 大数据平台 | 阿里云大规模计算软件 | V1.0 | 阿里云计算有限公司 |
| 容器/容器云 | 阿里云容器服务软件 | v1.0 | 阿里云计算有限公司 |
| 容器/容器云 | 灵雀云企业级全栈云原生开放平台 | V3 | 北京凌云雀科技有限公司 |
| 容器/容器云 | 谐云容器云平台 | - | 杭州谐云科技有限公司 |
| 虚拟化云平台 | 阿里云弹性计算软件 | V6 | 阿里云计算有限公司 |

| 虚拟化云平台 | 浪潮云海InCloud OS | - | 浪潮集团 |
|---|---|---|---|
| 存储软件 | 阿里云存储与CDN软件 | V1.0 | 阿里云计算有限公司 |
| 分布式存储软件 | ceph | 12.2.7 | 开源组件 |
| 分布式存储软件 | glusterfs | 6 | 开源组件 |
| 备份软件 | 爱数备份与恢复系统 | V8.0 | 上海爱数信息技术股份有限公司 |
| 备份软件 | 鼎甲数据备份与恢复系统 | V8.0 | 广州鼎甲计算机科技有限公司 |
| 备份软件 | 政务云云下备份解决方案 | - | 上海爱数信息技术股份有限公司 |
| 集群软件 | 中兴新支点高可用集群软件NewStart HA | - | 中兴新支点技术有限公司 |
| 集群软件 | CMP（云管平台） | V6.1 | 上海骞云信息科技有限公司 |
| 运维平台 | Apsara Stack运维系统 | - | 阿里云计算有限公司 |
| 运维平台 | CloudFlux云计算销售与数字化运营平台 | - | 上海驻云信息科技有限公司 |
| 网络防护 | 云盾-Web应用防火墙-企业版 | - | 阿里云计算有限公司 |
| 终端防护及杀毒 | 云盾-安骑士高级版 | - | 阿里云计算有限公司 |
| 身份认证 | 阿里云身份安全IDAAS | - | 阿里云计算有限公司 |

### Alibaba Cloud Linux 3硬件兼容性

**列表**

Alibaba Cloud Linux 3硬件兼容性列表是Alibaba Cloud Linux 3操作系统与整机、板卡外设之间兼容性认证的清单，通过Alibaba Cloud Linux 3硬件兼容性认证测试的硬件设备将会发布到这个清单上。

| 设备厂商 | 设备名 | 架构 | CPU型号 | 内核版本 |
|---|---|---|---|---|
| Dell | OptiPlex 3050 | x86 64 _ | Intel(R) Core(TM) i5-7500 CPU @ 3.40GHz | 5.10 |
| Dell | PowerEdge R730 | x86 64 _ | Intel(R) Xeon(R) CPU E5-2620 v4 @ 2.10GHz | 5.10 |
| HP | HP 268 Pro G1 MT | x86 64 _ | ZHAOXIN KaiXian KX- U6780A@2.7GHz | 5.10 |
| HP | ProLiant DL360 Gen9 | x86 64 _ | Intel(R) Xeon(R) CPU E5-2620 v4 @ 2.10GHz | 5.10 |
| HP | ProLiant DL388 Gen10 | x86 64 _ | Intel(R) Xeon(R) Silver 4210R CPU @ 2.40GHz | 5.10 |
| Inventec | K800G3-10G | x86 64 _ | Intel(R) Xeon(R) CPU E5-2680 v3 @ 2.50GHz | 5.10 |
| Supermi cro | X10DRH | x86 64 _ | Intel(R) Xeon(R) CPU E5-2678 v3 @ 2.50GHz | 5.10 |
| Supermi cro | X11DPi-N(T) | x86 64 _ | Intel(R) Xeon(R) Gold 5218 CPU @ 2.30GHz | 5.10 |
| Supermi cro | X11DPi-N(T) | x86 64 _ | Intel(R) Xeon(R) Gold 6248R CPU @ 3.00GHz | 5.10 |
| Supermi cro | X11DPi-N(T) | x86 64 _ | Intel(R) Xeon(R) Silver 4210 CPU @ 2.20GHz | 5.10 |
| 超聚变 | 1288H V6 | x86 64 _ | Intel(R) Xeon(R) Silver 4310 CPU @ 2.10GHz | 5.10 |
| 超聚变 | 2288H V5 | x86 64 _ | Intel(R) Xeon(R) Gold 5218 CPU @ 2.30GHz | 5.10 |
| 超云 | R2216 A13 | x86 64 _ | AMD EPYC 7763 64-Core Processor | 5.10 |
| 超云 | R5210 G12 | x86 64 _ | Intel(R) Xeon(R) Gold 6346 CPU @ 3.10GHz | 5.10 |

| 超云 | R5215 G12 | x86 64 _ | Intel(R) Xeon(R) Silver 4310 CPU @ 2.10GHz | 5.10 |
|---|---|---|---|---|
| 超云 | R5410 G12 | x86 64 _ | Intel(R) Xeon(R) Gold 6348 CPU @ 2.60GHz | 5.10 |
| 超云 | R7410 G11 | x86 64 _ | Intel(R) Xeon(R) Gold 5218 CPU @ 2.30GHz | 5.10 |
| 创新科 | R2020I | x86 64 _ | Montage Jintide(R) C08101 | 5.10 |
| 创新科 | R2230I | x86 64 _ | Intel(R) Xeon(R) Gold 5318Y CPU @ 2.10GHz | 5.10 |
| 创新科 | X1000-IL20810R | x86 64 _ | Intel(R) Xeon(R) E-2134 CPU @ 3.50GHz | 5.10 |
| 创新科 | X2000-IL | x86 64 _ | Montage Jintide(R) C08101 | 5.10 |
| 创新科 | X2000-IL(E5) | x86 64 _ | Intel(R) Xeon(R) CPU E5-2678 v3 @ 2.50GHz | 5.10 |
| 创新科 | X3000 | x86 64 _ | Intel(R) Xeon(R) Gold 5320 CPU @ 2.20GHz | 5.10 |
| 浪潮 | AS13000G5-CG12 | x86 64 _ | Hygon C86 7265 24-core Processor | 5.10 |
| 浪潮 | AS13000G5-CG36 | x86 64 _ | Hygon C86 7265 24-core Processor | 5.10 |
| 浪潮 | CS5260H2 | x86 64 _ | Hygon C86 5380 16-core Processor | 5.10 |
| 浪潮 | CS5260Z | x86 64 _ | ZHAOXIN KaiSheng KH- 37800D@2.7GHz | 5.10 |
| 浪潮 | CS5280H | x86 64 _ | Hygon C86 7265 24-core Processor | 5.10 |
| 浪潮 | CS5280H2 | x86 64 _ | Hygon C86 7380 32-core Processor | 5.10 |
| 浪潮 | CS5420H | x86 64 _ | Hygon C86 7185 32-core Processor | 5.10 |
| 浪潮 | NF3280-A7-A0-R0-00 | x86 64 _ | AMD EPYC 9654 96-Core Processor | 5.10 |

| 浪潮 | NF5180M5 | x86 64 _ | Intel(R) Xeon(R) Platinum 8260 CPU @ 2.40GHz | 5.10 |
|---|---|---|---|---|
| 浪潮 | NF5180M6 | x86 64 _ | Intel(R) Xeon(R) Gold 6354 CPU @ 3.00GHz | 5.10 |
| 浪潮 | NF5270M3 | x86 64 _ | Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz | 5.10 |
| 浪潮 | NF5270M6 | x86 64 _ | Intel(R) Xeon(R) Gold 5318Y CPU @ 2.10GHz | 5.10 |
| 浪潮 | NF5280A6 | x86 64 _ | AMD EPYC 7453 28-Core Processor | 5.10 |
| 浪潮 | NF5280A6 | x86 64 _ | AMD EPYC 7763 64-Core Processor | 5.10 |
| 浪潮 | NF5280M4 | x86 64 _ | Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz | 5.10 |
| 浪潮 | NF5280M5 | x86 64 _ | Intel(R) Xeon(R) Gold 6238 CPU @ 2.10GHz | 5.10 |
| 浪潮 | NF5280M5 | x86 64 _ | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz | 5.10 |
| 浪潮 | NF5280M6 | x86 64 _ | Intel(R) Xeon(R) Gold 5318Y CPU @ 2.10GHz | 5.10 |
| 浪潮 | NF5280M6 | x86 64 _ | Intel(R) Xeon(R) Gold 6330 CPU @ 2.00GHz | 5.10 |
| 浪潮 | NF5280-M7-A0-R0-00 | x86 64 _ | Intel(R) Xeon(R) Platinum 8468V | 5.10 |
| 浪潮 | NF5288M5 | x86 64 _ | Intel(R) Xeon(R) Platinum 8270 CPU @ 2.70GHz | 5.10 |
| 浪潮 | NF5468M6 | x86 64 _ | Intel(R) Xeon(R) Silver 4316 CPU @ 2.30GHz | 5.10 |
| 浪潮 | NF8260M5 | x86 64 _ | Intel(R) Xeon(R) Gold 6148 CPU @ 2.40GHz | 5.10 |

| 浪潮 | NF8260M6 | x86 64 _ | Intel(R) Xeon(R) Gold 5318H CPU @ 2.50GHz | 5.10 |
|---|---|---|---|---|
| 浪潮 | SA5112M6 | x86 64 _ | Intel(R) Xeon(R) Gold 6330N CPU @ 2.20GHz | 5.10 |
| 浪潮 | SA5212H2 | x86 64 _ | Intel(R) Xeon(R) CPU E5-2430 @ 2.20GHz | 5.10 |
| 浪潮 | SA5212M4 | x86 64 _ | Intel(R) Xeon(R) CPU E5-2680 v3 @ 2.50GHz | 5.10 |
| 浪潮 | SA5212M5 | x86 64 _ | Intel(R) Xeon(R) Silver 4208 CPU @ 2.10GHz | 5.10 |
| 浪潮 | SA5212M5 | x86 64 _ | Intel(R) Xeon(R) Silver 4210 CPU @ 2.20GHz | 5.10 |
| 浪潮 | SA5270M6 | x86 64 _ | Intel(R) Xeon(R) Gold 6338 CPU @ 2.00GHz | 5.10 |
| 浪潮 | SA8212M5 | x86 64 _ | Intel(R) Xeon(R) Platinum 8163 CPU @ 2.50GHz | 5.10 |
| 联想 | KaiTianM630Z | x86 64 _ | ZHAOXIN KaiXian KX- U6780A@2.7GHz | 5.10 |
| 联想 | Lenovo WenTian WA5480 G3 | x86 64 _ | Intel(R) Xeon(R) Platinum 8490H | 5.10 |
| 联想 | Lenovo WenTian WA5480 G3 | x86 64 _ | INTEL(R) XEON(R) PLATINUM 8592V | 5.10 |
| 联想 | Lenovo WenTian WR3220 G2 | x86 64 _ | Intel(R) Xeon(R) Platinum 8352V CPU @ 2.10GHz | 5.10 |
| 联想 | Lenovo WenTian WR3228 G2 | x86 64 _ | Intel(R) Xeon(R) Platinum 8352V CPU @ 2.10GHz | 5.10 |
| 联想 | Lenovo WenTian WR5220 G3 | x86 64 _ | Intel(R) Xeon(R) Platinum 8490H | 5.10 |
| 联想 | Lenovo WenTian WR5220 G3 | x86 64 _ | INTEL(R) XEON(R) PLATINUM 8592+ | 5.10 |

| 联想 | ThinkServer SR660 V2 | x86 64 _ | Intel(R) Xeon(R) Gold 6334 CPU @ 3.60GHz | 5.10 |
|---|---|---|---|---|
| 联想 | ThinkServer SR660 V2 | x86 64 _ | Intel(R) Xeon(R) Platinum 8380 CPU @ 2.30GHz | 5.10 |
| 联想 | ThinkSystem SR655 V3 | x86 64 _ | AMD EPYC 9354P 32-Core Processor | 5.10 |
| 联想 | ThinkSystem SR665 | x86 64 _ | AMD EPYC 7763 64-Core Processor | 5.10 |
| 联想 | ZhaoYangCF4620Z- A123 | x86 64 _ | ZHAOXIN KaiXian KX- 6640MA@2.2+GHz | 5.10 |
| 宁畅 | R620 G30 | x86 64 _ | Intel(R) Xeon(R) Gold 6230 CPU @ 2.10GHz | 5.10 |
| 宁畅 | R620 G50 | x86 64 _ | Intel(R) Xeon(R) Platinum 8460H | 5.10 |
| 曙光 | I620-G30 | x86 64 _ | Intel(R) Xeon(R) Gold 6230 CPU @ 2.10GHz | 5.10 |
| 新华三 | H3C UniServer R3950 G6 | x86 64 _ | AMD EPYC 9654 96-Core Processor | 5.10 |
| 新华三 | H3C UniServer R4300 G5 | x86 64 _ | Intel(R) Xeon(R) Gold 5318Y CPU @ 2.10GHz | 5.10 |
| 新华三 | H3C UniServer R4330 G5 | x86 64 _ | Hygon C86 7285 32-core Processor | 5.10 |
| 新华三 | H3C UniServer R4330 G5 | x86 64 _ | Hygon C86 7380 32-core Processor | 5.10 |
| 新华三 | H3C UniServer R4700 G5 | x86 64 _ | Intel(R) Xeon(R) Gold 6354 CPU @ 3.00GHz | 5.10 |
| 新华三 | H3C UniServer R4700 G6 | x86 64 _ | Intel(R) Xeon(R) Gold 5420+ | 5.10 |
| 新华三 | H3C UniServer R4900 G3 | x86 64 _ | Intel(R) Xeon(R) Gold 6230 CPU @ 2.10GHz | 5.10 |

| 新华三 | H3C UniServer R4900 G5 | x86 64 _ | Intel(R) Xeon(R) Gold 6330 CPU @ 2.00GHz | 5.10 |
|---|---|---|---|---|
| 新华三 | H3C UniServer R4900 G5 | x86 64 _ | Intel(R) Xeon(R) Silver 4310 CPU @ 2.10GHz | 5.10 |
| 新华三 | H3C UniServer R4900 G6 | x86 64 _ | Intel(R) Xeon(R) Platinum 8490H | 5.10 |
| 新华三 | H3C UniServer R4900 G6 Ultra | x86 64 _ | Intel(R) Xeon(R) Gold 5420+ | 5.10 |
| 新华三 | H3C UniServer R4930 G5 | x86 64 _ | Hygon C86 7265 24-core Processor | 5.10 |
| 新华三 | H3C UniServer R4930 G5 | x86 64 _ | Hygon C86 7285 32-core Processor | 5.10 |
| 新华三 | H3C UniServer R4930 G5 | x86 64 _ | Hygon C86 7380 32-core Processor | 5.10 |
| 新华三 | H3C UniServer R4950 G5 | x86 64 _ | AMD EPYC 7402 24-Core Processor | 5.10 |
| 新华三 | H3C UniServer R4950 G5 | x86 64 _ | AMD EPYC 7413 24-Core Processor | 5.10 |
| 新华三 | H3C UniServer R4950 G5 | x86 64 _ | AMD EPYC 7H12 64-Core Processor | 5.10 |
| 新华三 | H3C UniServer R4950 G6 | x86 64 _ | AMD EPYC 9224 24-Core Processor | 5.10 |
| 新华三 | H3C UniServer R4950 G6 | x86 64 _ | AMD EPYC 9654 96-Core Processor | 5.10 |
| 新华三 | H3C UniServer R6700 G6 | x86 64 _ | Intel(R) Xeon(R) Platinum 8468H | 5.10 |
| 新华三 | H3C UniServer R6900 G5 | x86 64 _ | Intel(R) Xeon(R) Gold 6330H CPU @ 2.00GHz | 5.10 |
| 新华三 | H3C UniServer R6900 G6 | x86 64 _ | Intel(R) Xeon(R) Platinum 8468H | 5.10 |

| 新华三 | UNIS Server R3630 G5 | x86 64 _ | Hygon C86 7285 32-core Processor | 5.10 |
|---|---|---|---|---|
| 新华三 | UNIS Server R3830 G5 | x86 64 _ | Hygon C86 7265 24-core Processor | 5.10 |
| 新华三 | UNIS Server R3830 G5 | x86 64 _ | Hygon C86 7285 32-core Processor | 5.10 |
| 新华三 | UniServer R4900 G3 | x86 64 _ | Intel(R) Xeon(R) Gold 5218R CPU @ 2.10GHz | 5.10 |
| 中科可控 | H520-C30 | x86 64 _ | Hygon C86 5185 16-core Processor | 5.10 |
| 中科可控 | H520-G30A | x86 64 _ | Hygon C86 5280 16-core Processor | 5.10 |
| 中科可控 | H620-G30 | x86 64 _ | Hygon C86 7151 16-core Processor | 5.10 |
| 中科可控 | H620-G30 | x86 64 _ | Hygon C86 7185 32-core Processor | 5.10 |
| 中科可控 | H620-G30A | x86 64 _ | Hygon C86 7280 32-core Processor | 5.10 |
| 中科可控 | N6150H0L | x86 64 _ | Hygon C86 7490 64-core Processor | 5.10 |
| 中科可控 | R6230HA | x86 64 _ | Hygon C86 7280 32-core Processor | 5.10 |
| 中科可控 | R6240H0 | x86 64 _ | Hygon C86 7375 32-core Processor | 5.10 |
| 中科可控 | R6250A0 | x86 64 _ | AMD EPYC 9654 96-Core Processor | 5.10 |
| 中科可控 | R6250H0 | x86 64 _ | Hygon C86 7490 64-core Processor | 5.10 |
| 中科可控 | R8450H0 | x86 64 _ | Hygon C86 7490 64-core Processor | 5.10 |
| 中科可控 | X7340H0 | x86 64 _ | Hygon C86 7380 32-core Processor | 5.10 |
| 中科可控 | X7850H0 | x86 64 _ | Hygon C86 7490 64-core Processor | 5.10 |
| 中兴 | R5300 G4X | x86 64 _ | Intel(R) Xeon(R) Gold 6330 CPU @ 2.00GHz | 5.10 |
| 中兴 | R5300 G5 | x86 64 _ | Intel(R) Xeon(R) Gold 6430 | 5.10 |

| 中兴 | R5300 G5 | x86 64 _ | INTEL(R) XEON(R) SILVER 4514Y | 5.10 |
|---|---|---|---|---|
| 中兴 | R5350 G5 | x86 64 _ | AMD EPYC 9554 64-Core Processor | 5.10 |
| 中兴 | R5500 G4X | x86 64 _ | Intel(R) Xeon(R) Gold 5318Y CPU @ 2.10GHz | 5.10 |
| 中兴 | R5930 G2 | x86 64 _ | Hygon C86 7285 32-core Processor | 5.10 |
| 中兴 | R8500G4X | x86 64 _ | Intel(R) Xeon(R) Gold 6328HL CPU @ 2.80GHz | 5.10 |
| 紫光恒越 | UNIS Server R3850 G6 | x86 64 _ | AMD EPYC 9654 96-Core Processor | 5.10 |
| 百信 | Hengshan 326RA | aarch64 | HUAWEI Kunpeng 920 7260 | 5.10 |
| 百信 | Hengshan TS02F-F30 | aarch64 | HUAWEI Kunpeng 920 5220 | 5.10 |
| 百信 | Hengshan TS02F-F30 | aarch64 | HUAWEI Kunpeng 920 7261K | 5.10 |
| 百信 | Hengshan TS02F-F39 | aarch64 | HUAWEI Kunpeng 920 7260 | 5.10 |
| 百信 | 百信太行220E-M | aarch64 | HUAWEI Kunpeng 920 | 5.10 |
| 宝德 | PR210K | aarch64 | HUAWEI Kunpeng 920 3210 | 5.10 |
| 宝德 | PR410K | aarch64 | Kunpeng920 5220 _ | 5.10 |
| 飞腾 | Phytium S2500 | aarch64 | Phytium S2500/64 | 5.10 |
| 华为 | HUAWEI PGU-WBY0 | aarch64 | HUAWEI Kunpeng920 3211K | 5.10 |
| 华为 | TaiShan 200 (Model 2280) | aarch64 | HUAWEI Kunpeng 920 5250 | 5.10 |
| 华为 | TaiShan 200K (Model 2280K) | aarch64 | Kunpeng 920-5233K | 5.10 |
| 华为 | TaiShan 2280 | aarch64 | Hi1616 | 5.10 |

| 华为 | TaiShan 2280 | aarch64 | Kunpeng 920-4826 | 5.10 |
|---|---|---|---|---|
| 华为 | TaiShan 2280 V2 | aarch64 | Kunpeng 920-4826 | 5.10 |
| 黄河科技 | Huanghe 2280 V2 | aarch64 | HUAWEI Kunpeng 920 5220 | 5.10 |
| 黄河科技 | Huanghe 2480 V2 | aarch64 | HUAWEI Kunpeng 920 5250 | 5.10 |
| 黄河科技 | Huanghe OceanAI 800- H | aarch64 | HUAWEI Kunpeng 920 5250 | 5.10 |
| 黄河科技 | Huanghe OceanAI 900 | aarch64 | HUAWEI Kunpeng 920 5250 | 5.10 |
| 浪潮 | CE3000F | aarch64 | FT-2000/4 | 5.10 |
| 浪潮 | NF2180M3 | aarch64 | FT-2000+/64 | 5.10 |
| 浪潮 | NF5280R6 | aarch64 | Ampere(R) Altra(R) Processor Q64-30 2.80GHz | 5.10 |
| 联想 | LXKT-FTD2000-mATX | aarch64 | D2000 | 5.10 |
| 神州数码 | KunTai R524 | aarch64 | Kunpeng920 5220 _ | 5.10 |
| 神州数码 | KunTai R722 | aarch64 | HUAWEI Kunpeng 920 5250 | 5.10 |
| 神州数码 | KunTai R822 | aarch64 | Kunpeng920 5250 _ | 5.10 |
| 新华三 | H3C UniServer R4960 G5 | aarch64 | HUAWEI Kunpeng 920 5220 | 5.10 |
| 新华三 | H3C UniServer R4970 G7 | aarch64 | S5000C-64 | 5.10 |
| 新华三 | R4960 G3 | aarch64 | HUAWEI Kunpeng 920 5250 | 5.10 |
| 长城 | DF720-EEC | aarch64 | FT2000PLUS | 5.10 |
| 长城 | GW-001M1A-FTF | aarch64 | FT-2000/4 | 5.10 |

| 长城 | 擎天DF720 | aarch64 | FT2000PLUS | 5.10 |
|---|---|---|---|---|
| 长江计算 | R220K V2 | aarch64 | HUAWEI Kunpeng 920 5220 | 5.10 |
| 长江计算 | R220K V2 | aarch64 | Kunpeng920 5250 _ | 5.10 |
| 长江计算 | R240K V2 | aarch64 | Kunpeng920 5250 _ | 5.10 |
| 长江计算 | R420K V2 | aarch64 | HUAWEI Kunpeng 920 5220 | 5.10 |
| 中兴 | R5310 G3 | aarch64 | ZXIC(R) ZhuFengXin 8166 Processor | 5.10 |
| 中兴 | R5510 G3 | aarch64 | ZXIC(R) ZhuFengXin 8166 Processor | 5.10 |
| 紫光恒越 | UNIS Server R4970 G7 | aarch64 | S5000C-64 | 5.10 |
| 龙芯中科 | Dabieshan T22C08B0 | loongarc h64 | Loongson-3C5000 | 5.10 |
| 龙芯中科 | Dabieshan T24C28B0 | loongarc h64 | Loongson-3C5000 | 5.10 |
| 龙芯中科 | LM-LS3A5000-7A1000- 1w-V01-pc A2101 _ | loongarc h64 | Loongson-3A5000HV | 5.10 |
| 龙芯中科 | LM-LS3A5000-7A1000- 1w-V01-pc A2101 _ | loongarc h64 | Loongson-3A5000LL | 5.10 |
| 龙芯中科 | LOONGSON T100 T2208A | loongarc h64 | Loongson-3C5000LL | 5.10 |
| 龙芯中科 | Loongson-3A5000-HV- 7A2000-1w-V0.1-EVB | loongarc h64 | Loongson-3A5000-HV | 5.10 |
| 龙芯中科 | Loongson-LS2C50C6 | loongarc h64 | Loongson-3C5000 | 5.10 |
| 龙芯中科 | Loongson-LS3A5000- 7A1000-1w-V0.1-CRB | loongarc h64 | Loongson-3A5000LL | 5.10 |

| 龙芯中科 | LS2C5LE 20201125- LS2C5LE-PPPN | loongarc h64 | Loongson-3C5000L | 5.10 |
|---|---|---|---|---|
| 龙芯中科 | LS2C5LE FRU Ver 0.01 | loongarc h64 | Loongson-3D5000 | 5.10 |

板卡兼容性列表：

| 类别 | 设备厂商 | 设备名 | 设备驱动 | 内核版本 |
|---|---|---|---|---|
| DPU | 益思芯 | Stargate-N1025 SmartNIC | ixgbe | 5.10 |
| DPU | 云豹智能 | ALPS V1.0 | - | 5.10 |
| FC | QLogic Corp. | ISP2532-based 8Gb Fibre Channel to PCI Express HBA (QLE2560 PCI Express to 8Gb FC Single Channel) | qla2xx x | 5.10 |
| FC | QLogic Corp. | ISP2722-based 16/32Gb Fibre Channel to PCIe Adapter | qla2xx x | 5.10 |
| FC | QLogic Corp. | ISP2722-based 16/32Gb Fibre Channel to PCIe Adapter (QLE2690 Single Port 16Gb Fibre Channel to PCIe Adapter) | qla2xx x | 5.10 |
| GPU | NVIDIA Corporation | GP100GL [Tesla P100 PCIe 16GB] | nvidia | 5.10 |
| GPU | NVIDIA Corporation | TU104GL [Tesla T4] | nvidia | 5.10 |
| GPU | 成都海光 | Z100L | hydcu | 5.10 |
| GPU | 登临科技 | Goldwasser-I | dengli n | 5.10 |
| GPU | 上海燧原科技有限公司 | I20 | enflam e | 5.10 |
| GPU | 上海燧原科技有限公司 | T20 | dtu | 5.10 |

| GPU | 天数智芯 | Iluvatar BI-V100 | iluvata r-itr | 5.10 |
|---|---|---|---|---|
| Networ k | Broadcom Inc. and subsidiaries | BCM57302 NetXtreme-C 10Gb/25Gb Ethernet Controller | bnxt e _ n | 5.10 |
| Networ k | Broadcom Inc. and subsidiaries | NetXtreme BCM5719 Gigabit Ethernet PCIe | tg3 | 5.10 |
| Networ k | Broadcom Inc. and subsidiaries | NetXtreme BCM5720 2-port Gigabit Ethernet PCIe | tg3 | 5.10 |
| Networ k | Broadcom Inc. and subsidiaries | NetXtreme II BCM57800 1/10 Gigabit Ethernet (BCM57800 10-Gigabit Ethernet) | bnx2x | 5.10 |
| Networ k | Broadcom Inc. and subsidiaries | NetXtreme II BCM57810 10 Gigabit Ethernet (FlexFabric 10Gb 2-port 534FLR-SFP+ Adapter) | bnx2x | 5.10 |
| Networ k | Intel Corporation | 82545EM Gigabit Ethernet Controller (Copper) (PRO/1000 MT Single Port Adapter) | e1000 | 5.10 |
| Networ k | Intel Corporation | 82599ES 10-Gigabit SFI/SFP+ Network Connection | ixgbe | 5.10 |
| Networ k | Intel Corporation | 82599ES 10-Gigabit SFI/SFP+ Network Connection (10G SFP+ DP EP102Fi4 Adapter) | ixgbe | 5.10 |
| Networ k | Intel Corporation | 82599ES 10-Gigabit SFI/SFP+ Network Connection (Ethernet Server Adapter X520-2) | ixgbe | 5.10 |
| Networ k | Intel Corporation | Ethernet Connection (12) I219-V | e1000 e | 5.10 |
| Networ k | Intel Corporation | Ethernet Connection (5) I219-LM | e1000 e | 5.10 |
| Networ k | Intel Corporation | Ethernet Connection X552 Backplane | ixgbe | 5.10 |

| Networ k | Intel Corporation | Ethernet Connection X722 for 10GbE SFP+ | i40e | 5.10 |
|---|---|---|---|---|
| Networ k | Intel Corporation | Ethernet Connection X722 for 1GbE | i40e | 5.10 |
| Networ k | Intel Corporation | Ethernet Controller 10-Gigabit X540-AT2 (10G base-T DP EP102Ti3A Adapter) | ixgbe | 5.10 |
| Networ k | Intel Corporation | Ethernet Controller E810-XXV for SFP | ice | 5.10 |
| Networ k | Intel Corporation | Ethernet Controller E810-XXV for SFP (Ethernet Network Adapter E810-XXV-2) | ice | 5.10 |
| Networ k | Intel Corporation | Ethernet Controller E810-XXV for SFP (Ethernet Network Adapter E810-XXVAM2) | ice | 5.10 |
| Networ k | Intel Corporation | Ethernet Controller X710 for 10GBASE-T (Ethernet Network Adapter X710-T2L for OCP 3.0) | i40e | 5.10 |
| Networ k | Intel Corporation | Ethernet Controller X710 for 10GBASE-T (Ethernet Network Adapter X710-T2L) | i40e | 5.10 |
| Networ k | Intel Corporation | Ethernet Controller X710 for 10GBASE-T (NIC- ETH565T-3S-2P) | i40e | 5.10 |
| Networ k | Intel Corporation | Ethernet Controller X710 for 10GbE SFP+ | i40e | 5.10 |
| Networ k | Intel Corporation | Ethernet Controller X710 for 10GbE SFP+ (10G SFP+ DP EP102Fi4 Adapter) | i40e | 5.10 |
| Networ k | Intel Corporation | Ethernet Controller X710 for 10GbE SFP+ (Ethernet Converged Network Adapter X710) | i40e | 5.10 |
| Networ k | Intel Corporation | Ethernet Controller X710 for 10GbE SFP+ (Ethernet Converged Network Adapter X710-2) | i40e | 5.10 |
| Networ k | Intel Corporation | Ethernet Controller X710 for 10GbE SFP+ (F102IX710) | i40e | 5.10 |
| Networ k | Intel Corporation | Ethernet Controller X710/X557-AT 10GBASE-T | i40e | 5.10 |

| Networ k | Intel Corporation | I210 Gigabit Backplane Connection | igb | 5.10 |
|---|---|---|---|---|
| Networ k | Intel Corporation | I210 Gigabit Network Connection | igb | 5.10 |
| Networ k | Intel Corporation | I350 Gigabit Network Connection (1G base-T QP EP014Ti1 Adapter) | igb | 5.10 |
| Networ k | Intel Corporation | I350 Gigabit Network Connection (360T-B) | igb | 5.10 |
| Networ k | Intel Corporation | I350 Gigabit Network Connection (Ethernet 1Gb 4- port 366FLR Adapter) | igb | 5.10 |
| Networ k | Intel Corporation | I350 Gigabit Network Connection (Ethernet Network Adapter I350-T4 for OCP NIC 3.0) | igb | 5.10 |
| Networ k | Intel Corporation | I350 Gigabit Network Connection (Ethernet Server Adapter I350-T2) | igb | 5.10 |
| Networ k | Intel Corporation | I350 Gigabit Network Connection (F014I350) | igb | 5.10 |
| Networ k | Intel Corporation | I350 Gigabit Network Connection (NIC-ETH360T-3S- 4P) | igb | 5.10 |
| Networ k | Mellanox Technologies | MT27710 Family [ConnectX-4 Lx] | mlx5 _ core | 5.10 |
| Networ k | Mellanox Technologies | MT27710 Family [ConnectX-4 Lx] (620F-B) | mlx5 _ core | 5.10 |
| Networ k | Mellanox Technologies | MT27710 Family [ConnectX-4 Lx] (ConnectX-4 Lx Stand-up dual-port 10GbE MCX4121A-XCAT) | mlx5 _ core | 5.10 |
| Networ k | Mellanox Technologies | MT27710 Family [ConnectX-4 Lx] (MCX4421A-ACQN ConnectX-4 Lx EN OCP,2x25G) | mlx5 _ core | 5.10 |
| Networ k | Mellanox Technologies | MT27710 Family [ConnectX-4 Lx] (NIC-ETH640F-3S- 2P) | mlx5 _ core | 5.10 |

| Networ k | Mellanox Technologies | MT27710 Family [ConnectX-4 Lx] (Stand-up ConnectX-4 Lx EN, 25GbE dual-port SFP28, PCIe3.0 x8, MCX4121A-ACAT) | mlx5 _ core | 5.10 |
|---|---|---|---|---|
| Networ k | Mellanox Technologies | MT27800 Family [ConnectX-5] (ConnectX?-5 EN network interface card, 10/25GbE dual-port SFP28, PCIe3.0 x8, tall bracket ; MCX512A-ACAT) | mlx5 _ core | 5.10 |
| Networ k | Mellanox Technologies | MT28908 Family [ConnectX-6] | mlx5 _ core | 5.10 |
| Networ k | Mellanox Technologies | MT2892 Family [ConnectX-6 Dx] | mlx5 _ core | 5.10 |
| Networ k | Realtek Semiconducto r Co., Ltd. | RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller | r8169 | 5.10 |
| Networ k | Realtek Semiconducto r Co., Ltd. | RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller (RTL8111/8168 PCI Express Gigabit Ethernet controller) | r8169 | 5.10 |
| Networ k | 北京网迅科技有限公司 | Ethernet Controller RP2000 for 10GbE SFP+ (Ethernet Network Adaptor RP2000 for 10GbE SFP+) | txgbe | 5.10 |
| Networ k | 北京网迅科技有限公司 | WX1860A2 Gigabit Ethernet Controller (Dual-Port Ethernet Network Adaptor SF200T (WOL, NCSI)) | ngbe | 5.10 |
| Networ k | 北京网迅科技有限公司 | WX1860A4 Gigabit Ethernet Controller (Qual-Port Ethernet Network Adaptor SF400T) | ngbe | 5.10 |
| Networ k | 北京网迅科技有限公司 | WX1860AL4 Gigabit Ethernet Controller (Qual-Port Ethernet Network Adaptor SF400HT) | ngbe | 5.10 |
| Networ k | 北京网迅科技有限公司 | WX1860-LC Gigabit Ethernet Controller | ngbe | 5.10 |
| Networ k | 成都北中网芯科技有限公司 | N5 Series 2-port 25GbE Network Adapter | ncepf | 5.10 |
| Networ k | 成都北中网芯科技有限公司 | N6S Series 2-port 100GbE Network Adapter | ncepf | 5.10 |
| Networ k | 华为 | HNS GE/10GE/25GE RDMA Network Controller | hns3 | 5.10 |

| Networ k | 华为 | HNS GE/10GE/25GE/50GE RDMA Network Controller | hns3 | 5.10 |
|---|---|---|---|---|
| Networ k | 龙芯中科 | Gigabit Ethernet Controller | stmm aceth | 5.10 |
| Networ k | 龙芯中科 | Loongson Technology LLC | stmm aceth | 5.10 |
| Networ k | 芯启源 | Network Flow Processor 3800 | nfp | 5.10 |
| Networ k | 中科驭数 | SWIFT-2200NX10 Ethernet Controller (Device 2018) | swiftn | 5.10 |
| Networ k | 中兴 | NS212 | mlx5 _ core | 5.10 |
| Networ k | 中兴 | NS312 | mlx5 _ core | 5.10 |
| NPU | 寒武纪 | MLU370-S4 | cambri con- pci- drv ml _ u370 _ pigeon | 5.10 |
| NVMe | Intel Corporation | Express Flash NVMe P4500/P4600 | nvme | 5.10 |
| NVMe | Intel Corporation | NVMe Datacenter SSD [3DNAND, Beta Rock Controller] (NVMe Datacenter SSD [3DNAND] ME 2.5" U.2 (P4610)) | nvme | 5.10 |
| NVMe | Intel Corporation | NVMe Datacenter SSD [3DNAND, Beta Rock Controller] (NVMe Datacenter SSD [3DNAND] SE 2.5" U.2 (P4500)) | nvme | 5.10 |
| NVMe | Intel Corporation | NVMe Datacenter SSD [3DNAND, Beta Rock Controller] (NVMe Datacenter SSD [3DNAND] SE 2.5" U.2 (P4510)) | nvme | 5.10 |
| NVMe | Intel Corporation | NVMe Datacenter SSD [Optane] (15mm 2.5" U.2 (P4800X)) | nvme | 5.10 |

| NVMe | Intel Corporation | NVMe DC SSD [3DNAND, Beta Rock Controller] | nvme | 5.10 |
|---|---|---|---|---|
| NVMe | Intel Corporation | NVMe DC SSD [3DNAND, Sentinel Rock Controller] | nvme | 5.10 |
| NVMe | Intel Corporation | Optane DC P4800X Series SSD (DC P4800X Series [2.5" SFF]) | nvme | 5.10 |
| NVMe | Intel Corporation | PCIe Data Center SSD (DC P3600 SSD [Add-in Card]) | nvme | 5.10 |
| NVMe | Micron Technology Inc | Micron 5300 MTFD _ _ | nvme | 5.10 |
| NVMe | Phison Electronics Corporation | E12 NVMe Controller | nvme | 5.10 |
| NVMe | Samsung Electronics Co Ltd | NVMe SSD Controller 172Xa/172Xb | nvme | 5.10 |
| NVMe | Samsung Electronics Co Ltd | NVMe SSD Controller PM9A1/PM9A3/980PRO (General DC NVMe PM9A3) | nvme | 5.10 |
| NVMe | Samsung Electronics Co Ltd | NVMe SSD Controller SM961/PM961 | nvme | 5.10 |
| NVMe | Samsung Electronics Co Ltd | NVMe SSD Controller SM981/PM981/PM983 | nvme | 5.10 |
| NVMe | SiliconGo | SGM9702C | nvme | 5.10 |
| NVMe | Western Digital | Ultrastar DC SN840 NVMe SSD | nvme | 5.10 |
| NVMe | 北京得瑞领新科技有限公司 | D7436 | nvme | 5.10 |
| NVMe | 北京忆恒创源科技股份有限公司 | MEMBLAZE P6531DT0384Y00 | nvme | 5.10 |

| NVMe | 北京忆恒创源科技股份有限公司 | MEMBLAZE P6536DT0320M00 | nvme | 5.10 |
|---|---|---|---|---|
| NVMe | 北京忆恒创源科技股份有限公司 | MEMBLAZE P6537DT0320Y00 | nvme | 5.10 |
| NVMe | 北京忆恒创源科技股份有限公司 | MEMBLAZE P7940DT1536Y00 | nvme | 5.10 |
| NVMe | 北京忆恒创源科技股份有限公司 | PBlaze5 700/900 | nvme | 5.10 |
| NVMe | 北京忆恒创源科技股份有限公司 | PBlaze5 910/916 | nvme | 5.10 |
| NVMe | 合肥大唐存储科技有限公司 | DTGC-CP 256GB | nvme | 5.10 |
| NVMe | 合肥大唐存储科技有限公司 | NVMe SSD Controller 300A | nvme | 5.10 |
| NVMe | 华为 | ES3000 V5 NVMe PCIe SSD | nvme | 5.10 |
| NVMe | 江波龙 | ORCA 4836 Series eSSD | nvme | 5.10 |
| NVMe | 深圳大普微电子股份有限公司 | J5100 | nvme | 5.10 |
| NVMe | 深圳大普微电子股份有限公司 | R5100 | nvme | 5.10 |
| NVMe | 深圳大普微电子股份有限公司 | R5101 | nvme | 5.10 |
| NVMe | 深圳大普微电子股份有限公司 | R5300 | nvme | 5.10 |
| NVMe | 深圳大普微电子股份有限公司 | R5301 | nvme | 5.10 |
| NVMe | 深圳大普微电子股份有限公司 | X2900 | nvme | 5.10 |

| NVMe | 深圳大普微电子股份有限公司 | X2900P | nvme | 5.10 |
|---|---|---|---|---|
| NVMe | 深圳忆联信息系统有限公司 | NVMe SSD Controller UHXXXa series (NVMe SSD UHXXXa series U.2 1600GB) | nvme | 5.10 |
| NVMe | 深圳忆联信息系统有限公司 | UH711a | nvme | 5.10 |
| NVMe | 深圳忆联信息系统有限公司 | UH811a | nvme | 5.10 |
| NVMe | 深圳忆联信息系统有限公司 | UH831a | nvme | 5.10 |
| SSD | 合肥大唐存储科技有限公司 | DSS200-B 960GB _ | sd | 5.10 |
| SSD | 合肥大唐存储科技有限公司 | DTGC-C 512GB _ | sd | 5.10 |
| SSD | 江波龙 | RSYE3836N-3840 | sd | 5.10 |
| Storage | Adaptec | Smart Storage PQI 12G SAS/PCIe 3 (RAID PM8204- 2GB) | smart pqi | 5.10 |
| Storage | Adaptec | Smart Storage PQI 12G SAS/PCIe 3 (Smart Array P408i-a SR Gen10) | smart pqi | 5.10 |
| Storage | Adaptec | Smart Storage PQI 12G SAS/PCIe 3 (SmartRAID 3100) | smart pqi | 5.10 |
| Storage | Adaptec | Smart Storage PQI SAS (HBA H460-B1) | smart pqi | 5.10 |
| Storage | Adaptec | Smart Storage PQI SAS (PM8222-SHBA) | smart pqi | 5.10 |
| Storage | Adaptec | Smart Storage PQI SAS (RAID PM8204-2GB) | smart pqi | 5.10 |

| Storage | Adaptec | Smart Storage PQI SAS (SmartRAID 3100) | smart pqi | 5.10 |
|---|---|---|---|---|
| Storage | ASMedia Technology Inc. | ASM1062 Serial ATA Controller | ahci | 5.10 |
| Storage | Broadcom / LSI | 53c1030 PCI-X Fusion-MPT Dual Ultra320 SCSI (LSI Logic Parallel SCSI Controller) | mptspi | 5.10 |
| Storage | Broadcom / LSI | Fusion-MPT 12GSAS/PCIe Secure SAS38xx (9500-8i Tri-Mode HBA) | mpt3s as | 5.10 |
| Storage | Broadcom / LSI | HGST HUH721212ALE600 8CKWX40E | mpt3s as | 5.10 |
| Storage | Broadcom / LSI | MegaRAID 12GSAS/PCIe Secure SAS39xx (MegaRAID 9560-16i) | megar aid sa _ s | 5.10 |
| Storage | Broadcom / LSI | MegaRAID 12GSAS/PCIe Secure SAS39xx (MegaRAID 9560-8i) | megar aid sa _ s | 5.10 |
| Storage | Broadcom / LSI | MegaRAID 12GSAS/PCIe Secure SAS39xx (ThinkSystem RAID 940-16i 4GB Flash PCIe Gen4 12Gb Adapter) | megar aid sa _ s | 5.10 |
| Storage | Broadcom / LSI | MegaRAID 12GSAS/PCIe Secure SAS39xx (ThinkSystem RAID 940-8i 4GB Flash PCIe Gen4 12Gb Adapter) | megar aid sa _ s | 5.10 |
| Storage | Broadcom / LSI | MegaRAID SAS 2208 [Thunderbolt] | megar aid sa _ s | 5.10 |
| Storage | Broadcom / LSI | MegaRAID SAS-3 3108 [Invader] (MegaRAID SAS 9361-8i) | megar aid sa _ s | 5.10 |
| Storage | Broadcom / LSI | MegaRAID SAS-3 3316 [Intruder] (MegaRAID SAS 9361-16i) | megar aid sa _ s | 5.10 |
| Storage | Broadcom / LSI | MegaRAID Tri-Mode SAS3408 (MegaRAID 9440-8i) | megar aid sa _ s | 5.10 |

| Storage | Broadcom / LSI | MegaRAID Tri-Mode SAS3416 (ThinkSystem RAID 530-16i PCIe 12Gb Adapter) | megar aid sa _ s | 5.10 |
|---|---|---|---|---|
| Storage | Broadcom / LSI | MegaRAID Tri-Mode SAS3508 (MegaRAID 9460-8i) | megar aid sa _ s | 5.10 |
| Storage | Broadcom / LSI | MegaRAID Tri-Mode SAS3516 (MegaRAID 9460-16i) | megar aid sa _ s | 5.10 |
| Storage | Broadcom / LSI | MegaRAID Tri-Mode SAS3516 (ThinkSystem RAID 930-16i 4GB Flash PCIe 12Gb Adapter) | megar aid sa _ s | 5.10 |
| Storage | Broadcom / LSI | SAS3008 PCI-Express Fusion-MPT SAS-3 (12G SAS3008IR Onboard) | mpt3s as | 5.10 |
| Storage | Broadcom / LSI | SAS3008 PCI-Express Fusion-MPT SAS-3 (AOC- S3008L-L8e) | mpt3s as | 5.10 |
| Storage | Broadcom / LSI | SAS3008 PCI-Express Fusion-MPT SAS-3 (SAS9311- 8i) | mpt3s as | 5.10 |
| Storage | Broadcom / LSI | SAS3416 Fusion-MPT Tri-Mode I/O Controller Chip (IOC) (HBA 9400-16i) | mpt3s as | 5.10 |
| Storage | Intel Corporation | 400 Series Chipset Family SATA AHCI Controller | ahci | 5.10 |
| Storage | Intel Corporation | 8 Series/C220 Series Chipset Family 6-port SATA Controller 1 [AHCI mode] | ahci | 5.10 |
| Storage | Intel Corporation | Atom Processor C3000 Series SATA Controller 1 | ahci | 5.10 |
| Storage | Intel Corporation | C600/X79 series chipset 6-Port SATA AHCI Controller | ahci | 5.10 |
| Storage | Intel Corporation | C602 chipset 4-Port SATA Storage Control Unit | isci | 5.10 |
| Storage | Intel Corporation | C610/X99 series chipset 6-Port SATA Controller [AHCI mode] | ahci | 5.10 |

| Storage | Intel Corporation | C610/X99 series chipset sSATA Controller [AHCI mode] | ahci | 5.10 |
|---|---|---|---|---|
| Storage | Intel Corporation | C620 Series Chipset Family SATA Controller [AHCI mode] | ahci | 5.10 |
| Storage | Intel Corporation | C620 Series Chipset Family SSATA Controller [AHCI mode] | ahci | 5.10 |
| Storage | Intel Corporation | Cannon Lake PCH SATA AHCI Controller | ahci | 5.10 |
| Storage | Intel Corporation | Mass storage controller AHCI 1.0 | ahci | 5.10 |
| Storage | Intel Corporation | Q170/Q150/B150/H170/H110/Z170/CM236 Chipset SATA Controller [AHCI Mode] | ahci | 5.10 |
| Storage | Intel Corporation | SATA Controller [RAID mode] | ahci | 5.10 |
| Storage | Intel Corporation | Sunrise Point-H SATA controller [AHCI mode] | ahci | 5.10 |
| Storage | Intel Corporation | Volume Management Device NVMe RAID Controller | vmd | 5.10 |
| Storage | LSI Logic / Symbios Logic | SAS2308 PCI-Express Fusion-MPT SAS-2 (SAS9217- 8i) | mpt3s as | 5.10 |
| Storage | Marvell Technology Group Ltd. | 88SE9215 PCIe 2.0 x1 4-port SATA 6 Gb/s Controller | ahci | 5.10 |
| Storage | Marvell Technology Group Ltd. | 88SE9230 PCIe 2.0 x2 4-port SATA 6 Gb/s RAID Controller | ahci | 5.10 |
| Storage | Marvell Technology Group Ltd. | 88SE9230 PCIe SATA 6Gb/s Controller | ahci | 5.10 |
| Storage | VIA Technologies, Inc. | Standard AHCI 1.0 SATA Controller | ahci | 5.10 |

| Storage | 成都海光 | FCH SATA Controller [AHCI mode] | ahci | 5.10 |
|---|---|---|---|---|
| Storage | 华为 | HiSilicon AHCI HBA | ahci | 5.10 |
| Storage | 华为 | HiSilicon SAS 3.0 HBA | hisi sa _ s v3 h _ _ w | 5.10 |
| Storage | 龙芯中科 | SATA AHCI Controller | ahci | 5.10 |
| Storage | 兆芯 | ZX-100/ZX-200/ZX-E StorX AHCI Controller | ahci | 5.10 |
| Storage | 中兴 | RM241B-18i | smart pqi | 5.10 |
| Storage | 中兴 | RM241B-18i 2G | smart pqi | 5.10 |
| Storage | 中兴 | RM242B-18i | smart pqi | 5.10 |
| Storage | 中兴 | RM242B-18i 4G | smart pqi | 5.10 |
| Storage | 中兴 | RM243B-18i | smart pqi | 5.10 |
| Storage | 中兴 | RS241-18i | smart pqi | 5.10 |
| Storage | 中兴 | RS241-18i 2G | smart pqi | 5.10 |
| Storage | 中兴 | RS242-18i | smart pqi | 5.10 |
| Storage | 中兴 | RS242-18i 4G | smart pqi | 5.10 |
| Storage | 中兴 | RS243-18i | smart pqi | 5.10 |
