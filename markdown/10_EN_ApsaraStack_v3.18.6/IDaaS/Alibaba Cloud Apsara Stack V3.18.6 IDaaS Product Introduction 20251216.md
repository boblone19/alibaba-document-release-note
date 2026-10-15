---
title: "IDaaS Product Introduction 20251216"
product_version: "V3.18.6"
pdf_pages: 11
source_pdf: "a4c44cf8bb287d01_Alibaba Cloud Apsara Stack V3.18.6 IDaaS Product Introduction 20251216.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E5%BA%94%E7%94%A8%E8%BA%AB%E4%BB%BD%E6%9C%8D%E5%8A%A1/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20IDaaS%20Product%20Introduction%2020251216.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# IDaaS Product Introduction 20251216

## Table of Contents

- 1 What is IDaaS?
- 2 Terms
- 3 Scenarios

aS?

## 1 What is IDaaS?

Identity as a Service (IDaaS) is a cloud-based identity and access management (IAM) service that supports various all-in-one services, including organizational structure management, account lifecycle management, and single sign-on (SSO). IDaaS is ideal for connecting enterprise identity and access management (EIAM) systems and multi-account systems. It helps you improve the efficiency and security of identity management.

**Overview**

IDaaS is a cloud-native IAM system designed for enterprise users. It provides an all-in-one platform for administrators to centrally manage organizational structures, regulate the lifecycle and permissions of accounts, and configure features for applications such as SSO.

**Key features**

IDaaS helps administrators to manage organizational structures, regulate the lifecycle and permissions of accounts, and configure SSO for applications on an all-in-one platform. IDaaS allows users to access application portals, use independent login systems, and manage accounts. ​

**Benefits**

You can use IDaaS to manage accounts and assign permissions across applications in a centralized manner. This prevents repetitive permission configuration and O&M operations, and improves efficiency and productivity.
**Cloud-native**: IDaaS is a standard, secure, and stable service integrated with cloud service
identities.
**Open**: IDaaS is designed for developers and provides a wide range of templates. IDaaS can
also be integrated with other Apsara Stack services. ​

**Scenarios**

**EIAM**: You can use IDaaS to centrally manage accounts and assign permissions across
applications. This avoids repetitive permission configuration and O&M operations, and improves efficiency and productivity.
**Connect different account systems**: IDaaS account systems can be integrated with
applications and enterprise contacts. You can also use IDaaS as an EIAM system or as a centralized system that connects different account systems. IDaaS not only provides powerful identity management features, but also ensures high system availability and security. IDaaS is an efficient and secure EIAM service for connecting different account systems and managing identities. IDaaS is an ideal service for such scenarios.

## 2 Terms

**IDaaS terms**

Identity as a Service (IDaaS) is a cloud-based identity management service that helps enterprises centrally manage identities. ​

**EIAM**

Enterprise Identity and Access Management (EIAM) is a cloud-based identity management service that supports enterprise employment identity management systems, unified identity authentication platforms, identity and access management (IAM) systems, and authentication, authorization, account, and audit (4A) platforms. EIAM allows enterprises to manage the identities of internal personnel and partners, such as employees, interns, temporary staff, suppliers, and store staff. ​

**CIAM**

Customer Identity and Access Management (CIAM) is a cloud-based identity management service that allows enterprises to manage the identities of external users, such as consumers, members, and citizens. ​

**Internationalization**

Internationalization refers to the provision of multilingual services, user interfaces, images, documentation, operations, and support. IDaaS supports both Chinese and English. ​

**Security Authentication**

Security Authentication is a cloud-based service that provides password-free login methods such as phone number verification, authentication based on International Internet Finance Authentication Alliance (IIFAA), WebAuthn, text message verification, and one-time passwords (OTPs). It also offers SDKs for these methods. ​

**Zero trust**

Zero trust is an emerging network architecture that is widely used in the industry. The zerotrust architecture requires trusted identities and authorization for access to all services. This improves the security and ease of use of the overall network architecture. The zero-trust architecture can be used in modern workplace scenarios, such as telecommuting, multi-cloud deployment, and bring your own device (BYOD). ​

**Private deployment**

IDaaS private deployment refers to a private deployment of Apsara Stack IDaaS to a specified environment, such as your Apsara Stack virtual private cloud (VPC), an Amazon Web Services (AWS) environment, or a data center.

**Terms related to identity providers**

**IdP**

In Security Assertion Markup Language (SAML), an identity provider (IdP) verifies and authenticates the user and returns the SAML response information to a service provider (SP). IdP now refers to a unified identity management platform in general. In IDaaS, IDaaS is the IdP. ​

**SP**

In SAML, a service provider (SP) is a resolver that receives the response returned by an IdP. SP now refers to an application to which an IdP is connected. In IDaaS, an SP is an application.

**AD**

Active Directory (AD) is a directory service developed by Microsoft and is used to manage organizations, accounts, and permissions in enterprise business scenarios. AD can be separately deployed. A large number of modern applications also support the AD account system. However, enterprises usually look for other identity management solutions, such as IDaaS, because AD has compatibility issues and thus affects user experience. ​

**LDAP**

Lightweight Directory Access Protocol (LDAP) is usually used with AD and OpenLDAP but is also used with other systems such as Apache Directory. ​

**OpenLDAP**

OpenLDAP is an open source implementation of LDAP. ​

**ADFS**

Active Directory Federation Services (ADFS) is a default component of Windows Server and is used to extend AD access to external applications. However, ADFS is difficult to use and requires O&M. ​

**DingTalk Contacts**

DingTalk Contacts can be connected to IDaaS. You can synchronize identities between DingTalk and other account systems.

**Account**

**Organizational structure**

An organizational structure is a tree structure of an enterprise. A department is a unit in the structure.

**Organization**

An organization, organizational unit (OU), or department is a node in an organizational structure. In general, an organization is a department in an enterprise. ​

**Root organization node**

Each IDaaS instance has only one root node, which is the enterprise itself. In IDaaS, you can modify the name of the root node. ​

**Account**

In theory, each user has only one IDaaS account. A user can use an account to log in to the IDaaS Application Portal. A user can also be authorized to access applications after single sign-on (SSO) is implemented. ​

**Account lifecycle management**

Account lifecycle management is the process of managing the full lifecycle of an account, from the creation of an account (onboarding of the employee) to the termination of an account (offboarding of the employee), and includes operations such as disabling, locking, moving, and modifying the account. ​

**Group**

A group is a set of accounts and is used to assign permissions and set the synchronization scope. ​

**Synchronization**

In IDaaS, synchronization refers to the transfer of accounts and organizations between different systems. You can synchronize incremental data or full data, perform instant synchronization or scheduled synchronization, and synchronize data from IDaaS to an external system or from an external system to IDaaS. ​

**SCIM**

System for Cross-domain Identity Management (SCIM) is an international specification for the synchronization of accounts and organizations between different systems. A large number of applications receive SCIM synchronization requests to achieve the interoperability of different system identities.

**Terms related to applications**

**SSO**

SSO means that users can access all applications after a single login. SSO is implemented in different forms as applications evolve over time. In the context of IDaaS, SSO refers only to federated identity management based on standard protocols such as SAML and OpenID Connect (OIDC). ​

**IdP-initiated SSO**

IdP-initiated SSO is triggered when a user accesses an application after the user is logged in to the IDaaS application portal. In this process, the request is initiated by IDaaS (IdP). ​

**SP-initiated SSO**

SP-initiated SSO is triggered when a user accesses an application and the application determines whether login is required. If login is required, the user is redirected to IDaaS (IdP) for authentication and redirected back to the application. In this process, the request is initiated by the application (SP). ​

**Application user**

An application user is the identity assumed by a logged-on IDaaS account in the application during SSO. For example, zhangsan (IDaaS account) is the administrator (application user) in the Operations Platform application. IDaaS supports multiple ways to associate application users with IDaaS accounts. When multiple identities can be assumed in an application, users need to select one identity to access the application. ​

**Signature generation and verification**

A signature that uses asymmetric encryption algorithms is usually used to ensure that tokens are not forged or tampered with. When OIDC-based SSO is implemented, IDaaS uses an RSA- 256 private key to sign the issued `id_token` . To ensure that the token is not forged or tampered with, the application uses a public key to verify the token. ​

**Encryption and decryption**

Encryption is implemented by using symmetric or asymmetric encryption algorithms. When data of an IDaaS application is synchronized, IDaaS uses AES-256 to encrypt the data before the data is transmitted. The application uses a symmetric key to decrypt the data, which ensures privacy and accuracy in insecure network environments. ​

**Authorization**

Authorization refers to the assignment of permissions on objects (applications or other resources) to subjects (organizations or accounts). In IDaaS, you can grant access to all connected applications to manage permissions in a centralized manner. An organization can access an application only after you grant the organization access to the application in IDaaS.

**SAML**

Security Assertion Markup Language (SAML) is a widely adopted XML-based authentication standard for SSO. SAML is more complex than OIDC. IDaaS supports SAML 2.0. ​

**OIDC**

OpenID Connect (OIDC) is an identity federation protocol that is commonly used worldwide in scenarios such as SSO, authentication, and delegated authentication. OIDC was published in 2014 and is built on OpenID and OAuth 2.0. ​

**JWT**

JSON Web Token (JWT) is an open standard (RFC 7519) that defines a format for transmitting information between parties as a JSON object. In the context of identity and access management (IAM) in China, JWT often represents a simplified SSO implementation that is partially based on the OIDC implicit flow because the transmitted content can be signed and encrypted. ​

**CAS**

Central Authentication Service (CAS) is a global SSO protocol for the web. It supports the browser-server model. ​

**OAuth 2.0**

OAuth 2.0 is an authorization protocol that is often used to implement SSO. Because OIDC is implemented based on OAuth 2.0, most of the flows in OIDC and OAuth 2.0 are the similar. ​

**access_token/id_token/refresh_token**

An `access token` is used to call an API operation provided by an IdP. An `ID token` is used to obtain information about the account that is logged on.

| refresh token pires. ​ |   |
|---|---|
| pires. |   |

A `refresh token` is used to obtain a new access token after the original `access token`

**OIDC and OAuth client credentials flow**

In the client credentials flow, the application service instead of the user or account is granted permissions. The application obtains the permissions to call the resource or API operation.

| client secret _ |   | parameters |
|---|---|---|
| eters for an |   |   |

specified by IDaaS. ​

**OAuth authorization code flow**

In the authorization code flow, the user is authorized. The application obtains the identity information of the third-party system and logs on to the system by using the identity. DingTalk and WeChat both use the authorization code flow for login. ​

**OAuth device flow**

The device flow is used in specific hardware devices and allows a user to access the IDaaS login page in a computer or mobile browser when the device cannot display the IDaaS login page. After the user logs on, the identity of the user is transmitted to the device to complete the login. ​

**Terms related to login**

**Password complexity**

The passwords of the accounts must meet the complexity requirements. ​

**Lazy loading**

Lazy loading and just-in-time provisioning refer to the following design. If IDaaS cannot find the identity information of a user who logs on, an authentication request is automatically forwarded to the original identity system of the enterprise. When the user is authenticated, the account information is stored in IDaaS. Such designs are usually used in scenarios in which passwords in the original system cannot be imported to IDaaS and can only be imported by using lazy loading.

**MFA and 2FA**

Multi-factor authentication (MFA) and two-factor authentication (2FA) refer to the crossverification of multiple credentials presented by a user. MFA and 2FA are usually used to enhance account security for password-based login due to the security risks of passwords. IDaaS allows you to use 2FA methods such as text message verification code, email verification code, and OTP. ​

**OTP**

An OTP is a dynamic password that is valid for only one time. The most common type of OTP is the time-based OTP (TOTP), which is usually valid for 30 seconds. The server and the client need to align the seed and synchronize the time in advance. During the same time window, the OTP calculated by the client must be the same as the OTP of the server for authentication to complete. ​

**Application Portal**

IDaaS Application Portal is the page on which you can initiate SSO to all applications.

## 3 Scenarios

Identity as a Service (IDaaS) allows you to break down identity silos and manage the lifecycle of application accounts in different departments and organizations for centralized access control. Enterprise members can use one account to access all applications. ​ This topic describes some common scenarios of IDaaS.

**Scenario 1: Manage the accounts of R&D teams**

A large number of members in the R&D, O&M, and IT teams use applications. This leads to bottlenecks in the management of accounts and passwords. In recent years, issues related to account permissions have emerged. To ensure the security of enterprise assets, enterprises allow only team managers to manage the accounts of various systems. Managers spend a significant amount of time daily on labor-intensive account management tasks, such as changing passwords, unlocking accounts, and assigning permissions. Such low-value work reduces efficiency, and fragmented account management is risky and difficult to control. Manual management is infeasible. In IDaaS, you can integrate all applications related to R&D and O&M to implement single sign-on (SSO) and centralized permission management. This improves security and efficiency, and simplifies configuration. You can implement SSO for common documents, task management, code management, API management, resource O&M, logging, alerting, and communications. You need to only configure SSO for each application, which requires a minimum of 5 minutes per application. ​

**Scenario 2: Manage the accounts of business applications**

IDaaS allows you to centrally manage the permissions of users, such as permanent employees, temporary employees, interns, partners, and ecosystem enterprises, on applications such as business, finance, and human resources software as a service (HR SaaS) applications. ​ In addition, enterprises can use IDaaS to connect various self-developed applications for centralized access control.

**Scenario 3: Connect enterprise accounts**

If you use enterprise account systems such as DingTalk, Active Directory (AD), and WeCom, you may find it difficult to connect the accounts of different systems and applications. Specific applications cannot be adapted to the synchronization APIs of DingTalk and AD because the applications have unique rules, which results in repetitive operations when accounts are modified. The repetitive operations are labor-intensive and may cause improper configurations. In this case, you can use IDaaS to connect the identity information of different systems. Modifications to DingTalk and AD accounts can be instantly synchronized to all enterprise identity sources. Similarly, modifications in other applications can be synchronized to DingTalk and AD. Each identity source has issues, such as improperly mapped fields, missing fields, improper error handling, and different time policies. IDaaS streamlines configurations and provides a powerful set of connection capabilities for identity information. This helps enterprises break down the silos of identity information.
