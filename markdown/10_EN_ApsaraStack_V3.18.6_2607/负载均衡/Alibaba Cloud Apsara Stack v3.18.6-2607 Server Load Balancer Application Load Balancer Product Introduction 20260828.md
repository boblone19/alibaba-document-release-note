---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Server Load Balancer Application Load Balancer Product Introduction 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 20
source_pdf: "94b05615be0caae1_Alibaba Cloud Apsara Stack v3.18.6-2607 Server Load Balancer Application Load Balancer Product Intro"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Server%20Load%20Balancer%20Application%20Load%20Balancer%20Product%20Introduction%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Server Load Balancer Application Load Balancer Product Introduction 20260828

## Table of Contents

- 1 Product details
- 2 Product value
- 3 Scenarios
- 4 Features

## 1 Product details

**Overview**

Application Load Balancer (ALB) is a load balancing service from Alibaba Cloud that provides powerful application-layer processing and advanced routing features. It is designed for application-layer load balancing scenarios that use protocols such as HTTP, HTTPS, and QUIC.

| Concept | Description |
|---|---|
| Instance | An instance operates at Layer 7 and provides powerful Layer 7 load balancing. It distributes traffic across multiple backend servers to increase your application's service throughput. |
| Listener | A listener is the smallest service unit of an ALB instance. Configure a protocol and port for the listener to specify the traffic to process, such as HTTP traffic on port 80. Each ALB instance requires at least one listener to process and distribute traffic. By default, you can add up to 50 listeners to each ALB instance to handle different types of service traffic. |
| Forwarding rule | A forwarding rule determines how an ALB instance routes requests to backend servers in one or more backend server groups. ALB has advanced routing capabilities. In addition to traditional routing rules, it can forward requests based on rules such as HTTP headers, cookies, and HTTP request methods. This allows for flexible, service-based scheduling. |
| Server group | A server group is a logical group of backend servers that process requests distributed by ALB. In ALB, server groups exist independently of ALB instances. You can attach the same server group to different ALB instances. By default, you can add up to 100 backend servers to each server group. ALB server groups support various types of backend servers, such as ECS instances, ENIs, and IP addresses. |
| Health check | ALB uses health checks to determine the service availability of backend servers. ALB detects unhealthy servers in a server group and stops distributing traffic to them. ALB supports flexible health check configurations, such as protocol, port, and various health check thresholds. ALB also provides health check templates that you can quickly apply to different server groups. |

| Access control | Set an access whitelist or blacklist for a listener: Whitelist: Allows specific IP addresses to access the load balancer. Only requests from the IP addresses or address ranges set in the selected access control policy group are forwarded. A whitelist is suitable for scenarios where only specific IP addresses are allowed access. Setting a whitelist poses certain service risks. After you set a whitelist, only IP addresses in the whitelist can access the SLB listener. If you enable a whitelist but do not add any IP addresses to the policy group, the listener forwards all requests. Blacklist: Denies specific IP addresses access to the load balancer. Requests from the IP addresses or address ranges set in the selected access control policy group are not forwarded. A blacklist is suitable for scenarios where you want to restrict access from specific IP addresses. If you enable a blacklist but do not add any IP addresses to the policy group, the listener forwards all requests. |
|---|---|
| Certificate management | Manage server certificates and CA certificates: Server certificate: Proves the identity of the server. A browser uses the server certificate to check whether the certificate sent by the server is issued by a trusted authority. CA certificate: The server uses a CA certificate to authenticate the signature of a client certificate. If the authentication fails, the connection is rejected. |

## 2 Product value

Application Load Balancer (ALB) provides powerful processing capabilities and advanced routing features for application-layer protocols such as HTTP, HTTPS, and QUIC. This topic describes the benefits of ALB.

**High elasticity at the application layer**

ALB operates at the application layer. It distributes traffic to scale your applications, eliminates single points of failure, and improves system availability.

**Advanced protocol support**

ALB supports the HTTP, HTTPS, and QUIC protocols. For online applications such as ApsaraVideo Real-time Communication, interactive streaming, and games, ALB provides faster access and more secure, reliable transmission. ALB also supports the gRPC framework to enable efficient API communication among microservices.

**Advanced content-based routing**

ALB can identify specific service traffic based on conditions such as the path, HTTP header, query string, HTTP request method, cookie, and source IP address, and then forward the traffic to different backend servers. ALB also supports advanced operations such as redirection, rewrites, and custom HTTPS headers.

## 3 Scenarios

Application Load Balancer (ALB) provides powerful application-layer processing and advanced routing features. It focuses on the HTTP, HTTPS, and QUIC application-layer protocols. Common scenarios for ALB include the following:
**High elasticity at the application layer**: ALB operates at the application layer and
provides a virtual IP address (VIP) service to handle a massive volume of requests. ALB scales your applications by distributing traffic. This process eliminates single points of failure and improves application availability.
**Advanced protocol support**: ALB supports the HTTP, HTTPS, and QUIC protocols and can
process traffic at a massive scale. For mobile Internet applications, such as ApsaraVideo Real-time Communication and interactive streams, ALB provides faster access and more secure, reliable transmission. ALB also supports the gRPC framework. This enables efficient API communication between microservices.
**Advanced content-based routing**: ALB can detect specific service traffic based on
conditions such as the path, HTTP header, query string, HTTP request method, cookie, and source IP address. ALB then forwards the traffic to different backend servers. ALB also supports advanced operations such as redirection, rewrites, and custom HTTPS headers.

## 4 Features

This topic describes the features of Application Load Balancer (ALB).

**Instances**

| Feature |   | Description |
|---|---|---|
| Instance network type | Private network | Supports private ALB instances, which have only private IP addresses. |
|   | Public network | Supports public ALB instances, which have both public and private IP addresses. |
|   | Switch between public and private network types | Supports switching between IPv4/IPv6 public and private network types. |
| IP mode | Static IP | Supports the static IP mode. |
| Protocol version | IPv4 | Supports IPv4 instances. |
|   | Dual-stack | Supports IPv4/IPv6 dual-stack instances. |
| Instance name | Specify an instance name | Supports specifying an instance name. |
|   | Modify an instance name | Supports modifying an instance name. |
| Tags | Edit instance tags | Supports adding, modifying, and deleting instance tags. |
|   | Filter instances by tag | Supports filtering instances by tag. |
| Deletion protection | Enable/Disable deletion protection | Supports enabling and disabling deletion protection. |
| Configuration read-only mode | Enable/Disable configuration read-only mode | Supports enabling and disabling the configuration read- only mode. |

**Listeners**

| Feature | Description |
|---|---|

| Listener protocol | Supported protocols | ALB supports the HTTP protocol. |
|---|---|---|
|   |   | ALB supports the HTTPS protocol. |
|   | Advanced application layer protocols | ALB supports the QUIC protocol. |
| Common features | Configure a frontend port | You can configure a frontend port. |
|   | Set a listener name | You can set a listener name. |
|   | Modify a listener name | You can modify a listener name. |
|   | Select a server group | You can select a server group. |
|   | Replace a server group | You can replace a server group. |
|   | Set an idle timeout period | You can set an idle timeout period for connections. |
|   | Set a request timeout period | You can set a request timeout period for connections. |
|   | Enable data compression | You can enable data compression for specific file types. |
|   | Obtain the client source IP address | Retrieves the client IP address from the X-Forwarded- For header field. |
| HTTP listener | Additional HTTP header fields | Adds the SLB-ID header field to retrieve the ID of the SLB instance. |
|   |   | Adds the X-Forwarded-Proto header field to retrieve the listener protocol of the instance. |
|   | Additional HTTP header fields for advanced forwarding | Adds the X-Forwarded-Port header field to retrieve the listener port of the instance. |
|   |   | Adds the X-Forwarded-Client-srcport header field to retrieve the port of the client that accesses the SLB instance. |

| HTTPS listener | Enable HTTP/2 | You can enable HTTP/2. |
|---|---|---|
|   | Additional HTTP header fields | Adds the SLB-ID header field to retrieve the ID of the SLB instance. |
|   |   | Adds the X-Forwarded-Proto header field to retrieve the listener protocol of the instance. |
|   | Additional HTTP header fields for advanced forwarding | Adds the X-Forwarded-Clientcert-subjectdn header field to retrieve the owner information of the client certificate. |
|   |   | Adds the X-Forwarded-Clientcert-issuerdn header field to retrieve the issuer information of the client certificate. |
|   |   | Adds the X-Forwarded-Clientcert-fingerprint header field to retrieve the fingerprint of the client certificate. |
|   |   | Adds the X-Forwarded-Clientcert-clientverify header field to retrieve the verification result of the client certificate. |
|   |   | Adds the X-Forwarded-Port header field to retrieve the listener port of the SLB instance. |
|   |   | Adds the X-Forwarded-Client-srcport header field to retrieve the port of the client that accesses the SLB instance. |
|   | Enable QUIC upgrade (Advanced) | You can enable QUIC upgrade. If you enable this feature, you must select a created QUIC listener from the associated QUIC listener drop-down list. |
|   | Configure SSL certificates | You can configure server certificates. |
|   |   | You can configure CA certificates to enable mutual authentication. |
|   | Select a TLS security policy | You can select a TLS security policy. |
|   | Additional HTTP header fields | Adds the SLB-ID header field to retrieve the ID of the SLB instance. |
|   | ion: 20260828 |   |

| pplication Load B Introduction·Fea | alancer Produc tures | Server Load Balance |
|---|---|---|
| QUIC listener |   |   |
|   |   | Adds the X-Forwarded-Proto header field to retrieve the listener protocol of the instance. |
|   | Additional HTTP header fields for advanced forwarding | Adds the X-Forwarded-Port header field to retrieve the listener port of the instance. |
|   | Configure SSL certificates | You can configure server certificates. |
| Listener status | Start and stop a listener | You can start and stop a listener. |
| Forwarding rules | Set a forwarding rule name | You can set a name for a forwarding rule. |
|   | Configure request forwarding rules | You can configure forwarding conditions based on the domain name or path. Matching methods: Domain name: exact match, wildcard character, and case-insensitive regular expression. Path: exact match, wildcard character, case- insensitive regular expression, and case-sensitive regular expression. |
|   |   | You can configure the forwarding action to forward requests to one or more server groups. Session persistence between server groups is supported. |
|   | Configure advanced request forwarding rules | You can configure advanced forwarding conditions based on the HTTP header, query string, HTTP request method, cookie, or source IP address. Matching methods: HTTP header, query string, and cookie: exact match and wildcard character. Source IP address: CIDR block. |

|   |   | Supported forwarding actions include Redirect, Return Fixed Response, Rewrite, Insert Header, Remove Header, Rate Limit, Traffic Mirror, and Cross- Origin Resource Sharing (CORS). Details: Return Fixed Response: You can set the response status code, response body type, and response body. Redirect: You can set the protocol, domain name, port, path, query, and status code (301 to 308). Insert Header: You can set the header key and value. The value can be user-defined, a reference to a field in the request header, or system-defined. Rewrite: You can rewrite the domain name, path, and query. Rate Limit: You can set the total rate limit and the rate limit based on the client source IP address. Cross-Origin Resource Sharing (CORS): You can set the allowed origins, allowed methods, allowed request headers, allowed response headers, whether to allow credentials, and the browser cache time. |
|---|---|---|
|   | Configure advanced response forwarding rules | Forwarding conditions: request direction (optional), status code, and header. |
|   |   | Forwarding actions: Return Fixed Response, Insert Header, and Remove Header. |
|   | Edit a forwarding rule | You can edit forwarding rules. |
|   | Reorder forwarding rules | You can reorder forwarding rules. |
|   | Delete a forwarding rule | You can delete forwarding rules. |
| WebSocket | WebSocket | HTTP listeners support WebSocket by default. |
|   | WebSocket Secure | HTTPS listeners support WebSocket Secure by default. |

**Server groups**

| Feature |   | Description |
|---|---|---|
| Server group type | Server type | Supports adding ECS instances as backend servers. |
|   | IP type | Supports adding IP addresses as backend servers. |

| Server group name | Set a server group name | Supports setting a server group name. |
|---|---|---|
| Backend protocol | HTTP | Supports HTTP as the backend protocol. |
|   | HTTPS - Advanced security | Supports HTTPS as the backend protocol. |
|   | gRPC - Advanced application layer | Supports gRPC as the backend protocol. |
| Scheduling algorithm | Weighted round-robin | Distributes requests to servers based on their weights in a round-robin manner. |
|   | Weighted least connections | If weights are the same, backend servers with fewer connections have a higher probability of being selected. |
|   | Consistent hashing | Supports source IP hashing. |
|   |   | Supports URL parameter hashing. |
| IPv6 attachment | Enable IPv6 attachment - Advanced IPv6 | Enable IPv6 attachment: The server group supports attaching IPv4 and IPv6 backend servers. The server group type can only be Server type. |
|   |   | Do not enable IPv6 attachment: The server group supports attaching only IPv4 backend servers. The server group type can be Server type, IP type, or Function Compute type. |
| Session persistence | Enable session persistence | Supports inserting a cookie to implement session persistence. |
|   |   | Supports rewriting a cookie to implement session persistence. |
|   | Configure a session persistence timeout period | Supports configuring a session persistence timeout period. |
| Persistent backend connection | Enable persistent backend connection - Advanced application layer | After you enable persistent backend connections, ALB maintains a number of persistent TCP connections to backend servers. When a new request arrives, ALB preferentially uses an idle persistent TCP connection to forward the request. |

| Slow start | Enable slow start - Advanced application layer | After you enable slow start, ALB gradually increases the number of requests sent to a newly added backend server in the server group. |
|---|---|---|
| Connection draining | Enable connection draining - Advanced application layer | Supports enabling connection draining. |
| Tags | Edit server group tags | Supports editing server group tags. |
|   | Filter server groups by tag | Supports filtering server groups by tag. |
| Health check | Enable and disable health checks | Supports enabling and disabling health checks. |
|   | Select and load a health check configuration | Supports creating health check configurations separately and attaching them to server groups. |
| Backend server | Add a backend server | Based on the server group type, supports adding backend servers of the Server type or IP type. |
|   | Remove a backend server | Supports removing backend servers. |
| Save configuration | Save a server group configuration | Supports saving a server group configuration for reuse. |

**Security management**

| Feature |   | Description |
|---|---|---|
| Access control | Set a policy group name | Supports setting a policy group name. |
|   | Tag | Supports tags. |
|   | Set an access control method | Supports whitelists. |
|   |   | Supports blacklists. |
| > Document Ve | rsion: 20260828 1 |   |

|   | Edit IP entries | Supports adding, modifying, and deleting IP entries (CIDR blocks). |
|---|---|---|

| Feature |   | Description |
|---|---|---|
| Health check | Select a health check protocol | HTTP: Supports the HEAD and GET methods. |
|   |   | HTTPS: Supports the HEAD and GET methods. |
|   |   | TCP: Checks whether the server port is active by sending SYN handshake messages. |
|   | Advanced application layer health check protocols | gRPC: Sends POST or GET requests. |
|   | Select a health check method | For HTTP and HTTPS health checks, the HEAD method is used by default. |
|   |   | HTTP and HTTPS support GET requests. |
|   | Advanced application layer health check methods | gRPC supports the POST method by default. |
|   |   | For gRPC health checks, the GET method is also supported. |
|   | Advanced application layer health check protocol versions | HTTP/1.1 is supported. |
|   | Set a health check port | You can set a health check port. By default, the backend service port is used. |
|   | Set a health check path | You can set a health check path. |
|   | Set a health check domain name | You can use the private IP address of the backend server. This is the default setting. |
|   |   | You can specify a domain name. |

|   | Set health status return codes | For HTTP/HTTPS health checks, you can select http 2xx, _ http 3xx, http 4xx, and http 5xx. By default, http 2xx _ _ _ _ and http 3xx are selected. _ For gRPC health checks, you can select values from 0 to 99. You can specify up to 20 ranges. |
|---|---|---|
|   | Set a response timeout period | The amount of time to wait for a response to a health check probe. |
|   | Set a health check interval | You can set the interval between health checks. |
|   | You can set the Healthy Threshold. | The number of consecutive successful health checks required for a backend server to be declared healthy. |
|   | Set an unhealthy threshold | The number of consecutive failed health checks required for a backend server to be declared unhealthy. |

| Feature |   | Description |
|---|---|---|
| Certificate management | Server certificate | Supports adding additional server certificates. |
|   |   | Supports deleting additional server certificates. |
|   | CA certificate | Supports enabling or disabling mutual authentication. |
|   |   | Supports replacing a CA certificate. |

| Feature |   | Description |
|---|---|---|
| TLS security policy | Select a default policy | Supports the tls cipher policy 1 0 policy. _ _ _ _ |
|   |   | Supports the tls cipher policy 1 1 policy. _ _ _ _ |
|   |   | Supports the tls cipher policy 1 2 policy. _ _ _ _ |
|   |   | Supports the tls cipher policy 1 2 strict policy. _ _ _ _ _ |
|   |   | Supports the tls cipher policy 1 2 strict with 1 3 policy. _ _ _ _ _ _ _ _ |

|   | Custom policies (Advanced) | You can select the minimum TLS version. TLS 1.0 and later TLS 1.1 and later TLS 1.2 and later |
|---|---|---|
|   |   | You can enable TLS 1.3. |
|   |   | You can select specific cipher suites. |

**Monitoring**

| Feature |   | Description |
|---|---|---|
|   |   | Number of active connections. |
|   |   | Number of idle connections. |
|   |   | Maximum number of concurrent connections. |
|   |   | Number of failed backend TLS handshakes per second. |
|   |   | Number of new connections per second. |
|   |   | Number of dropped connections per second. |
|   |   | Number of failed backend connections per second. |
|   |   | Number of failed frontend TLS handshakes per second. |
|   |   | Number of custom responses per second. |
|   |   | Number of redirections per second. |
|   |   | Number of requests per second (QPS). |
|   |   | Number of requests per second that do not have session persistence. |
|   |   | Backend response time. |

| Monitoring metrics | Instance monitoring metrics |   |
|---|---|---|
|   |   | Request latency. |
|   |   | Outbound bandwidth. |
|   |   | Inbound bandwidth. |
|   |   | Number of 2xx status codes per second. |
|   |   | Number of 3xx status codes per second. |
|   |   | Number of 4xx status codes per second. |
|   |   | An SLB instance can handle up to 500 new connections per second. |
|   |   | The SLB instance processes 502 requests per second. |
|   |   | Number of 503 status codes per second. |
|   |   | An SLB instance can process 504 connections per second. |
|   |   | Number of 5xx status codes per second. |
|   |   | Number of backend 2xx status codes per second. |
|   |   | Number of backend 3xx status codes per second. |
|   |   | Number of backend 4xx status codes per second. |
|   |   | Number of backend 5xx status codes per second. |
|   |   | Number of healthy backend servers. |
|   |   | Number of unhealthy backend servers. |
|   | View monitoring data in the console | You can view monitoring data in the console. |

| pplication Load Introduction·Fea |   |   |
|---|---|---|
| View monitoring information |   |   |
|   | View monitoring data using API operations | You can view monitoring data using API operations. |
|   | View monitoring data using an SDK | You can view monitoring data using an SDK. |
| Alert rules | Set the resource scope for an alert rule | All resources. |
|   |   | Application groups. |
|   |   | Instances. |
|   | Select a monitoring metric for an alert | You can select a monitoring metric for an alert. |
|   | Select a dimension | You can select a listener protocol. |
|   |   | You can select a listener port. |
|   | Set a threshold and an alert level | Critical: phone call, text message, email, and WebHook. Warning: text message, email, and WebHook. Info: email and WebHook. |
