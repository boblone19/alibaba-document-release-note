---
title: "Server Guard Advanced Edition Operations and Maintenance Guide"
product_version: "V3.18.6"
doc_version: "20260701"
pdf_pages: 12
source_pdf: "Alibaba Cloud Apsara Stack V3.18.6 Server Guard Advanced Edition Operations and Maintenance Guide 20260701.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E4%BA%91%E7%9B%BE-%E5%AE%89%E9%AA%91%E5%A3%AB%E9%AB%98%E7%BA%A7%E7%89%88/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Server%20Guard%20Advanced%20Edition%20Operations%20and%20Maintenance%20Guide%2020260701.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Server Guard Advanced Edition Operations and Maintenance Guide

## Check the service status

### Log on to the Apsara

**Infrastructure Management**

**console**

This topic describes how to log on to the Apsara Infrastructure Management console.

**Prerequisites**

The endpoint of the Apsara Uni-manager Operations Console and the username and password that are used to log in to the console are obtained from a deployment engineer or an administrator. The endpoint of the Apsara Uni-manager Operations Console is in the following format: regi on-id.ops.console.intranet-domain-id. A supported browser is used. We recommend that you use Google Chrome.
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
5. In the top navigation bar of the Apsara Uni-manager Operations Console, choose **Products**
**> Platforms > Apsara Infrastructure Management Framework**.

### Check the agent status

Check the Server Guard agent based on the information provided in this topic and and make sure that the agent is running as normal.

**Check the agent logs**

Agent logs are stored in the data directory of the directory in which the process file of the Server Guard agent is stored. Example: /usr/local/aegis/aegis_client/aegis_xx_xx/data. The log files are named by date. Example: data.1-data.7

**Check the status of the agent**

Run the following command to check whether the agent is online:

```
 ps -aux | grep AliYunDun
```

**Check the network connectivity**

Run the following command to check whether the agent can communicate with Server Guard over TCP:

```
 netstat -tunpe |grep AliYunDun
```

**Check the UUID of the agent**

Open the data.x log file of the agent and check the string that follows `Currentuid Ret` . The string is the UUID of the agent.

**Check the processes of the agent**

| AliYunDunUpdate |   |   |
|---|---|---|
| ng, the | AliHips |   |

The `AliYunDun` and `AliYunDunUpdate` processes of the agent are running. If you enable If both the AliYunDun and AliYunDunUpdate processes are running as normal, the agent is working as expected.

**Note**

If the agent runs in a Windows operating system, the `AliYunDun` and

|   | AliYunDunUpdate |   |
|---|---|---|
| Service |   |   |

| Alibaba Security Aegis Detect |   |
|---|---|

`AliYunDunUpdate` processes run as services named `Alibaba Security Aegis Detect`

```
Service and Alibaba Security Aegis Detect Service .
```

### Check the status of Aegiserver

**Background information**

To check the running status of Aegiserver, follow the following steps:
1. Run the `ssh server IP address` command to log on to the server of Aegiserver.
2. Run the following command to find the Aegiserver image ID:

```bash
 docker ps -a |grep aegiserver
```

The following message is displayed:

```
b9e59994df41 reg.docker.alibabainc.com/aqs/aegiserverlite@sha256:f9d292f54c58646b672a8533a0d78fba534d26d376a194034e884 70d9aa0b3 "/bin/bash /startApp." 2 hours ago Up 2 hours 80/tcp, 7001/tcp, 8005/tcp, 8 009/tcp yundun-aegis.Aegiserverlite__.aegiserverlite. 1484712802
```

3. Run the following command to go to the Docker container:

```bash
 docker exec -it [imageId] /bin/bash
```

4. Run the following command to check whether the Java process is normal:

```
 ps aux |grep aegiserver
```

The following message is displayed:

```
root 153 0.6 25.8 2983812 1084588 ? Sl 12:13 1:01 /opt/taobao/java/bin/java -Djava.ut il.logging.config.file=/home/admin/aegiserverlite/.default/conf/logging.properties -D java.util.logging.manager=org.apache.juli.ClassLoaderLogManager -server -Xms2g -Xmx2g -XX:PermSize=96m -XX:MaxPermSize=384m -Xmn1g -XX:+UseConcMarkSweepGC - XX:+UseCMSCompactAtFullCollection -XX:CMSMaxAbortablePrecleanTime=5000 -XX:+CMSClassU nloadingEnabled -XX:+UseCMSInitiatingOccupancyOnly - XX:CMSInitiatingOccupancyFraction=80 -XX:+HeapDumpOnOutOfMemoryError - XX:HeapDumpPath=/home/admin/logs/java.hprof -verbose:gc - Xloggc:/home/admin/logs/gc.log -XX:+PrintGCDetails -XX:+PrintGCDateStamps -Djava.awt. headless=true -Dsun.net.client.defaultConnectTimeout=10000 - Dsun.net.client.defaultReadTimeout=30000 -XX:+DisableExplicitGC -Dfile.encoding=UTF-8 -Ddruid.filters=mergeStat -Ddruid.useGloalDataSourceStat=true - Dproject.name=aegiserverlite -Dcatalina.vendor=alibaba - Djava.security.egd=file:/dev/./urandom -Dlog4j.defaultInitOverride=true -Dorg.apache. tomcat.util.http.ServerCookie.ALLOW_EQUALS_IN_VALUE=true - Dorg.apache.tomcat.util.http.ServerCookie.ALLOW_HTTP_SEPARATORS_IN_V0=true -Djava.end orsed.dirs=/opt/taobao/tomcat/endorsed -classpath /opt/taobao/tomcat/bin/bootstrap.jar:/opt/taobao/tomcat/bin/tomcat-juli.jar -Dcatalin a.logs=/home/admin/aegiserverlite/.default/logs - Dcatalina.base=/home/admin/aegiserverlite/.default -Dcatalina.home=/opt/taobao/tomcat -Djava.io.tmpdir=/home/admin/aegiserverlite/.default/temp org.apache.catalina.startup.Bootstrap - Djboss.server.home.dir=/home/admin/aegiserverlite/.default - Djboss.server.home.url=file:/home/admin/aegiserverlite/.default start
```

5. Run the following command to perform the health check:

```bash
 curl 127.0.0.1:7001/checkpreload.htm
```

If the response is "success", the service is normal.
6. View related logs.
**Protocol logs**: View logs about upstream and downstream protocol messages between
the server and client in /home/admin/aegiserver/logs/AEGIS_MESSAGE.log.
**Operation logs**: View abnormal stack information during operation in
/home/admin/aegiserver/logs/aegis-default.log.
**Offline logs**: View the logs about client disconnection caused by time-out in
/home/admin/aegiserver/logs/AEGIS_OFFLINE_MESSAGE.log.

### Check the Server Guard

**Update Service status**

**Background information**

To check the status of Server Guard Update Service, follow the following steps:
1. Run the `ssh host IP address` command to log on to the server of Aegiserver.
2. Run the following command to find the Aegiserver image ID:

```bash
 docker ps -a |grep aegiserver
```

3. Run the following command to go to the Docker container:

```bash
 docker exec -it [imageId] /bin/bash
```

4. Run the following command to check whether the Java process is normal:

```
 ps aux |grep aegisupdate
```

5. Run the following command to perform the health check:

```bash
 curl 127.0.0.1:7001/checkpreload.htm
```

If the response is "success", the service is normal.

### Check the Defender module

**status**

**Background information**

To check the status of the Defender module of Server Guard, follow these steps:
1. Run the `ssh server IP address` command to log on to the server that hosts the Defender
module of Server Guard.
2. Run the following command to find the image ID of the Defender module of Server Guard:

```bash
 docker ps -a |grep defender
```

3. Run the following command to go to the Docker container:

```bash
 docker exec -it [imageId] /bin/bash
```

4. Run the following command to check whether the Java process is normal:

```
 ps aux |grep defender
```

5. Run the following command to perform health check:

```bash
 curl 127.0.0.1:7001/checkpreload.htm
```

If the response is "success", the service is normal.

### Restart Server Guard

**Background information**

To restart Server Guard when a fault occurs, follow these steps:
1. Run the `ssh server IP address` command to log on to the server that hosts Server Guard.
2. Run the following command to find the image ID of Server Guard:

```bash
 docker ps -a |grep application name
```

3. Run the following command to go to the Docker container:

```bash
 docker exec -it [imageId] /bin/bash
```

4. Restart related services.
Restart the Server Guard client service. For a server running a Windows OS, go to the service manager, locate Server Guard Detect Service, and restart this service. For a server running a Linux OS, use either of the following methods to restart the Server Guard client service:

| Run the service aegis restart command to restart the service. Run the killall AliYunDun command as the | service aegis restart | command to restart the service. |   |
|---|---|---|---|
|   | killall |   |   |
| AliYunDun |   |   |   |
|   |   |   | command as the |

stop the current process, and then restart the /usr/local/aegis/aegis_client/aegis_xx_xx/AliYunDun process. Restart the Aegiserver service. a. Run the following command to view the Java process ID:

|   | ps aux \|grep |   |
|---|---|---|
| aegiserver |   |   |

b. Run the following command to stop the current process:

```
 kill -9 process
```

c. Run the following command to restart the process:

```python
 sudo -u admin
                                        /home/admin/aegiserever/bin/jbossctl
                                restart
```

d. Run the following command to check whether the process has been successfully restarted:

|   | curl |   |
|---|---|---|
| 127.0.0.1:7001/checkpreload.htm |   |   |

Restart Server Guard Update Service: a. Run the following command to view the Java process ID:

|   | ps aux \|grep |   |
|---|---|---|
| aegisupdate |   |   |

b. Run the following command to stop the current process:

```
 kill -9 process
```

c. Run the following command to restart the process:

```python
 sudo -u admin
                                        /home/admin/aegisupdate/bin/jbossctl
                                restart
```

d. Run the following command to check whether the process has been successfully restarted:

|   | curl |   |
|---|---|---|
| 127.0.0.1:7001/checkpreload.htm |   |   |

Restart the Defender service of Server Guard. a. Run the following command to view the Java process ID:

|   | ps aux \|grep |   |
|---|---|---|
| secure-service |   |   |

b. Run the following command to stop the current process:

```
 kill -9 process
```

c. Run the following command to restart the process:

```python
 sudo -u admin
                                        /home/admin/secure-service/bin/jbossctl
                                restart
```

d. Run the following command to check whether the process has been successfully restarted:

|   | curl |
|---|---|
| 127.0.0.1:7001/checkpreload.htm |   |
