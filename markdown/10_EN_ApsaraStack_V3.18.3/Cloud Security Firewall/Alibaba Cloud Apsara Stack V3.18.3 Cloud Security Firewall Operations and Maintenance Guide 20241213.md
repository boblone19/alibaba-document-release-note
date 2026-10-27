---
title: "Alibaba Cloud Apsara Stack V3.18.3 Cloud Security Firewall Operations and Maintenance Guide 20241213"
product_version: "V3.18.3"
doc_version: "20241213"
pdf_pages: 8
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 Cloud Security Firewall Operations and Maintenance Guide 20241213.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/%E4%BA%91%E7%9B%BE%E4%BA%91%E9%98%B2%E7%81%AB%E5%A2%99/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20Cloud%20Security%20Firewall%20Operations%20and%20Maintenance%20Guide%2020241213.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.3 Cloud Security Firewall Operations and Maintenance Guide 20241213

## Table of Contents

- 1 Log on to the Apsara Infrastructure Management console
- 2 Check the service status

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

## 2 Check the service status

To check the running status of the Cloud Firewall server, follow the following steps:

**Procedure**

1. Run the **ssh server IP address** command to log on to the server that hosts Cloud Firewall.
2. Run the following command to find the image ID of the Cloud Firewall server:

| sudo docker ps \| grep |   |
|---|---|

The following message is displayed:

```
af8a1a182a17 reg.docker.aliyun-inc.com/yundunadvance/cloudfirewall:696dcf568512deceb7199dc4c9aa70855e66aca71244296cf13bfaf4a0897ebe "/bin/bash /home/admi" 23 hours ago Up 23 hours yunduncloudfirewall.CloudFirewallApp__.cloudfirewall-app. 1523453835
```

3. Run the following command to go to the Docker container:

```bash
 docker exec –it [imageId] /bin/bash
```

4. Run the following command to check whether the Java process is normal:

|   | ps aux \|grep |   |
|---|---|---|
| cloudfirewall |   |   |

The following message is displayed:

```
admin 118 0.5 28.2 6261808 2368828 ? Sl Apr11 8:06 /opt/taobao/java/bin/java -Djava.u til.logging.config.file=/home/admin/cloud-fi rewall/.default/conf/logging.properties - Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager -server -Xms4g -Xmx4 g -XX:PermSize=96m -XX:MaxPermSize=384m -Xmn2g -XX:+UseConcMarkSweepGC -XX:+UseCMSCom pactAtFullCollection -XX:CMSMaxAbortablePrecleanTime=5000 - XX:+CMSClassUnloadingEnabled -XX:+UseCMSInitiatingOccupancyOnly - XX:CMSInitiatingOccupancyFraction=80 -XX:+HeapDumpOnOutOfMemoryError - XX:HeapDumpPath=/home/admin/logs/java.hprof -verbose:gc - Xloggc:/home/admin/logs/gc.log -XX:+PrintGCDetails -XX:+PrintGCDateStamps -Djava.awt. headless=true -Dsun.net.client.defaultConnectTimeout=10000 - Dsun.net.client.defaultReadTimeout=30000 -XX:+DisableExplicitGC -Dfile.encoding=UTF-8 -Ddruid.filters=mergeStat -Ddruid.useGloalDataSourceStat=true -Dproject.name=cloud-fi rewall -Dhsf.server.port=21015 -Djdk.tls.ephemeralDHKeySize=2048 - Dcatalina.vendor=alibaba -Djava.security.egd=file:/dev/./urandom - Dlog4j.defaultInitOverride=true - Dorg.apache.tomcat.util.http.ServerCookie.ALLOW_EQUALS_IN_VALUE=true - Dorg.apache.tomcat.util.http.ServerCookie.ALLOW_HTTP_SEPARATORS_IN_V0=true -Dcatalina .logs=/home/admin/cloud-firewall/.default/logs -Dignore.endorsed.dirs= -classpath /op t/taobao/tomcat/bin/bootstrap.jar:/opt/taobao/tomcat/bin/tomcat-juli.jar -Dcatalina.b ase=/home/admin/cloud-firewall/.default -Dcatalina.home=/opt/taobao/tomcat -Djava.io. tmpdir=/home/admin/cloud-firewall/.default/temp org.apache.catalina.startup.Bootstrap -Djboss.server.home.dir=/home/admin/cloud-firewall/.default - Djboss.server.home.url=file:/home/admin/cloud-firewall/.default startroot 4931 0.0 0. 0 61208 764 ? S+ 21:32 0:00 grep cloud-firewall
```

5. Run the following command to perform the health check:

|   | curl |   |
|---|---|---|
| 127.0.0.1:2015/cloud-firewall/check health _ |   |   |

If OK is returned, the service is normal.
6. View related logs.
View the routine printing logs of the Cloud Firewall server in /home/admin/cloudfirewall/logs/cloud-firewall-info.log. View the error printing logs of the Cloud Firewall server in /home/admin/cloudfirewall/logs/cloud-firewall-error.log. View the logs returned after Cloud Firewall calls OpenAPI in /home/admin/cloudfirewall/logs/cloud-firewall-openApi.log.
