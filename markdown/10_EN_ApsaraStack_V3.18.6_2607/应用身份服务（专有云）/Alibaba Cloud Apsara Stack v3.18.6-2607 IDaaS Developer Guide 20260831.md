---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 IDaaS Developer Guide 20260831"
product_version: "V3.18.6_2607"
doc_version: "20260831"
pdf_pages: 555
source_pdf: "Alibaba Cloud Apsara Stack v3.18.6-2607 IDaaS Developer Guide 20260831.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E5%BA%94%E7%94%A8%E8%BA%AB%E4%BB%BD%E6%9C%8D%E5%8A%A1%EF%BC%88%E4%B8%93%E6%9C%89%E4%BA%91%EF%BC%89/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20IDaaS%20Developer%20Guide%2020260831.pdf"
converter: pdf2md (PyMuPDF line classifier)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 IDaaS Developer Guide 20260831

## API Reference

### API overview

You can use Apsara Stack SDKs to call the API operations of IDentity as a Service (IDaaS), as shown in the following example:

**Add a Maven dependency**

```xml
<dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>aliyun-java-sdk-core</artifactId>
  <version>4.5.0</version>
</dependency>
```

**Sample API call**

```java
package org.example; public class CommoRequestTest {
    public static void main(String[] args) throws ClientException {
        DefaultProfile profile = DefaultProfile.getProfile(
            // The region ID of the current environment.
            "${regionId}",
            // The AccessKey ID of your Apsara Stack tenant account.
            "${ak}",
            // The AccessKey secret of your Apsara Stack tenant account.
            "${sk}");
        // The endpoint, in the format of api-idaas-
biz.${global:region}.${global:internet-domain}.
        String domain = "${domain}";
        // The IP address and port of the proxy.
        String proxy = "HTTP://${proxyIp}:${proxyPort}";
        String method = "GET";
        String version = "2021-12-01";
        String action = "ListLanguages";
        Map<String, String> headerParam = new HashMap<>();
        Map<String, String> pathParam = new HashMap<>();
        Map<String, String> queryParam = new HashMap<>();
        Map<String, String> bodyParam = new HashMap<>();
        queryParam.put("InstanceId","123");
        queryParam.put("Action",action);
        doRpcRequest(profile, domain, proxy, version, action, method, headerParam, path
Param, queryParam, bodyParam);
    public static void doRpcRequest(IClientProfile profile, String domain, String proxy
, String version, String action, String method,
                                    Map<String, String> headerParam,
                                    Map<String, String> pathParam,
                                    Map<String, String> queryParam,
                                    Map<String, String> bodyParam) {
```

```java
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setReadTimeoutMillis(100 * 1000);
        clientConfig.setHttpProxy(proxy);
        clientConfig.setIgnoreSSLCerts( true);
        profile.setHttpClientConfig(clientConfig);
        DefaultAcsClient client = new DefaultAcsClient(profile);
        CommonRequest request = new CommonRequest();
        request.setSysDomain(domain);
        request.setSysVersion(version);
        request.setSysAction(action);
        request.setSysMethod(MethodType.valueOf(method));
        request.setSysProtocol(ProtocolType.HTTPS);
        for (Map.Entry<String, String> entry : headerParam.entrySet()) {
            request.putHeadParameter(entry.getKey(), entry.getValue());
        for (Map.Entry<String, String> entry : pathParam.entrySet()) {
            request.putPathParameter(entry.getKey(), entry.getValue());
        for (Map.Entry<String, String> entry : queryParam.entrySet()) {
            request.putQueryParameter(entry.getKey(), entry.getValue());
        for (Map.Entry<String, String> entry : bodyParam.entrySet()) {
            request.putBodyParameter(entry.getKey(), entry.getValue());
        try {
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
        } catch (ServerException e) {
            // Add your computing logic for handling errors.
            // For example, you can display the exception information.
            System.out.println("ErrorCode=" + e.getErrCode());
            System.out.println("ErrorMessage=" + e.getErrMsg());
            // If the error persists, submit a ticket that includes the request ID
(RequestId) to request technical support.
            System.out.println("ResponseId=" + e.getRequestId());
        } catch (ClientException e) {
            // Add your computing logic for handling errors.
            // For example, you can display the exception information.
            System.out.println("ErrorCode=" + e.getErrCode());
            System.out.println("ErrorMessage=" + e.getErrMsg());
            System.out.println("ResponseId=" + e.getRequestId());
```

1. List of operations by function

**1.1 Instance management**

| No. | API operation | Related topic | Description |
|---|---|---|---|
| 1 | CreateApsaraEiamInstance | CreateApsaraEiamInstance | Creates an instance to use all capabilities of IDaaS Enterprise Identity Access Management (EIAM). |
| 2 | DeleteApsaraEiamInstance | DeleteApsaraEiamInstance | Deletes an IDaaS EIAM instance. |
| 3 | UpdateApsaraEiamInstance Description | UpdateApsaraEiamInstance Description | Modifies the description of an IDaaS EIAM instance. |
| 4 | ListApsaraEiamInstances | ListApsaraEiamInstances | Queries the information about one or more IDaaS EIAM instances. |
| 5 | UpdateApsaraEiamInstance Quota | UpdateApsaraEiamInstance Quota | Queries the details of an IDaaS EIAM instance. |
| 6 | GetInstanceLicense | GetInstanceLicense | Queries the valid license of an IDaaS EIAM instance. |

**1.2 Application management**

| No. | API operation | Related topic | Description |
|---|---|---|---|
| - | Basic information management | Basic information management |   |
| 1 | CreateApplication | CreateApplication | Creates an application on an IDaaS EIAM instance. |
| 2 | DeleteApplication | DeleteApplication | Deletes an application in IDaaS EIAM. |
| 3 | UpdateApplicationDescripti on | UpdateApplicationDescriptio n | Modifies the description of an application in IDaaS EIAM. |
| 4 | EnableApplication | EnableApplication | Enables a disabled application in IDaaS EIAM. |

| 5 | DisableApplication | DisableApplication | Disables an enabled application in IDaaS EIAM. If an IDaaS EIAM application is disabled, all its features cannot be used. |
|---|---|---|---|
| 6 | GetApplication | GetApplication | Queries the details of an application in IDaaS EIAM. |
| 7 | ListApplications | ListApplications | Queries the information about one or more applications in IDaaS EIAM by page. |
| 8 | GetApplicationTemplate | GetApplicationTemplate | Queries the information about an application template in IDaaS EIAM. |
| 9 | UpdateApplicationInfo | UpdateApplicationInfo | Modifies the basic information about an application in IDaaS EIAM. |
| 10 | ListApplicationsForNetwork AccessEndpoint | ListApplicationsForNetworkA ccessEndpoint | Queries a list of applications for a network access endpoint. |
| 8 | ListApplicationsForNetwork Zone | ListApplicationsForNetworkZ one | Queries a list of applications associated with a network zone. |
| 9 | ListApplicationsForGroup | ListApplicationsForGroup | Queries a list of applications that an account group in IDaaS EIAM can access. |
| - | SSO configuration management | SSO configuration management |   |
| 1 | EnableApplicationSso | EnableApplicationSso | Enables the single sign-on (SSO) feature for an application in IDaaS EIAM. |
| 2 | DisableApplicationSso | DisableApplicationSso | Disables the SSO feature for an application in IDaaS EIAM. This way, employees cannot log in to the application by using SSO. |
| 3 | SetApplicationSsoConfig | SetApplicationSsoConfig | Configures the SSO configuration attributes for an application in IDaaS EIAM. |

| 4 | GetApplicationSsoConfig | GetApplicationSsoConfig | Queries the SSO configuration attributes of an application in IDaaS EIAM. |
|---|---|---|---|
| - | Authorization management | Authorization management |   |
| 1 | AuthorizeApplicationToUser s | AuthorizeApplicationToUsers | Grants the permissions to access an application to multiple accounts in IDaaS EIAM at a time. |
| 2 | AuthorizeApplicationToOrg anizationalUnits | AuthorizeApplicationToOrga nizationalUnits | Grants the permissions to access an application to multiple organizations in IDaaS EIAM at a time. |
| 3 | AuthorizeApplicationToGro ups | AuthorizeApplicationToGrou ps | Grants the permissions to access an application to multiple account groups in IDaaS EIAM at a time. |
| 4 | RevokeApplicationFromUse rs | RevokeApplicationFromUser s | Revokes the permissions to access an application from multiple accounts in IDaaS EIAM at a time. |
| 5 | RevokeApplicationFromOrg anizationalUnits | RevokeApplicationFromOrga nizationalUnits | Revokes the permissions to access an application from multiple organizations in IDaaS EIAM at a time. |
| 6 | RevokeApplicationFromGro ups | RevokeApplicationFromGrou ps | Revokes the permissions to access an application from multiple account groups in IDaaS EIAM at a time. |
| 7 | UpdateApplicationAuthoriz ationType | UpdateApplicationAuthorizat ionType | Modifies the authorization type of an application in IDaaS EIAM. |
| 8 | ListUsersForApplication | ListUsersForApplication | Queries a list of accounts that are granted permissions to access an application in IDaaS EIAM by page. This operation returns the IDs of the accounts. To obtain the details of the accounts, call the GetUser operation. |

| 9 | ListOrganizationalUnitsForA pplication | ListOrganizationalUnitsForAp plication | Queries a list of organizations that are granted permissions to access an application in IDaaS EIAM by page. This operation returns the IDs of the organizations. To obtain the details of the organizations, call the GetOrganizationalUnit operation. |
|---|---|---|---|
| 10 | ListGroupsForApplication | ListGroupsForApplication | Queries a list of account groups that are granted permissions to access an application in IDaaS EIAM by page. This operation returns the IDs of the account groups. To query the details of the account groups, call the GetGroup operation. |
| 11 | ListApplicationsForUser | ListApplicationsForUser | Queries a list of applications that an account in IDaaS EIAM can access by page. This operation returns the IDs of the applications. To obtain the details of the applications, call the GetApplication operation. |
| 12 | ListApplicationsForOrganiz ationalUnit | ListApplicationsForOrganizat ionalUnit | Queries a list of applications that an organization in IDaaS EIAM can access by page. This operation returns the IDs of the applications. To obtain the details of the applications, call the GetApplication operation. |
| - | Client key management | Client key management |   |
| 1 | CreateApplicationClientSec ret | CreateApplicationClientSecr et | Creates a client key for an application in IDaaS EIAM. An application in IDaaS EIAM can have up to two client keys. |
| 2 | DeleteApplicationClientSec ret | DeleteApplicationClientSecr et | Deletes a client key from an application in IDaaS EIAM. |
| 3 | DisableApplicationClientSe cret | DisableApplicationClientSecr et | Disables a client key for an application in IDaaS EIAM. |

| 4 | EnableApplicationClientSec ret | EnableApplicationClientSecr et | Enables a client key for an application in IDaaS EIAM. |
|---|---|---|---|
| 5 | ListApplicationClientSecret s | ListApplicationClientSecrets | Queries all client keys of an application in IDaaS EIAM. This operation returns masked key secrets. To obtain unmasked key secrets, call the ObtainApplicationClientSecret operation. |
| 6 | ObtainApplicationClientSec ret | ObtainApplicationClientSecr et | Queries a client key of an application in IDaaS EIAM. This operation returns a masked key secret. To obtain an unmasked key secret, call the ListApplicationClientSecrets operation. |
| 7 | UpdateApplicationClientSec retExpirationTime | UpdateApplicationClientSecr etExpirationTime | Modifies the expiration time of a client key for an application in IDaaS EIAM. |
| - | Application token management | Application token management |   |
| 1 | CreateApplicationToken | CreateApplicationToken | Creates an application token. |
| 2 | EnableApplicationToken | EnableApplicationToken | Enables an application token. |
| 3 | DisableApplicationToken | DisableApplicationToken | Disables an application token. |
| 4 | UpdateApplicationTokenEx pirationTime | UpdateApplicationTokenExpi rationTime | Modifies the expiration time of an application token. |
| 5 | ListApplicationTokens | ListApplicationTokens | Queries a list of application tokens. |
| 6 | ObtainApplicationToken | ObtainApplicationToken | Queries an application token. |
| 7 | DeleteApplicationToken | DeleteApplicationToken | Deletes an application token. |
| - | Application RAM user management | Application RAM user management |   |

| 1 | AddApplicationAccountToU ser | AddApplicationAccountToUs er | Adds an application account for an employee under the current application in IDaaS EIAM. |
|---|---|---|---|
| 2 | ListApplicationAccounts | ListApplicationAccounts | Queries a list of application accounts under an application in IDaaS EIAM by page. |
| 3 | ListApplicationAccountsFor User | ListApplicationAccountsForU ser | Queries all application accounts of a user under the current application in IDaaS EIAM. |
| 4 | RemoveApplicationAccount FromUser | RemoveApplicationAccountF romUser | Deletes the application account of an employee under the current application in IDaaS EIAM. |
| - | Application Developer API | Application Developer API |   |
| 1 | EnableApplicationApiInvok e | EnableApplicationApiInvoke | Enables the Developer API feature for an application in IDaaS EIAM. |
| 2 | DisableApplicationApiInvok e | DisableApplicationApiInvoke | Disables the Developer API feature for an application in IDaaS EIAM. |
| 3 | SetApplicationGrantScope | SetApplicationGrantScope | Configures the permissions of the Developer API feature of an application in IDaaS EIAM. |
| 4 | GetApplicationGrantScope | GetApplicationGrantScope | Queries the permissions of the Developer API feature for an application in IDaaS EIAM. |
| - | Application account synchronization | Application account synchronization |   |
| 1 | DisableApplicationProvision ing | DisableApplicationProvisioni ng | Disables the account synchronization feature for an application in IDaaS EIAM. |
| 2 | EnableApplicationProvisioni ng | EnableApplicationProvisionin g | Enables the account synchronization feature for an application in IDaaS EIAM. |

| 3 | SetApplicationProvisioning Config | SetApplicationProvisioningC onfig | Configures the account synchronization feature for an application in IDaaS EIAM. |
|---|---|---|---|
| 4 | SetApplicationProvisioning Scope | SetApplicationProvisioningSc ope | Configures the account synchronization scope of an application in IDaaS EIAM. This scope is the same as the scope within which developers can call the Developer API operations to query and manage accounts. |
| 5 | GetApplicationProvisioning Config | GetApplicationProvisioningC onfig | Queries the configuration of the account synchronization feature for an application in IDaaS EIAM. |
| 6 | GetApplicationProvisioning Scope | GetApplicationProvisioningS cope | Queries the account synchronization scope of an application in IDaaS EIAM. This scope is the same as the scope within which developers can call the Developer API operations to query and manage accounts. |

**1.3 Account management**

| No. | API operation | Related topic | Description |
|---|---|---|---|
| 1 | CreateUser | CreateUser | Creates an IDaaS EIAM account for an IDaaS EIAM instance. |
| 2 | AddUserToOrganizationalUn its | AddUserToOrganizationalUni ts | Adds an IDaaS EIAM account to multiple IDaaS EIAM organizations. If the account already exists in an organization, a success response is returned. |
| 3 | DeleteUser | DeleteUser | Deletes an IDaaS EIAM account. After the account is deleted, the information related to the account is also cleared. |

| 4 | RemoveUserFromOrganizati onalUnts | RemoveUserFromOrganizati onalUnits | Removes an IDaaS EIAM account from multiple IDaaS EIAM organizations. You cannot remove an account from a primary organization. |
|---|---|---|---|
| 5 | UpdateUser | UpdateUser | Modifies the basic information about an IDaaS EIAM account. |
| 6 | UpdateUserPassword | UpdateUserPassword | Changes the password of an IDaaS EIAM account. The password must meet the requirements of the password policies in the IDaaS console. |
| 7 | UpdateUserDescription | UpdateUserDescription | Modifies the description of an IDaaS EIAM account. |
| 8 | DisableUser | DisableUser | Disables an IDaaS EIAM account. If the account is already disabled, a success response is returned. |
| 9 | EnableUser | EnableUser | Enables an IDaaS EIAM account. |
| 10 | UnlockUser | UnlockUser | Unlocks a locked IDaaS EIAM account. |
| 11 | SetUserPrimaryOrganizatio nalUnit | SetUserPrimaryOrganization alUnit | Configures the primary organization to which an IDaaS EIAM account belongs. This operation removes the account from its original primary organization and adds it to the new primary organization. |
| 12 | GetUser | GetUser | Queries the details of an IDaaS EIAM account. |
| 13 | ListUsers | ListUsers | Queries a list of IDaaS EIAM accounts by page. |

**1.4 Organization management**

| No . | API operation | Related topic | Description |
|---|---|---|---|
| 1 | CreateOrganizationalUnit | CreateOrganizationalUnit | Creates an IDaaS EIAM organization within a specific organization. |
| 2 | DeleteOrganizationalUnit | DeleteOrganizationalUnit | Deletes an IDaaS EIAM organization. If the organization has IDaaS EIAM accounts or subordinate organizations, the delete operation fails. |
| 3 | DeleteOrganizationalUnitChil dren | DeleteOrganizationalUnitChi ldren | Deletes all data of an IDaaS EIAM organization. You can forcibly delete all accounts and subordinate organizations of a specific organization. |
| 4 | UpdateOrganizationalUnit | UpdateOrganizationalUnit | Modifies the basic information about an IDaaS EIAM organization. By default, if you do not specify the request parameters, the basic information about the organization is not modified. |
| 5 | UpdateOrganizationalUnitDe scription | UpdateOrganizationalUnitDe scription | Modifies the description of an IDaaS EIAM organization to add a tag or note to it. |
| 6 | UpdateOrganizationalUnitPar entId | UpdateOrganizationalUnitPa rentId | Modifies the parent organization ID of an IDaaS EIAM organization. This operation moves the organization from its parent node to a new node. |
| 7 | GetRootOrganizationalUnit | GetRootOrganizationalUnit | Queries the information about a root IDaaS EIAM organization. |
| 8 | GetOrganizationalUnit | GetOrganizationalUnit | Queries the information about an IDaaS EIAM organization. |
| 9 | ListOrganizationalUnits | ListOrganizationalUnits | Queries a list of IDaaS EIAM organizations by page. |

| 10 | ListOrganizationalUnitParent s | ListOrganizationalUnitParent s | Queries a list of all parent organizations of an IDaaS EIAM organization. The results are sorted in descending order based on the level of the parent organizations of the IDaaS EIAM organization. |
|---|---|---|---|

**1.5 Account group management**

| No. | API operation | Related topic | Description |
|---|---|---|---|
| 1 | CreateGroup | CreateGroup | Creates an IDaaS EIAM account group. |
| 2 | AddUsersToGroup | AddUsersToGroup | Adds multiple IDaaS EIAM accounts to an IDaaS EIAM account group. |
| 3 | DeleteGroup | DeleteGroup | Deletes the information about an IDaaS EIAM account group. |
| 4 | RemoveUsersFromGroup | RemoveUsersFromGroup | Removes multiple IDaaS EIAM accounts from an IDaaS EIAM account group. |
| 5 | UpdateGroup | UpdateGroup | Modifies the information about an IDaaS EIAM account group. If the information is empty, it is not updated by default. |
| 6 | UpdateGroupDescription | UpdateGroupDescription | Modifies the description of an IDaaS EIAM account group to add a note or tag to it. |
| 7 | GetGroup | GetGroup | Queries the details of an IDaaS EIAM account group. |
| 8 | ListGroups | ListGroups | Queries a list of IDaaS EIAM account groups. |
| 9 | ListUsersForGroup | ListUsersForGroup | Queries a list of accounts that belong to an IDaaS EIAM account group. |
| 10 | ListGroupsForUser | ListGroupsForUser | Queries a list of account groups to which an IDaaS EIAM account belongs. |

**1.6 Identity provider (IdP) management**

| No. | API operation | Related topic | Description |
|---|---|---|---|
| 1 | CreateIdentityProvider | CreateIdentityProvider | Creates an IdP. |
| 2 | DeleteIdentityProvider | DeleteIdentityProvider | Deletes an IdP. |
| 3 | UpdateIdentityProvider | UpdateIdentityProvider | Modifies the basic configurations of an IdP. |
| 4 | GetIdentityProvider | GetIdentityProvider | Queries an IdP. |
| 5 | ListIdentityProviders | ListIdentityProviders | Queries a list of IdPs. |
| 6 | EnableIdentityProviderUdPull | EnableIdentityProviderUdPul l | Enables the inbound synchronization feature for IdPs. |
| 7 | DisableIdentityProviderUdPul l | DisableIdentityProviderUdPu ll | Disables the inbound synchronization feature for IdPs. |
| 8 | SetIdentityProviderUdPullCon figuration | SetIdentityProviderUdPullCo nfiguration | Modifies the inbound synchronization configurations for IdPs. |
| 9 | GetIdentityProviderUdPullCo nfiguration | GetIdentityProviderUdPullCo nfiguration | Queries the inbound synchronization configurations for IdPs. |

**1.7 Password policy management**

| No. | API operation | Related topic | Description |
|---|---|---|---|
| 1 | SetForgetPasswordConfigur ation | SetForgetPasswordConfigu ration | Configures a forgot password policy for an IDaaS EIAM instance. |
| 2 | SetPasswordInitializationCo nfiguration | SetPasswordInitializationC onfiguration | Configures a password initialization policy for an IDaaS EIAM instance. |

| 3 | SetPasswordHistoryConfigur ation | SetPasswordHistoryConfig uration | Configures a password history policy for an IDaaS EIAM instance. |
|---|---|---|---|
| 4 | SetPasswordExpirationConfi guration | SetPasswordExpirationCon figuration | Configures a password expiration policy for an IDaaS EIAM instance. |
| 5 | SetPasswordComplexityCon figuration | SetPasswordComplexityCo nfiguration | Configures a password complexity policy for an IDaaS EIAM instance. |
| 6 | GetForgetPasswordConfigur ation | GetForgetPasswordConfigu ration | Queries the forgot password policy of an IDaaS EIAM instance. |
| 7 | GetPasswordInitializationCo nfiguration | GetPasswordInitializationC onfiguration | Queries the password initialization policy of an IDaaS EIAM instance. |
| 8 | GetPasswordHistoryConfigur ation | GetPasswordHistoryConfig uration | Queries the password history policy of an IDaaS EIAM instance. |
| 9 | GetPasswordExpirationConfi guration | GetPasswordExpirationCon figuration | Queries the password expiration policy of an IDaaS EIAM instance. |
| 10 | GetPasswordComplexityCon figuration | GetPasswordComplexityCo nfiguration | Queries the password complexity policy of an IDaaS EIAM instance. |

**1.8 Synchronization**

| No. | API operation | Related topic | Description |
|---|---|---|---|
| 1 | ListSynchronizationJobs | ListSynchronizationJobs | Queries a list of synchronization jobs. |
| 2 | RunSynchronizationJob | RunSynchronizationJob | Creates a synchronization job and immediately runs the job. |
| 3 | GetSynchronizationJob | GetSynchronizationJob | Queries the information about a synchronization job. |

**1.9 Brand**

| No. | API operation | Related topic | Description |
|---|---|---|---|
| 1 | CreateBrand | CreateBrand | Creates a brand. |
| 2 | UpdateBrand | UpdateBrand | Modifies a brand. |

**1.10 Network endpoints**

| No. | API operation | Related topic | Description |
|---|---|---|---|
| 1 | CreateNetworkAccessEndpo int | CreateNetworkAccessEndpoi nt | Creates a dedicated network endpoint. |
| 2 | DeleteNetworkAccessEndpoi nt | DeleteNetworkAccessEndpoi nt | Deletes a dedicated network endpoint. |
| 3 | UpdateNetworkAccessEndp ointName | UpdateNetworkAccessEndpoi ntName | Modifies the name of a dedicated network endpoint. |
| 4 | ListNetworkAccessEndpoint AvailableRegions | ListNetworkAccessEndpointA vailableRegions | Queries a list of regions in which network endpoints can be created for IDaaS EIAM. |
| 5 | ListNetworkAccessEndpoint AvailableZones | ListNetworkAccessEndpointA vailableZones | Queries a list of zones within a region in which network endpoints can be created for IDaaS EIAM. |
| 6 | GetNetworkAccessEndpoint | GetNetworkAccessEndpoint | Queries the information about a network endpoint. |
| 7 | ListNetworkAccessEndpoints | ListNetworkAccessEndpoints | Queries a list of network endpoints of an IDaaS EIAM instance. |
| 8 | ListNetworkAccessPaths | ListNetworkAccessPaths | Queries a list of access paths for a network endpoint. |
| 9 | ListVpcs | ListVpcs | Queries a list of virtual private clouds (VPCs) available for an account when a network endpoint is created. |

| 10 | ListVSwitches | ListVSwitches | Queries a list of vSwitches in a VPC when a network endpoint is created. |
|---|---|---|---|
| 11 | ListNatGateways | ListNatGateways | Queries the outbound public IP addresses of a network endpoint. |
| 12 | ListNetworkInterfaces | ListNetworkInterfaces | Queries a list of elastic network interfaces (ENIs) associated with a network endpoint. |
| 13 | CheckServiceLinkedRoleExis tence | CheckServiceLinkedRoleExist ence | Checks whether a service- linked role exists. |
| 14 | CreateServiceLinkedRole | CreateServiceLinkedRole | Creates a service-linked role. |

**1.11 Network zone management**

| No. | API operation | Related topic | Description |
|---|---|---|---|
| 1 | CreateNetworkZone | CreateNetworkZone | Creates a network zone. |
| 2 | DeleteNetworkZone | DeleteNetworkZone | Deletes a network zone. |
| 3 | UpdateNetworkZone | UpdateNetworkZone | Modifies a network zone. |
| 4 | UpdateNetworkZoneDescripti on | UpdateNetworkZoneDescriptio n | Modifies the description of a network zone. |
| 5 | ListNetworkZones | ListNetworkZones | Queries a list of network zones. |
| 6 | GetNetworkZone | GetNetworkZone | Queries a network zone. |

**1.12 Others**

| No. | API operation | Related topic | Description |
|---|---|---|---|
| 1 | DisableIdentityProviderAuth n | DisableIdentityProviderAut hn | Disables the IdP authentication feature. |

| 2 | EnableIdentityProviderAuthn | EnableIdentityProviderAuth n | Enables the IdP authentication feature. |
|---|---|---|---|
| 3 | ListApplicationSupportedPro visionProtocolTypes | ListApplicationSupportedPr ovisionProtocolTypes | Queries a list of synchronization protocol types that are supported by an application. |
| 4 | DeleteBrand | DeleteBrand | Deletes a brand. |
| 5 | DisableBrand | DisableBrand | Disables a brand. |
| 6 | EnableBrand | EnableBrand | Enables a brand. |
| 7 | GetBrand | GetBrand | Queries the details of a brand. |
| 8 | GetLoginRedirectApplication ForBrand | GetLoginRedirectApplicatio nForBrand | Queries the application to which users are redirected after login for a brand. |
| 9 | ListBrands | ListBrands | Queries a list of brands. |
| 10 | SetLoginRedirectApplication ForBrand | SetLoginRedirectApplicatio nForBrand | Configures the application to which users are redirected after login for a brand. |
| 11 | UpdateDomainBrand | UpdateDomainBrand | Modifies the brand associated with a domain name. |

### Endpoints

IDentity as a Service (IDaaS) provides OpenAPI operations. Business applications can manage IDaaS resources by calling the API operations. IDaaS endpoints are in the following format: api-idaas-biz.${global_region}.${internet_domain} To obtain the value of global_region and internet_domain, log in to the Apsara Uni-manager Management Console. In the top navigation bar, choose **Security > Identity and O&M**
**Security > IDaaS**. On the IDaaS page, find the required instance and click Console in the
Actions column. On the Quick Start page, view the **URL** in the upper-right corner. In the following example: The value of global_region is cn-ece-entity121-d01. The value of internet_domain is cloud.ece-group-121.com.

### Authorization information

Resource Access Management (RAM) is a service provided by Apsara Stack to manage user identities and resource access permissions. RAM allows you to grant minimum permissions to RAM users without the need to share the AccessKey pair of your Apsara Stack tenant account. RAM uses policies to define permissions. This topic describes the elements such as Action, Resource, and Condition that are defined by IDentity as a Service (IDaaS). You can use the elements to create policies in RAM. The code (RamCode) that is used in RAM to indicate IDaaS is eiam. You can grant permissions on IDaaS at the resource level.

**General structure of a policy**

Policies can be stored as JSON files. The following code provides an example on the general structure of a policy:

```json
  "Version": "1",
  "Statement": [
      "Effect": "<Effect>",
      "Action": "<Action>",
      "Resource": "<Resource>",
      "Condition": {
        "<Condition_operator>": {
          "<Condition_key>": [
            "<Condition_value>"
```

`]` `]` The following list describes the fields in the policy: Effect: specifies the authorization result. Valid values: Allow and Deny. Action: specifies one or more operations that are allowed or denied. For more information, see the "Action" section of this topic. Resource: specifies one or more resources to which the policy applies. You can use an Alibaba Cloud Resource Name (ARN) to specify a resource. For more information, see the "Resource" section of this topic. Condition: specifies one or more conditions that are required for the policy to take effect. This field is optional. For more information, see the "Condition" section of this topic. Condition_operator: specifies the conditional operators. Different types of conditions support different conditional operators. For more information, see Policy elements. Condition_key: specifies the condition keys. Condition_value: specifies the condition values.

**Action**

The following table lists the actions defined by placeholder-${productName}. The table's columns are detailed below: Action: The actions can be used in the `Action` element of RAM permission policy statements to grant permissions to perform the operation. API: The API that you can call to perform the action. Access level: The predefined level of access granted for each API. Valid values: create, list, get, update, and delete. Resource type: The type of the resource that support authorization to perform the action. It indicates if the action supports resource-level permission. The specified resource must be compatible with the action. Otherwise, the policy will be ineffective. For APIs with resource-level permissions, required resource types are marked with an asterisk (*). Specify the corresponding ARN in the `Resource` element of the policy. For APIs without resource-level permissions, it is shown as All Resources. Use an asterisk (*) in the `Resource` element of the policy. Condition key: The condition keys defined by the service. The key allows for granular control, applying to either actions alone or actions associated with specific resources. In addition to service-specific condition keys, Alibaba Cloud provides a set of common condition keys that are applicable across all RAM-integrated services. For more information, see Common condition keys. Dependent action: The dependent actions required to run the action. To complete the action, the RAM user or the RAM role must have the permissions to perform all dependent actions.

|   | Operation |   | API |   | Operati on type |   | Resource type |   | Condition key | Associated operation |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | eiam:GetFeder atedCredential |   | GetFederatedCr |   |   |   | *FederatedCreden tialProvider acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | ederatedCr |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | edential | edentialProvide |   |   |   |   |   |   |   |   |
|   |   |   |   |   | get |   | stance/{#Instan |   | N/A | N/A |   |
|   | Provider |   |   |   |   |   |   |   |   |   |   |
|   |   |   | r |   |   |   | ceId}/federated |   |   |   |   |
|   |   |   |   |   |   |   | credentialprovi |   |   |   |   |
|   |   |   |   |   |   |   | der/{#Federate |   |   |   |   |
|   |   |   |   |   |   |   | dCredentialProv |   |   |   |   |
|   |   |   |   |   |   |   | iderId} |   |   |   |   |
|   | eiam:DisableBr and |   | DisableBrand |   |   |   | *Brand acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | leBrand | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/brand/{# |   |   |   |   |
|   |   |   |   |   |   |   | BrandId} |   |   |   |   |

|   |   |   |   |   |   |   | *FederatedCreden tialProvider acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/federated |   |   |   |   |
|   | eiam:UpdateFe |   | UpdateFederate |   |   |   | credentialprovi |   |   |   |   |
|   | deratedCreden |   | dCredentialProv |   | update |   | der/{#Federate |   | N/A | N/A |   |
|   | tialProvider |   | ider |   |   |   | dCredentialProv |   |   |   |   |
|   |   |   |   |   |   |   | iderId} |   |   |   |   |
|   | eiam:UpdateAp plicationDescri ption |   | UpdateApplicati |   |   |   | *Application acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | teApplicati | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   | onDescription |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |
|   | eiam:RemoveU serFromOrgani zationalUnits |   | RemoveUserFro mOrganizationa |   |   |   | *User acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | anizationa | delete |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   | lUnits |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/user/{#Us |   |   |   |   |
|   |   |   |   |   |   |   | erId} |   |   |   |   |
|   | eiam:ListDomai ns |   | ListDomains |   |   |   | *Domain acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | omains | list |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/domain/* |   |   |   |   |

|   | eiam:EnableIde ntityProviderAu thn |   | EnableIdentityP |   |   |   | *IdentityProvider acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | leIdentityP | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   | roviderAuthn |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/identitypr |   |   |   |   |
|   |   |   |   |   |   |   | ovider/{#Identi |   |   |   |   |
|   |   |   |   |   |   |   | tyProviderId} |   |   |   |   |
|   | eiam:RevokeAp plicationFromO rganizationalUn |   | RevokeApplicati onFromOrganiz |   |   |   | *Application acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | keApplicati mOrganiz | delete |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | ationalUn | ationalUnits |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   | its |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |
|   | eiam:GetIdentit yProviderUdPul lConfiguration |   | GetIdentityProvi derUdPullConfig |   |   |   | *IdentityProvider acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | entityProvi dPullConfig | get |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | uration | uration |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/identitypr |   |   |   |   |
|   |   |   |   |   |   |   | ovider/{#Identi |   |   |   |   |
|   |   |   |   |   |   |   | tyProviderId} |   |   |   |   |
|   | eiam:ListApplic ationAccounts |   | ListApplicationA |   |   |   | *ApplicationAccou nt acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | pplicationA |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | ccounts | ccounts |   | list |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id}/applicationa |   |   |   |   |
|   |   |   |   |   |   |   | ccount/* |   |   |   |   |
|   | eiam:UpdateDo mainIcpNumbe r |   | UpdateDomainI cpNumber |   |   |   | *Domain acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | teDomainI mber | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/domain/{ |   |   |   |   |
|   |   |   |   |   |   |   | #DomainId} |   |   |   |   |

|   | eiam:UpdateUs er |   | UpdateUser |   |   |   | *User acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | teUser | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/user/{#Us |   |   |   |   |
|   |   |   |   |   |   |   | erId} |   |   |   |   |
|   | eiam:Authorize ApplicationToO rganizationalUn |   | AuthorizeApplic ationToOrganiz |   |   |   | *Application acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | orizeApplic ToOrganiz | create |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | ationalUn | ationalUnits |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   | its |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |
|   | eiam:DisableAp plicationApiInv oke |   | DisableApplicati |   |   |   | *Application acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | leApplicati | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   | onApiInvoke |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |
|   | eiam:CreateIde ntityProvider |   | CreateIdentityP rovider |   |   |   | *IdentityProvider acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | eIdentityP er | create |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/identitypr |   |   |   |   |
|   |   |   |   |   |   |   | ovider/* |   |   |   |   |

|   |   |   |   |   |   |   | *IdentityProvider acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   | eiam:DisableId entityProviderU | isableId |   |   |   |   |   |   |   |   |   |
|   |   |   | DisableIdentityP |   | update |   | ceId}/identitypr |   | N/A | N/A |   |
|   | dPull |   | roviderUdPull |   |   |   | ovider/{#Identi |   |   |   |   |
|   |   |   |   |   |   |   | tyProviderId} |   |   |   |   |
|   | eiam:ListRegio ns |   | ListRegions |   | get |   | *All resources * |   | N/A | N/A |   |
|   | eiam:GetForget PasswordConfi guration |   | GetForgetPassw ordConfiguratio n |   | get |   | *AuthenticationSo urce acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   | get | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId} |   |   |   |   |
|   | eiam:GetPassw ordInitialization Configuration |   | GetPasswordInit ializationConfig uration |   | get |   | *Instance acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   | get | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   |   |   | N/A | N/A |   |
|   |   |   |   | n |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId} |   |   |   |   |
|   | eiam:CreateNe tworkAccessEn dpoint |   | CreateNetwork AccessEndpoint |   |   |   | *NetworkAccessE ndpoint acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | eNetwork ssEndpoint | create |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/networkac |   |   |   |   |
|   |   |   |   |   |   |   | cessendpoint/* |   |   |   |   |

|   | eiam:UpdateOr ganizationalUni tParentId |   | UpdateOrganiza tionalUnitParent |   |   |   | *OrganizationalUn it acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | lUnitParent |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | tionalUni tId | Id |   | update |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/organizati |   |   |   |   |
|   |   |   |   |   |   |   | onalunit/{#Org |   |   |   |   |
|   |   |   |   |   |   |   | anizationalUnitI |   |   |   |   |
|   |   |   |   |   |   |   | d} |   |   |   |   |
|   | eiam:Authorize ApplicationToU sers |   | AuthorizeApplic |   |   |   | *Application acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | orizeApplic | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   | ationToUsers |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |
|   | eiam:EnableCo nditionalAccess Policy |   | EnableCondition |   |   |   | *ConditionalAcces sPolicy acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | leCondition |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | alAccess | alAccessPolicy |   | update |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/condition |   |   |   |   |
|   |   |   |   |   |   |   | alaccesspolicy/{ |   |   |   |   |
|   |   |   |   |   |   |   | #ConditionalAcc |   |   |   |   |
|   |   |   |   |   |   |   | essPolicyId} |   |   |   |   |

|   |   |   |   |   |   |   | *Secret acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   | eiam:EnableAp |   | EnableApplicati |   |   |   | Id}/secret/{#Se |   | N/A |   |   |
|   | plicationClientS |   |   |   | update |   |   |   |   |   |   |
|   | ecret |   | onClientSecret |   |   |   | cretId} |   |   |   |   |
|   | eiam:DeleteIde ntityProvider |   | DeleteIdentityPr |   |   |   | *IdentityProvider acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | eIdentityPr | delete |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | ovider | ovider |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/identitypr |   |   |   |   |
|   |   |   |   |   |   |   | ovider/{#Identi |   |   |   |   |
|   |   |   |   |   |   |   | tyProviderId} |   |   |   |   |
|   | eiam:DeleteCo nditionalAccess Policy |   | DeleteCondition |   |   |   | *ConditionalAcces sPolicy acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | eCondition |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | alAccess | alAccessPolicy |   | delete |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/condition |   |   |   |   |
|   |   |   |   |   |   |   | alaccesspolicy/{ |   |   |   |   |
|   |   |   |   |   |   |   | #ConditionalAcc |   |   |   |   |
|   |   |   |   |   |   |   | essPolicyId} |   |   |   |   |
|   | eiam:UpdateGr oup |   | UpdateGroup |   |   |   | *Group acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | teGroup | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/group/{# |   |   |   |   |
|   |   |   |   |   |   |   | GroupId} |   |   |   |   |

|   | eiam:SetForget PasswordConfi guration |   | SetForgetPassw ordConfiguratio n |   | update |   | *Instance acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   | update | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId} |   |   |   |   |
|   | eiam:UpdateNe tworkZoneDesc ription |   | UpdateNetwork ZoneDescriptio |   |   |   | *NetworkZone acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | teNetwork Descriptio | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   | n |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/networkz |   |   |   |   |
|   |   |   |   |   |   |   | one/{#Network |   |   |   |   |
|   |   |   |   |   |   |   | ZoneId} |   |   |   |   |
|   | eiam:EnableDo mainProxyToke |   |   |   |   |   | *DomainProxyTok en acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | roxyToke | EnableDomainP roxyToken | leDomainP |   |   |   |   |   |   |   |
|   |   |   |   |   | update |   | stance/{#Instan |   | N/A | N/A |   |
|   | n |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/domain/{ |   |   |   |   |
|   |   |   |   |   |   |   | #DomainId}/do |   |   |   |   |
|   |   |   |   |   |   |   | mainproxytoken |   |   |   |   |
|   |   |   |   |   |   |   | /{#DomainProx |   |   |   |   |
|   |   |   |   |   |   |   | yTokenId} |   |   |   |   |
|   | eiam:DeleteFe deratedCreden |   | DeleteFederate |   |   |   | *FederatedCreden tialProvider acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | eFederate |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | dCreden | dCredentialProv |   |   |   |   |   |   |   |   |
|   |   |   |   |   | delete |   | stance/{#Instan |   | N/A | N/A |   |
|   | tialProvider |   |   |   |   |   |   |   |   |   |   |
|   |   |   | ider |   |   |   | ceId}/federated |   |   |   |   |
|   |   |   |   |   |   |   | credentialprovi |   |   |   |   |
|   |   |   |   |   |   |   | der/{#Federate |   |   |   |   |
|   |   |   |   |   |   |   | dCredentialProv |   |   |   |   |
|   |   |   |   |   |   |   | iderId} |   |   |   |   |

|   |   |   |   |   |   |   | *OrganizationalUn it acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/organizati |   |   |   |   |
|   | eiam:UpdateOr |   | UpdateOrganiza |   |   |   | onalunit/{#Org |   |   |   |   |
|   | ganizationalUni |   | tionalUnit |   | update |   | anizationalUnitI |   |   |   |   |
|   | t |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | d} |   |   |   |   |
|   | eiam:UpdateNe tworkZone |   | UpdateNetwork |   |   |   | *NetworkZone acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | teNetwork |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | one | Zone |   | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/networkz |   |   |   |   |
|   |   |   |   |   |   |   | one/{#Network |   |   |   |   |
|   |   |   |   |   |   |   | ZoneId} |   |   |   |   |
|   |   |   |   |   |   |   | *User acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/user/{#Us |   |   |   |   |
|   |   |   |   |   |   |   | erId} |   |   |   |   |
|   | eiam:AddApplic ationAccountTo User |   | AddApplication AccountToUser |   | create |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id}/applicationa |   |   |   |   |
|   |   |   |   |   |   |   | ccount/* |   |   |   |   |

|   |   |   |   |   |   |   | *ApplicationFeder atedCredential acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   | eiam:EnableAp |   |   |   |   |   |   |   |   |   |   |
|   |   |   | EnableApplicati |   |   |   | ceId}/applicatio |   |   |   |   |
|   | plicationFedera |   | onFederatedCre |   | update |   | n/{#Application |   | N/A | N/A |   |
|   | tedCredential |   | dential |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | Id}/applicationf |   |   |   |   |
|   |   |   |   |   |   |   | ederatedcreden |   |   |   |   |
|   |   |   |   |   |   |   | tial/{#Applicati |   |   |   |   |
|   |   |   |   |   |   |   | onFederatedCre |   |   |   |   |
|   |   |   |   |   |   |   | dentialId} |   |   |   |   |
|   | eiam:GetPassw ordComplexity Configuration |   | GetPasswordCo mplexityConfig uration |   | get |   | *Instance acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   | get | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   |   |   | N/A | N/A |   |
|   |   |   |   | n |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId} |   |   |   |   |
|   | eiam:UpdateUs erPassword |   | UpdateUserPass word |   |   |   | *User acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | teUserPass | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/user/{#Us |   |   |   |   |
|   |   |   |   |   |   |   | erId} |   |   |   |   |
|   | eiam:ObtainDo mainProxyToke |   |   |   |   |   | *DomainProxyTok en acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | roxyToke | ObtainDomainP roxyToken | nDomainP |   |   |   |   |   |   |   |
|   |   |   |   |   | get |   | stance/{#Instan |   | N/A | N/A |   |
|   | n |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/domain/{ |   |   |   |   |
|   |   |   |   |   |   |   | #DomainId}/do |   |   |   |   |
|   |   |   |   |   |   |   | mainproxytoken |   |   |   |   |
|   |   |   |   |   |   |   | /{#DomainProx |   |   |   |   |
|   |   |   |   |   |   |   | yTokenId} |   |   |   |   |
|   | eiam:ListNetwo rkAccessEndpoi ntAvailableRegi ons |   | ListNetworkAcc essEndpointAva ilableRegions |   | get |   | *All resources * |   | N/A | N/A |   |

|   | eiam:DeleteGr oup |   | DeleteGroup |   |   |   | *Group acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | eGroup | delete |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/group/{# |   |   |   |   |
|   |   |   |   |   |   |   | GroupId} |   |   |   |   |
|   | eiam:CreateDo mainProxyToke n |   | CreateDomainP |   |   |   | *DomainProxyTok en acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | eDomainP |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | roxyToke | roxyToken | oken | create |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/domain/{ |   |   |   |   |
|   |   |   |   |   |   |   | #DomainId}/do |   |   |   |   |
|   |   |   |   |   |   |   | mainproxytoken |   |   |   |   |
|   |   |   |   |   |   |   | /* |   |   |   |   |
|   | eiam:ListApplic ationsForOrgan izationalUnit |   | ListApplications |   |   |   | *OrganizationalUn it acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | pplications |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | ForOrgan alUnit | ForOrganization alUnit | ganization | list |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/organizati |   |   |   |   |
|   |   |   |   |   |   |   | onalunit/{#Org |   |   |   |   |
|   |   |   |   |   |   |   | anizationalUnitI |   |   |   |   |
|   |   |   |   |   |   |   | d} |   |   |   |   |
|   | eiam:GetPassw ordHistoryConfi guration |   | GetPasswordHis toryConfiguratio n |   | get |   | *Instance acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   | get | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId} |   |   |   |   |
|   | eiam:GetGroup |   | GetGroup |   |   |   | *Group acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | roup | get |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/group/{# |   |   |   |   |
|   |   |   |   |   |   |   | GroupId} |   |   |   |   |

|   | eiam:UpdateUs erDescription |   | UpdateUserDes cription |   |   |   | *User acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | on | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/user/{#Us |   |   |   |   |
|   |   |   |   |   |   |   | erId} |   |   |   |   |
|   | eiam:UpdateGr oupDescription |   |   |   |   |   | *Group acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | pdateGr scription | UpdateGroupDe scription | teGroupDe |   |   |   |   |   |   |   |
|   |   |   |   |   | update |   | stance/{#Instan |   | N/A | N/A |   |
|   |   |   |   |   |   |   | ceId}/group/{# |   |   |   |   |
|   |   |   |   |   |   |   | GroupId} |   |   |   |   |
|   | eiam:GetNetwo rkAccessEndpoi nt |   | GetNetworkAcc |   |   |   | *NetworkAccessE ndpoint acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | etworkAcc |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | ssEndpoi | essEndpoint |   | get |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/networkac |   |   |   |   |
|   |   |   |   |   |   |   | cessendpoint/{ |   |   |   |   |
|   |   |   |   |   |   |   | #NetworkAcces |   |   |   |   |
|   |   |   |   |   |   |   | sEndpointId} |   |   |   |   |
|   | eiam:DeleteAp saraEiamInstan ce |   | DeleteApsaraEi amInstance |   |   |   | *Instance acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | eApsaraEi stance | delete |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId} |   |   |   |   |
|   | eiam:CreateAp saraEiamInstan ce |   | CreateApsaraEi amInstance |   | create |   | *Instance acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   | create | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/* |   |   |   |   |

|   | eiam:EnableAp plicationApiInv oke |   | EnableApplicati |   |   |   | *Application acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | leApplicati | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   | onApiInvoke |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |
|   | eiam:DisableFe deratedCreden |   | DisableFederate |   |   |   | *FederatedCreden tialProvider acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | leFederate |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | dCreden | dCredentialProv |   |   |   |   |   |   |   |   |
|   |   |   |   |   | update |   | stance/{#Instan |   | N/A | N/A |   |
|   | tialProvider |   |   |   |   |   |   |   |   |   |   |
|   |   |   | ider |   |   |   | ceId}/federated |   |   |   |   |
|   |   |   |   |   |   |   | credentialprovi |   |   |   |   |
|   |   |   |   |   |   |   | der/{#Federate |   |   |   |   |
|   |   |   |   |   |   |   | dCredentialProv |   |   |   |   |
|   |   |   |   |   |   |   | iderId} |   |   |   |   |
|   | eiam:ListApplic |   |   |   |   |   | *ApplicationToken acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | istApplic | ListApplicationT okens | pplicationT |   |   |   |   |   |   |   |
|   |   |   |   |   | list |   | stance/{#Instan |   | N/A | N/A |   |
|   | ationTokens | okens |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id}/applicationt |   |   |   |   |
|   |   |   |   |   |   |   | oken/* |   |   |   |   |
|   | eiam:ListSynch ronizationJobs |   | ListSynchroniza tionJobs |   |   |   | *SynchronizationJ ob acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | bs | list | list |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/synchroni |   |   |   |   |
|   |   |   |   |   |   |   | zationjob/* |   |   |   |   |

|   | eiam:DisableCo nditionalAccess Policy |   | DisableConditio |   |   |   | *ConditionalAcces sPolicy acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | leConditio |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | alAccess | nalAccessPolicy |   | update |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/condition |   |   |   |   |
|   |   |   |   |   |   |   | alaccesspolicy/{ |   |   |   |   |
|   |   |   |   |   |   |   | #ConditionalAcc |   |   |   |   |
|   |   |   |   |   |   |   | essPolicyId} |   |   |   |   |
|   | eiam:DeleteOr ganizationalUni t |   | DeleteOrganizat |   |   |   | *OrganizationalUn it acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | eOrganizat |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | tionalUni | ionalUnit |   | delete |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/organizati |   |   |   |   |
|   |   |   |   |   |   |   | onalunit/{#Org |   |   |   |   |
|   |   |   |   |   |   |   | anizationalUnitI |   |   |   |   |
|   |   |   |   |   |   |   | d} |   |   |   |   |
|   | eiam:ListApsar aEiamInstances |   | ListApsaraEiamI nstances |   | get |   | *Instance acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   | get | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/* |   |   |   |   |
|   | eiam:DeleteAp plicationClientS |   |   |   |   |   | *Secret acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | onClientS | DeleteApplicati onClientSecret | eApplicati |   |   |   |   |   |   |   |
|   |   |   |   |   | delete |   | stance/{#Instan |   | N/A | N/A |   |
|   | ecret |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id}/secret/{#Se |   |   |   |   |
|   |   |   |   |   |   |   | cretId} |   |   |   |   |

|   | eiam:ListOrgan izationalUnits |   | ListOrganization alUnits |   |   |   | *OrganizationalUn it acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | ts | list | list |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/organizati |   |   |   |   |
|   |   |   |   |   |   |   | onalunit/* |   |   |   |   |
|   | eiam:GetCondit ionalAccessPoli cy |   | GetConditionalA |   |   |   | *ConditionalAcces sPolicy acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | onditionalA |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | ccessPoli | ccessPolicy |   | get |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/condition |   |   |   |   |
|   |   |   |   |   |   |   | alaccesspolicy/{ |   |   |   |   |
|   |   |   |   |   |   |   | #ConditionalAcc |   |   |   |   |
|   |   |   |   |   |   |   | essPolicyId} |   |   |   |   |
|   | eiam:CreateAp plicationFedera |   | CreateApplicati |   |   |   | *ApplicationFeder atedCredential acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | eApplicati |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | onFedera | onFederatedCre |   |   |   |   |   |   |   |   |
|   |   |   |   |   | create |   | stance/{#Instan |   | N/A | N/A |   |
|   | tedCredential |   |   |   |   |   |   |   |   |   |   |
|   |   |   | dential |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id}/applicationf |   |   |   |   |
|   |   |   |   |   |   |   | ederatedcreden |   |   |   |   |
|   |   |   |   |   |   |   | tial/* |   |   |   |   |
|   | eiam:EnableIde ntityProviderUd Pull |   | EnableIdentityP |   |   |   | *IdentityProvider acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | leIdentityP | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   | roviderUdPull |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/identitypr |   |   |   |   |
|   |   |   |   |   |   |   | ovider/{#Identi |   |   |   |   |
|   |   |   |   |   |   |   | tyProviderId} |   |   |   |   |

|   | eiam:ListApplic ationFederated |   | ListApplicationF |   |   |   | *ApplicationFeder atedCredential acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | pplicationF |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | ederated | ederatedCreden |   |   |   |   |   |   |   |   |
|   |   |   |   |   | list |   | stance/{#Instan |   | N/A | N/A |   |
|   | Credentials |   |   |   |   |   |   |   |   |   |   |
|   |   |   | tials |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id}/applicationf |   |   |   |   |
|   |   |   |   |   |   |   | ederatedcreden |   |   |   |   |
|   |   |   |   |   |   |   | tial/* |   |   |   |   |
|   | eiam:UpdateCo nditionalAccess Policy |   | UpdateConditio |   |   |   | *ConditionalAcces sPolicy acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | teConditio |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | alAccess | nalAccessPolicy |   | update |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/condition |   |   |   |   |
|   |   |   |   |   |   |   | alaccesspolicy/{ |   |   |   |   |
|   |   |   |   |   |   |   | #ConditionalAcc |   |   |   |   |
|   |   |   |   |   |   |   | essPolicyId} |   |   |   |   |
|   | eiam:DisableAp plicationSso |   | DisableApplicati |   |   |   | *Application acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | leApplicati | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | onSso | onSso |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |
|   | eiam:CreateCo nditionalAccess Policy |   | CreateCondition |   |   |   | *ConditionalAcces sPolicy acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | eCondition | create |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   | alAccessPolicy | essPolicy |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/condition |   |   |   |   |
|   |   |   |   |   |   |   | alaccesspolicy/* |   |   |   |   |

|   | eiam:DeleteOr ganizationalUni |   | DeleteOrganizat |   |   |   | *OrganizationalUn it acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | eOrganizat |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | tionalUni | ionalUnitChildre |   |   |   |   |   |   |   |   |
|   |   |   |   |   | delete |   | stance/{#Instan |   | N/A | N/A |   |
|   | tChildren |   |   |   |   |   |   |   |   |   |   |
|   |   |   | n |   |   |   | ceId}/organizati |   |   |   |   |
|   |   |   |   |   |   |   | onalunit/{#Org |   |   |   |   |
|   |   |   |   |   |   |   | anizationalUnitI |   |   |   |   |
|   |   |   |   |   |   |   | d} |   |   |   |   |
|   | eiam:GetApplic ationGrantScop e |   | GetApplicationG |   |   |   | *Application acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | pplicationG | get |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   | rantScope |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |
|   | eiam:ListOrgan izationalUnitsF orApplication |   | ListOrganization alUnitsForApplic |   |   |   | *Application acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | rganization tsForApplic | list |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | ication | ation |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |
|   | eiam:GetNetwo rkZone |   | GetNetworkZon |   |   |   | *NetworkZone acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | etworkZon | get |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | e | e |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/networkz |   |   |   |   |
|   |   |   |   |   |   |   | one/{#Network |   |   |   |   |
|   |   |   |   |   |   |   | ZoneId} |   |   |   |   |

|   |   | eiam:UpdateBr and |   |   | UpdateBrand |   |   |   | *Brand acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   | teBrand | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   |   |   | ceId}/brand/{# |   |   |   |   |
|   |   |   |   |   |   |   |   |   | BrandId} |   |   |   |   |
|   |   | eiam:GetApplic ationTemplate |   |   | GetApplicationT emplate |   |   |   | *ApplicationTempl ate acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   | pplicationT ate | get |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   | {#accountId}:a |   | N/A | N/A |   |
|   |   |   |   |   |   |   |   |   | pplicationtempl |   |   |   |   |
|   |   |   |   |   |   |   |   |   | ate/{#Applicati |   |   |   |   |
|   |   |   |   |   |   |   |   |   | onTemplateId} |   |   |   |   |
|   |   | eiam:ListBrand s |   |   | ListBrands |   | list |   | *Brand acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   |   | list | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   |   |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   |   |   | ceId}/brand/* |   |   |   |   |

|   |   |   |   |   |   |   | *Application acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |
|   | eiam:ListCondit ionalAccessPoli ciesForApplicat ion |   | ListConditionalA ccessPoliciesFor Application |   | list |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   | list | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   |   |   | N/A | N/A |   |
|   |   |   |   | cation |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/condition |   |   |   |   |
|   |   |   |   |   |   |   | alaccesspolicy/* |   |   |   |   |
|   | eiam:UpdateFe deratedCreden tialProviderDes |   | UpdateFederate |   |   |   | *FederatedCreden tialProvider acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | teFederate |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | dCreden viderDes | dCredentialProv |   |   |   |   |   |   |   |   |
|   |   |   |   |   | update |   | stance/{#Instan |   | N/A | N/A |   |
|   | cription |   |   |   |   |   |   |   |   |   |   |
|   |   |   | iderDescription |   |   |   | ceId}/federated |   |   |   |   |
|   |   |   |   |   |   |   | credentialprovi |   |   |   |   |
|   |   |   |   |   |   |   | der/{#Federate |   |   |   |   |
|   |   |   |   |   |   |   | dCredentialProv |   |   |   |   |
|   |   |   |   |   |   |   | iderId} |   |   |   |   |
|   | eiam:DeleteDo mainProxyToke |   |   |   |   |   | *DomainProxyTok en acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | roxyToke | DeleteDomainPr oxyToken | eDomainPr |   |   |   |   |   |   |   |
|   |   |   |   |   | delete |   | stance/{#Instan |   | N/A | N/A |   |
|   | n |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/domain/{ |   |   |   |   |
|   |   |   |   |   |   |   | #DomainId}/do |   |   |   |   |
|   |   |   |   |   |   |   | mainproxytoken |   |   |   |   |
|   |   |   |   |   |   |   | /{#DomainProx |   |   |   |   |
|   |   |   |   |   |   |   | yTokenId} |   |   |   |   |

|   |   |   |   |   |   |   | *NetworkZone acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/networkz |   |   |   |   |
|   |   |   |   |   |   |   | one/{#Network |   |   |   |   |
|   | eiam:ListApplic |   | ListApplications |   |   |   |   |   |   |   |   |
|   | ationsForNetwo |   | ForNetworkZon |   | list |   | ZoneId} |   |   |   |   |
|   | rkZone |   | e |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/* |   |   |   |   |
|   | eiam:RemoveU sersFromGroup |   | RemoveUsersFr omGroup |   |   |   | *Group acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | veUsersFr oup | delete |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/group/{# |   |   |   |   |
|   |   |   |   |   |   |   | GroupId} |   |   |   |   |
|   | eiam:ListNetwo |   |   |   |   |   | *NetworkAccessP ath acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | istNetwo | ListNetworkAcc |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   | rkAccessPaths |   |   |   | list |   |   |   | N/A | N/A |   |
|   |   |   | essPaths |   |   |   | ceId}/networkac |   |   |   |   |
|   |   |   |   |   |   |   | cessendpoint/{ |   |   |   |   |
|   |   |   |   |   |   |   | #NetworkAcces |   |   |   |   |
|   |   |   |   |   |   |   | sEndpointId}/ne |   |   |   |   |
|   |   |   |   |   |   |   | tworkaccesspat |   |   |   |   |
|   |   |   |   |   |   |   | h/* |   |   |   |   |

|   | eiam:ListOrgan |   |   |   |   |   | *OrganizationalUn it acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | istOrgan |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   | izationalUnitPar |   |   |   |   |   |   |   |   |   |   |
|   |   |   | ListOrganization |   | get |   | ceId}/organizati |   | N/A | N/A |   |
|   |   |   | alUnitParents |   |   |   |   |   |   |   |   |
|   | ents |   |   |   |   |   | onalunit/{#Org |   |   |   |   |
|   |   |   |   |   |   |   | anizationalUnitI |   |   |   |   |
|   |   |   |   |   |   |   | d} |   |   |   |   |
|   | eiam:GetApplic |   |   |   |   |   | *ApplicationFeder atedCredential acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | etApplic | GetApplicationF |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   | ationFederated |   |   |   |   |   |   |   |   |   |   |
|   |   |   | ederatedCreden |   | get |   | ceId}/applicatio |   | N/A | N/A |   |
|   | Credential |   | tial |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id}/applicationf |   |   |   |   |
|   |   |   |   |   |   |   | ederatedcreden |   |   |   |   |
|   |   |   |   |   |   |   | tial/{#Applicati |   |   |   |   |
|   |   |   |   |   |   |   | onFederatedCre |   |   |   |   |
|   |   |   |   |   |   |   | dentialId} |   |   |   |   |
|   | eiam:SetApplic ationGrantScop e |   | SetApplicationG |   |   |   | *Application acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | plicationG | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   | rantScope |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |

|   | eiam:ListApplic ationsForNetwo rkAccessEndpoi |   | ListApplications |   |   |   | *NetworkAccessE ndpoint acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | pplications |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | ssEndpoi | ForNetworkAcce ssEndpoint | etworkAcce | get |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   | nt |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/networkac |   |   |   |   |
|   |   |   |   |   |   |   | cessendpoint/{ |   |   |   |   |
|   |   |   |   |   |   |   | #NetworkAcces |   |   |   |   |
|   |   |   |   |   |   |   | sEndpointId} |   |   |   |   |
|   | eiam:DeleteAp |   |   |   |   |   | *ApplicationToken acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | eleteAp | DeleteApplicati |   |   |   |   |   |   |   |   |
|   |   |   |   |   | delete |   | stance/{#Instan |   | N/A | N/A |   |
|   | plicationToken | onToken | onToken |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id}/applicationt |   |   |   |   |
|   |   |   |   |   |   |   | oken/{#Applica |   |   |   |   |
|   |   |   |   |   |   |   | tionTokenId} |   |   |   |   |
|   | eiam:ListNetwo rkAccessEndpoi ntAvailableZon es |   | ListNetworkAcc essEndpointAva ilableZones |   | get |   | *All resources * |   | N/A | N/A |   |
|   | eiam:EnableInit DomainAutoRe direct |   | EnableInitDoma inAutoRedirect |   |   |   | *Domain acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | leInitDoma oRedirect | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/domain/* |   |   |   |   |

|   |   |   |   |   |   |   | *Brand acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/brand/{# |   |   |   |   |
|   |   |   |   |   |   |   | BrandId} |   |   |   |   |
|   | eiam:SetLoginR edirectApplicati onForBrand |   | SetLoginRedirec tApplicationFor Brand |   | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   | update | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   |   |   | N/A | N/A |   |
|   |   |   |   | d |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |
|   | eiam:AddUsers ToGroup |   | AddUsersToGro up |   |   |   | *Group acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   | create |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/group/{# |   |   |   |   |
|   |   |   |   |   |   |   | GroupId} |   |   |   |   |
|   | eiam:SetApplic |   |   |   |   |   | *Application acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | etApplic | SetApplicationP |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   | ationProvisioni |   |   |   |   |   |   |   |   |   |   |
|   |   |   | rovisioningConfi |   | update |   | ceId}/applicatio |   | N/A | N/ |   |
|   | ngConfig |   | g |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |

|   |   |   |   |   |   |   | *OrganizationalUn it acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/organizati |   |   |   |   |
|   |   |   |   |   |   |   | onalunit/{#Org |   |   |   |   |
|   | eiam:GetOrgan |   | GetOrganizatio |   | get |   | anizationalUnitI |   |   |   |   |
|   | izationalUnit |   | nalUnit |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | d} |   |   |   |   |
|   | eiam:DisableAp plicationClientS |   |   |   |   |   | *Secret acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | onClientS | DisableApplicati onClientSecret | leApplicati |   |   |   |   |   |   |   |
|   |   |   |   |   | update |   | stance/{#Instan |   | N/A | N/A |   |
|   | ecret |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id}/secret/{#Se |   |   |   |   |
|   |   |   |   |   |   |   | cretId} |   |   |   |   |
|   | eiam:DeleteNet workAccessEnd point |   | DeleteNetworkA |   |   |   | *NetworkAccessE ndpoint acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | eNetworkA |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | ccessEnd | ccessEndpoint |   | delete |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/networkac |   |   |   |   |
|   |   |   |   |   |   |   | cessendpoint/{ |   |   |   |   |
|   |   |   |   |   |   |   | #NetworkAcces |   |   |   |   |
|   |   |   |   |   |   |   | sEndpointId} |   |   |   |   |
|   | eiam:CreateGr oup |   | CreateGroup |   | create |   | *Group acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   | create | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/group/* |   |   |   |   |

|   | eiam:UpdateAp plicationToken |   |   |   |   |   | *ApplicationToken acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | pdateAp onToken | UpdateApplicati onTokenExpirati | teApplicati |   |   |   |   |   |   |   |
|   |   |   |   |   | update |   | stance/{#Instan |   | N/A | N/A |   |
|   | ExpirationTime |   |   |   |   |   |   |   |   |   |   |
|   |   |   | onTime |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id}/applicationt |   |   |   |   |
|   |   |   |   |   |   |   | oken/{#Applica |   |   |   |   |
|   |   |   |   |   |   |   | tionTokenId} |   |   |   |   |
|   |   |   |   |   |   |   | *ApplicationToken acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   | eiam:DisableAp |   | DisableApplicati |   |   |   |   |   |   |   |   |
|   | plicationToken |   | onToken |   | update |   | Id}/applicationt |   | N/A | N/A |   |
|   |   |   |   |   |   |   | oken/{#Applica |   |   |   |   |
|   |   |   |   |   |   |   | tionTokenId} |   |   |   |   |
|   |   |   |   |   |   |   | *ConditionalAcces sPolicy acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/condition |   |   | N/A |   |
|   | eiam:ListCondit |   |   |   |   |   | alaccesspolicy/* |   | N/A |   |   |
|   |   |   | ListConditionalA |   |   |   |   |   |   |   |   |
|   | ionalAccessPoli |   | ccessPoliciesFor |   | list |   |   |   |   |   |   |
|   | ciesForNetwork Zone |   | NetworkZone |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/networkz |   |   |   |   |
|   |   |   |   |   |   |   | one/{#Network |   |   |   |   |
|   |   |   |   |   |   |   | ZoneId} |   |   |   |   |

|   | eiam:CreateBra nd |   | CreateBrand |   | create |   | *Brand acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   | create | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/brand/* |   |   |   |   |
|   | eiam:UpdateDo |   |   |   |   |   | *Domain acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | pdateDo | UpdateDomain |   |   |   |   |   |   |   |   |
|   |   |   |   |   | update |   | stance/{#Instan |   | N/A | N/A |   |
|   | mainBrand | rand | Brand |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/domain/{ |   |   |   |   |
|   |   |   |   |   |   |   | #DomainId} |   |   |   |   |
|   | eiam:DisableAp plication |   | DisableApplicati |   |   |   | *Application acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | leApplicati | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | on | on |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |
|   | eiam:EnableAp |   |   |   |   |   | *ApplicationToken acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | nableAp | EnableApplicati |   |   |   |   |   |   |   |   |
|   |   |   |   |   | update |   | stance/{#Instan |   | N/A | N/A |   |
|   | plicationToken |   |   |   |   |   |   |   |   |   |   |
|   |   |   | onToken |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id}/applicationt |   |   |   |   |
|   |   |   |   |   |   |   | oken/{#Applica |   |   |   |   |
|   |   |   |   |   |   |   | tionTokenId} |   |   |   |   |
|   | eiam:GetDomai n |   | GetDomain |   |   |   | *Domain acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | omain | get |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/domain/{ |   |   |   |   |
|   |   |   |   |   |   |   | #DomainId} |   |   |   |   |

|   | eiam:GetLogin RedirectApplica tionForBrand |   | GetLoginRedire ctApplicationFor |   |   |   | *Brand acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | licationFor | get |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | rBrand | Brand |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/brand/{# |   |   |   |   |
|   |   |   |   |   |   |   | BrandId} |   |   |   |   |
|   | eiam:DisableD omainProxyTok |   |   |   |   |   | *DomainProxyTok en acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | ProxyTok | DisableDomain ProxyToken | leDomain |   |   |   |   |   |   |   |
|   |   |   |   |   | update |   | stance/{#Instan |   | N/A | N/A |   |
|   | en |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/domain/{ |   |   |   |   |
|   |   |   |   |   |   |   | #DomainId}/do |   |   |   |   |
|   |   |   |   |   |   |   | mainproxytoken |   |   |   |   |
|   |   |   |   |   |   |   | /{#DomainProx |   |   |   |   |
|   |   |   |   |   |   |   | yTokenId} |   |   |   |   |
|   | eiam:ListGroup sForApplication |   |   |   |   |   | *Application acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | istGroup plication | ListGroupsForA pplication | roupsForA |   |   |   |   |   |   |   |
|   |   |   |   |   | list |   | stance/{#Instan |   | N/A | N/A |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |

|   |   |   |   |   |   |   | *ApplicationFeder atedCredential acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   | eiam:UpdateAp |   | UpdateApplicati |   |   |   | Id}/applicationf |   |   |   |   |
|   | plicationFedera |   | onFederatedCre |   | update |   |   |   | N/A | N/A |   |
|   | tedCredential |   | dential |   |   |   | ederatedcreden |   |   |   |   |
|   |   |   |   |   |   |   | tial/{#Applicati |   |   |   |   |
|   |   |   |   |   |   |   | onFederatedCre |   |   |   |   |
|   |   |   |   |   |   |   | dentialId} |   |   |   |   |
|   | eiam:GetApplic ationProvisioni ngScope |   | GetApplicationP rovisioningScop |   |   |   | *Application acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | pplicationP oningScop | get |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | rovisioni pe | e |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |
|   | eiam:DisableIni tDomainAutoR edirect |   | DisableInitDom ainAutoRedirect |   |   |   | *Domain acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | leInitDom toRedirect | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | t |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/domain/* |   |   |   |   |
|   | eiam:DeleteBra nd |   | DeleteBrand |   |   |   | *Brand acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | eBrand | delete |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/brand/{# |   |   |   |   |
|   |   |   |   |   |   |   | BrandId} |   |   |   |   |

|   | eiam:UpdateNe tworkAccessEn dpointName |   | UpdateNetwork |   |   |   | *NetworkAccessE ndpoint acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | teNetwork |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | ccessEn Name | AccessEndpoint Name | ssEndpoint | update |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/networkac |   |   |   |   |
|   |   |   |   |   |   |   | cessendpoint/{ |   |   |   |   |
|   |   |   |   |   |   |   | #NetworkAcces |   |   |   |   |
|   |   |   |   |   |   |   | sEndpointId} |   |   |   |   |
|   | eiam:ObtainAp plicationClientS |   |   |   |   |   | *Secret acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | onClientS | ObtainApplicati onClientSecret | nApplicati |   |   |   |   |   |   |   |
|   |   |   |   |   | get |   | stance/{#Instan |   | N/A | N/A |   |
|   | ecret |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id}/secret/{#Se |   |   |   |   |
|   |   |   |   |   |   |   | cretId} |   |   |   |   |
|   |   |   |   |   |   |   | *IdentityProvider acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   | eiam:UpdateId |   |   |   |   |   |   |   |   |   |   |
|   |   |   | UpdateIdentityP |   | update |   | ceId}/identitypr |   | N/A | N/A |   |
|   | entityProvider |   | rovider |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | ovider/{#Identi |   |   |   |   |
|   |   |   |   |   |   |   | tyProviderId} |   |   |   |   |
|   | eiam:SetUserPr imaryOrganizat ionalUnit |   | SetUserPrimary OrganizationalU |   |   |   | *User acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | nizationalU | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | nit | nit |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/user/{#Us |   |   |   |   |
|   |   |   |   |   |   |   | erId} |   |   |   |   |

|   | eiam:EnableAp plication |   | EnableApplicati |   |   |   | *Application acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | leApplicati | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | on | on |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |
|   | eiam:GetApplic ationSsoConfig |   | GetApplicationS |   |   |   | *Application acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | pplicationS | get |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | soConfig | soConfig |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |
|   | eiam:EnableBr and |   | EnableBrand |   |   |   | *Brand acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | leBrand | update |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/brand/{# |   |   |   |   |
|   |   |   |   |   |   |   | BrandId} |   |   |   |   |
|   | eiam:GetInstan ceLicense |   | GetInstanceLice nse |   | get |   | *Instance acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   | get | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId} |   |   |   |   |
|   | eiam:ListNetwo rkAccessEndpoi nts |   | ListNetworkAcc essEndpoints |   |   |   | *NetworkAccessE ndpoint acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | etworkAcc dpoints | get |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/networkac |   |   |   |   |
|   |   |   |   |   |   |   | cessendpoint/* |   |   |   |   |

|   | eiam:ListFeder atedCredential Providers |   | ListFederatedCr edentialProvide |   |   |   | *FederatedCreden tialProvider acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | tialProvide | list |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | ers | rs |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/federated |   |   |   |   |
|   |   |   |   |   |   |   | credentialprovi |   |   |   |   |
|   |   |   |   |   |   |   | der/* |   |   |   |   |
|   | eiam:EnableUs er |   | EnableUser |   |   |   | *User acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | leUser | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/user/{#Us |   |   |   |   |
|   |   |   |   |   |   |   | erId} |   |   |   |   |
|   | eiam:DisableUs er |   |   |   |   |   | *User acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   | N/A |   |
|   |   |   | DisableUser | leUser | update |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/user/{#Us |   |   |   |   |
|   |   |   |   |   |   |   | erId} |   |   |   |   |
|   | eiam:CreateNe tworkZone |   | CreateNetwork Zone |   |   |   | *NetworkZone acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | eNetwork | create |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/networkz |   |   |   |   |
|   |   |   |   |   |   |   | one/* |   |   |   |   |
|   | eiam:DeleteAp plication |   | DeleteApplicati |   |   |   | *Application acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | eApplicati | delete |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | on | on |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |

|   | eiam:GetBrand |   | GetBrand |   |   |   | *Brand acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | rand | get |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/brand/{# |   |   |   |   |
|   |   |   |   |   |   |   | BrandId} |   |   |   |   |
|   | eiam:DisableAp |   |   |   |   |   | *ApplicationFeder atedCredential acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | isableAp | DisableApplicati |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   | plicationFedera |   |   |   |   |   |   |   |   |   |   |
|   |   |   | onFederatedCre |   | update |   | ceId}/applicatio |   | N/A | N/A |   |
|   | tedCredential |   |   |   |   |   |   |   |   |   |   |
|   |   |   | dential |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id}/applicationf |   |   |   |   |
|   |   |   |   |   |   |   | ederatedcreden |   |   |   |   |
|   |   |   |   |   |   |   | tial/{#Applicati |   |   |   |   |
|   |   |   |   |   |   |   | onFederatedCre |   |   |   |   |
|   |   |   |   |   |   |   | dentialId} |   |   |   |   |
|   | eiam:ListIdentit yProviders |   | ListIdentityProvi ders |   |   |   | *IdentityProvider acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   | list |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/identitypr |   |   |   |   |
|   |   |   |   |   |   |   | ovider/* |   |   |   |   |
|   |   |   |   |   |   |   | *Application acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   | eiam:ListUsers |   | ListUsersForApp |   |   |   | n/{#Application |   |   |   |   |
|   | ForApplication |   | lication |   | list |   | Id} |   |   |   |   |

|   |   |   |   |   |   |   | *User acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/user/{#Us |   |   |   |   |
|   |   |   |   |   |   |   | erId} |   |   |   |   |
|   | eiam:RemoveA pplicationAcco untFromUser |   | RemoveApplicat ionAccountFrom User |   | delete |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   | delete | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id}/applicationa |   |   |   |   |
|   |   |   |   |   |   |   | ccount/{#Applic |   |   |   |   |
|   |   |   |   |   |   |   | ationAccountId} |   |   |   |   |
|   | eiam:ListUsers ForGroup |   | ListUsersForGro up |   |   |   | *Group acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | sersForGro | get |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/group/{# |   |   |   |   |
|   |   |   |   |   |   |   | GroupId} |   |   |   |   |
|   | eiam:SetIdentit yProviderUdPul lConfiguration |   | SetIdentityProvi derUdPullConfig |   |   |   | *IdentityProvider acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | entityProvi dPullConfig | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | uration | uration |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/identitypr |   |   |   |   |
|   |   |   |   |   |   |   | ovider/{#Identi |   |   |   |   |
|   |   |   |   |   |   |   | tyProviderId} |   |   |   |   |

|   | eiam:AddUserT oOrganizationa lUnits |   | AddUserToOrga nizationalUnits |   |   |   | *User acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | onalUnits | create |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/user/{#Us |   |   |   |   |
|   |   |   |   |   |   |   | erId} |   |   |   |   |
|   | eiam:CreateAp plication |   | CreateApplicati on |   |   |   | *Application acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | eApplicati | create |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/* |   |   |   |   |
|   | eiam:RunSynch ronizationJob |   | RunSynchroniza tionJob |   |   |   | *SynchronizationJ ob acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | b | create |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/synchroni |   |   |   |   |
|   |   |   |   |   |   |   | zationjob/* |   |   |   |   |
|   |   |   |   |   |   |   | *Application acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   | eiam:UpdateAp |   | UpdateApplicati |   |   |   | n/{#Application |   |   |   |   |
|   | plicationInfo |   | onInfo |   | update |   | Id} |   |   |   |   |

|   | eiam:UpdateCo nditionalAccess PolicyDescripti |   | UpdateConditio |   |   |   | *ConditionalAcces sPolicy acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | teConditio |   |   | {#accountId}:in |   |   |   |   |
|   |   | Descripti | nalAccessPolicy Description | cessPolicy | update |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   | on |   |   |   |   |   | ceId}/condition |   |   |   |   |
|   |   |   |   |   |   |   | alaccesspolicy/{ |   |   |   |   |
|   |   |   |   |   |   |   | #ConditionalAcc |   |   |   |   |
|   |   |   |   |   |   |   | essPolicyId} |   |   |   |   |
|   | eiam:SetApplic ationSsoConfig |   | SetApplicationS |   |   |   | *Application acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | plicationS | create |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | soConfig | soConfig |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |
|   | eiam:ListGroup sForUser |   | ListGroupsForUs er |   |   |   | *User acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | roupsForUs | get |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/user/{#Us |   |   |   |   |
|   |   |   |   |   |   |   | erId} |   |   |   |   |
|   | eiam:GetIdentit yProvider |   | GetIdentityProvi |   |   |   | *IdentityProvider acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | entityProvi | get |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | der | der |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/identitypr |   |   |   |   |
|   |   |   |   |   |   |   | ovider/{#Identi |   |   |   |   |
|   |   |   |   |   |   |   | tyProviderId} |   |   |   |   |

|   | eiam:ListUsers |   |   |   |   |   | *User acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | istUsers | ListUsers |   |   |   |   |   |   |   |   |
|   |   |   |   |   | list |   | stance/{#Instan |   | N/A |   |   |
|   |   |   |   |   |   |   | ceId}/user/* |   |   |   |   |
|   | eiam:ObtainAp |   |   |   |   |   | *ApplicationToken acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | btainAp | ObtainApplicati |   |   |   |   |   |   |   |   |
|   |   |   |   |   | get |   | stance/{#Instan |   | N/A | N/A |   |
|   | plicationToken |   |   |   |   |   |   |   |   |   |   |
|   |   |   | onToken |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id}/applicationt |   |   |   |   |
|   |   |   |   |   |   |   | oken/{#Applica |   |   |   |   |
|   |   |   |   |   |   |   | tionTokenId} |   |   |   |   |
|   | eiam:GetSynch ronizationJob |   | GetSynchroniza tionJob |   |   |   | *SynchronizationJ ob acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | ynchroniza b |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | tionJob |   |   | get |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/synchroni |   |   |   |   |
|   |   |   |   |   |   |   | zationjob/{#Syn |   |   |   |   |
|   |   |   |   |   |   |   | chronizationJobI |   |   |   |   |
|   |   |   |   |   |   |   | d} |   |   |   |   |
|   | eiam:SetApplic ationProvisioni ngScope |   | SetApplicationP rovisioningScop |   |   |   | *Application acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | oningScop | update |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | pe | e |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |

|   | eiam:DeleteAp |   |   |   |   |   | *ApplicationFeder atedCredential acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | eleteAp | DeleteApplicati |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   | plicationFedera |   |   |   |   |   |   |   |   |   |   |
|   |   |   | onFederatedCre |   | delete |   | ceId}/applicatio |   | N/A | N/A |   |
|   | tedCredential |   | dential |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id}/applicationf |   |   |   |   |
|   |   |   |   |   |   |   | ederatedcreden |   |   |   |   |
|   |   |   |   |   |   |   | tial/{#Applicati |   |   |   |   |
|   |   |   |   |   |   |   | onFederatedCre |   |   |   |   |
|   |   |   |   |   |   |   | dentialId} |   |   |   |   |
|   | eiam:DisableAp plicationProvisi oning |   | DisableApplicati |   |   |   | *Application acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | leApplicati | update |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   | onProvisioning |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |
|   | eiam:CreateUs er |   | CreateUser |   | create |   | *User acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   | create | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/user/* |   |   |   |   |
|   | eiam:SetPassw ordInitialization Configuration |   | SetPasswordInit ializationConfig |   |   |   | *Instance acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | tionConfig | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | uration | uration |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId} |   |   |   |   |
|   | eiam:ListApplic ationsForUser |   | ListApplications ForUser |   |   |   | *User acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | pplications er | list |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/user/{#Us |   |   |   |   |
|   |   |   |   |   |   |   | erId} |   |   |   |   |

|   | eiam:GetInstan ce |   | GetInstance |   | get |   | *Instance acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   | get | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId} |   |   |   |   |
|   | eiam:ListApplic ationFederated CredentialsForP rovider |   | ListApplicationF ederatedCreden |   |   |   | *ApplicationFeder atedCredential acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | pplicationF tedCreden | list |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   | tialsForProvider |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/*/applicationf |   |   |   |   |
|   |   |   |   |   |   |   | ederatedcreden |   |   |   |   |
|   |   |   |   |   |   |   | tial/* |   |   |   |   |
|   | eiam:DisableId entityProviderA uthn |   | DisableIdentityP |   |   |   | *IdentityProvider acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | leIdentityP | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   | roviderAuthn |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/identitypr |   |   |   |   |
|   |   |   |   |   |   |   | ovider/{#Identi |   |   |   |   |
|   |   |   |   |   |   |   | tyProviderId} |   |   |   |   |
|   | eiam:ListGroup s |   | ListGroups |   | list |   | *Group acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   | list | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/group/* |   |   |   |   |
|   | eiam:DeleteNet workZone |   | DeleteNetworkZ |   |   |   | *NetworkZone acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | eNetworkZ | delete |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | one | one |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/networkz |   |   |   |   |
|   |   |   |   |   |   |   | one/{#Network |   |   |   |   |
|   |   |   |   |   |   |   | ZoneId} |   |   |   |   |

|   | eiam:GetRootO rganizationalUn it |   | GetRootOrganiz ationalUnit |   | get |   | *Instance acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   | get | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   |   |   | N/A | N/A |   |
|   |   |   |   | alUnit |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId} |   |   |   |   |
|   | eiam:GetApplic ation |   | GetApplication |   |   |   | *Application acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | pplication | get |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |
|   | eiam:GetPassw ordExpirationC onfiguration |   | GetPasswordEx pirationConfigur ation |   | get |   | *Instance acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   | get | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId} |   |   |   |   |
|   | eiam:SetPassw ordHistoryConfi guration |   | SetPasswordHis toryConfiguratio n |   | get |   | *Instance acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   | get | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   |   |   | N/A | N/A |   |
|   |   |   |   | onfiguratio |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId} |   |   |   |   |
|   |   |   |   |   |   |   | *User acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   | eiam:GetUser |   |   |   |   |   |   |   |   |   |   |
|   |   |   | GetUser |   | get |   | ceId}/user/{#Us |   | N/A |   |   |
|   |   |   |   |   |   |   | erId} |   |   |   |   |

|   | eiam:ListNetwo rkZones |   | ListNetworkZon es |   |   |   | *NetworkZone acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | etworkZon | list |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/networkz |   |   |   |   |
|   |   |   |   |   |   |   | one/* |   |   |   |   |
|   | eiam:CreateDo main |   | CreateDomain |   |   |   | *Domain acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | eDomain | create |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/domain/* |   |   |   |   |
|   | eiam:SetPassw ordExpirationC onfiguration |   | SetPasswordEx pirationConfigur ation |   | update |   | *Instance acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   | update | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId} |   |   |   |   |
|   | eiam:SetPassw ordComplexity Configuration |   | SetPasswordCo mplexityConfig uration |   | update |   | *Instance acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   | update | {#regionId}: |   | N/A | N/A |   |
|   |   |   |   | n |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId} |   |   |   |   |
|   | eiam:UnlockUs er |   | UnlockUser |   |   |   | *User acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | kUser | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/user/{#Us |   |   |   |   |
|   |   |   |   |   |   |   | erId} |   |   |   |   |

|   | eiam:EnableAp plicationSso |   | EnableApplicati |   |   |   | *Application acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | leApplicati | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | onSso | onSso |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |
|   | eiam:CreateFe deratedCreden tialProvider |   | CreateFederate dCredentialProv |   |   |   | *FederatedCreden tialProvider acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | dentialProv | create |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | vider | ider |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/federated |   |   |   |   |
|   |   |   |   |   |   |   | credentialprovi |   |   |   |   |
|   |   |   |   |   |   |   | der/* |   |   |   |   |
|   | eiam:Authorize ApplicationToG roups |   | AuthorizeApplic |   |   |   | *Application acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | orizeApplic | create |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   | ationToGroups |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |
|   | eiam:UpdateOr ganizationalUni tDescription |   | UpdateOrganiza |   |   |   | *OrganizationalUn it acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | teOrganiza |   |   | {#accountId}:in |   |   |   |   |
|   |   | tionalUni iption | tionalUnitDescri ption | lUnitDescri | update |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/organizati |   |   |   |   |
|   |   |   |   |   |   |   | onalunit/{#Org |   |   |   |   |
|   |   |   |   |   |   |   | anizationalUnitI |   |   |   |   |
|   |   |   |   |   |   |   | d} |   |   |   |   |

|   |   |   |   |   |   |   | *ConditionalAcces sPolicy acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   | eiam:ListCondit ionalAccessPoli | istCondit |   |   |   |   |   |   |   |   |   |
|   |   |   | ListConditionalA |   | list |   | ceId}/condition |   | N/A | N/A |   |
|   | cies |   | ccessPolicies |   |   |   | alaccesspolicy/* |   |   |   |   |
|   |   |   |   |   |   |   | *Group acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   | eiam:ListApplic |   |   |   |   |   |   |   |   |   |   |
|   |   |   | ListApplications |   | get |   | ceId}/group/{# |   | N/A |   |   |
|   | ationsForGroup |   | ForGroup |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | GroupId} |   |   |   |   |
|   | eiam:CreateAp plicationToken |   | CreateApplicati |   |   |   | *ApplicationToken acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | eApplicati |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | onToken | onToken |   | create |   | stance/{#Instan |   | N/A | N/A |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id}/applicationt |   |   |   |   |
|   |   |   |   |   |   |   | oken/* |   |   |   |   |
|   | eiam:CreateOr ganizationalUni t |   | CreateOrganiza tionalUnit |   | create |   | *OrganizationalUn it acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   | create | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   |   |   | N/A | N/A |   |
|   |   |   |   | lUnit |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/organizati |   |   |   |   |
|   |   |   |   |   |   |   | onalunit/* |   |   |   |   |

|   | eiam:ListDomai nProxyTokens |   | ListDomainProx |   |   |   | *DomainProxyTok en acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | omainProx |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | Tokens | yTokens |   | list |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/domain/{ |   |   |   |   |
|   |   |   |   |   |   |   | #DomainId}/do |   |   |   |   |
|   |   |   |   |   |   |   | mainproxytoken |   |   |   |   |
|   |   |   |   |   |   |   | /* |   |   |   |   |
|   |   |   |   |   |   |   | *User acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/user/{#Us |   |   |   |   |
|   |   |   |   |   |   |   | erId} |   |   |   |   |
|   | eiam:ListApplic ationAccountsF orUser |   | ListApplicationA ccountsForUser |   | get |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id}/applicationa |   |   |   |   |
|   |   |   |   |   |   |   | ccount/* |   |   |   |   |
|   | eiam:EnableAp plicationProvisi oning |   | EnableApplicati |   |   |   | *Application acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | leApplicati | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   | onProvisioning |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |

|   | eiam:RevokeAp plicationFromG roups |   | RevokeApplicati |   |   |   | *Application acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | keApplicati | delete |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   | onFromGroups |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |
|   | eiam:ListIdentit yProvidersForN etworkAccessE |   | ListIdentityProvi |   |   |   | *NetworkAccessE ndpoint acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | entityProvi |   |   | {#accountId}:in |   |   |   |   |
|   |   | AccessE | dersForNetwork AccessEndpoint | orNetwork | get |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   | ndpoint |   |   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/networkac |   |   |   |   |
|   |   |   |   |   |   |   | cessendpoint/{ |   |   |   |   |
|   |   |   |   |   |   |   | #NetworkAcces |   |   |   |   |
|   |   |   |   |   |   |   | sEndpointId} |   |   |   |   |
|   | eiam:RevokeAp plicationFromU sers |   | RevokeApplicati |   |   |   | *Application acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | keApplicati |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | onFromU | onFromUsers |   | delete |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |
|   | eiam:ListApplic |   |   |   |   |   | *Application acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | istApplic | ListApplicationS |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   | ationSupported |   |   |   |   |   |   |   |   |   |   |
|   |   |   | upportedProvisi |   | list |   | ceId}/applicatio |   | N/A | N/ |   |
|   | ProvisionProtoc |   | onProtocolType |   |   |   | n/{#Application |   |   |   |   |
|   | olTypes |   | s |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |

|   | eiam:UpdateAp plicationAuthor izationType |   | UpdateApplicati onAuthorization |   |   |   | *Application acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | teApplicati thorization | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | Type | Type |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |
|   | eiam:EnableFe deratedCreden |   | EnableFederate |   |   |   | *FederatedCreden tialProvider acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | leFederate |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | dCreden | dCredentialProv |   |   |   |   |   |   |   |   |
|   |   |   |   |   | update |   | stance/{#Instan |   | N/A | N/A |   |
|   | tialProvider |   |   |   |   |   |   |   |   |   |   |
|   |   |   | ider |   |   |   | ceId}/federated |   |   |   |   |
|   |   |   |   |   |   |   | credentialprovi |   |   |   |   |
|   |   |   |   |   |   |   | der/{#Federate |   |   |   |   |
|   |   |   |   |   |   |   | dCredentialProv |   |   |   |   |
|   |   |   |   |   |   |   | iderId} |   |   |   |   |
|   | eiam:UpdateAp |   |   |   |   |   | *ApplicationFeder atedCredential acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   | pdateAp | UpdateApplicati |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   | plicationFedera tedCredentialD | onFedera | onFederatedCre |   |   |   |   |   |   |   |   |
|   |   |   | dentialDescripti |   | update |   | ceId}/applicatio |   | N/A | N/A |   |
|   | escription |   | on |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id}/applicationf |   |   |   |   |
|   |   |   |   |   |   |   | ederatedcreden |   |   |   |   |
|   |   |   |   |   |   |   | tial/{#Applicati |   |   |   |   |
|   |   |   |   |   |   |   | onFederatedCre |   |   |   |   |
|   |   |   |   |   |   |   | dentialId} |   |   |   |   |
|   | eiam:DeleteUs er |   |   |   |   |   | *User acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   | DeleteUser |   | delete |   | stance/{#Instan |   | N/A | N/A |   |
|   |   |   |   |   |   |   | ceId}/user/{#Us |   |   |   |   |
|   |   |   |   |   |   |   | erId} |   |   |   |   |

|   | eiam:GetApplic ationProvisioni ngConfig |   | GetApplicationP rovisioningConfi |   |   |   | *Application acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | pplicationP oningConfi | get |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | fig | g |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id} |   |   |   |   |
|   | eiam:UpdateAp plicationClientS ecretExpiration |   | UpdateApplicati |   |   |   | *Secret acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | teApplicati |   |   | {#accountId}:in |   |   |   |   |
|   |   | onClientS xpiration | onClientSecretE |   |   |   |   |   |   |   |   |
|   |   |   |   |   | update |   | stance/{#Instan |   | N/A | N/A |   |
|   | Time |   | xpirationTime |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id}/secret/{#Se |   |   |   |   |
|   |   |   |   |   |   |   | cretId} |   |   |   |   |
|   | eiam:ListApplic ationClientSecr ets |   | ListApplicationC |   |   |   | *Secret acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | pplicationC | list |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   | lientSecrets |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id}/secret/* |   |   |   |   |
|   | eiam:DeleteDo main |   | DeleteDomain |   |   |   | *Domain acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | eDomain | delete |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/domain/{ |   |   |   |   |
|   |   |   |   |   |   |   | #DomainId} |   |   |   |   |
|   | eiam:SetDefaul tDomain |   | SetDefaultDom ain |   |   |   | *Domain acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | efaultDom | update |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/domain/{ |   |   |   |   |
|   |   |   |   |   |   |   | #DomainId} |   |   |   |   |

|   | eiam:UpdateAp saraEiamInstan ceDescription |   | UpdateApsaraEi amInstanceDes cription |   | update |   | *Instance acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   | update | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   |   |   | N/A | N/A |   |
|   |   |   |   | on |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId} |   |   |   |   |
|   | eiam:UpdateAp saraEiamInstan ceQuota |   | UpdateApsaraEi amInstanceQuo ta |   | update |   | *Instance acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   | update | {#regionId}: |   |   |   |   |
|   |   |   |   |   |   |   |   |   | N/A | N/A |   |
|   |   |   |   |   |   |   | {#accountId}:in |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId} |   |   |   |   |
|   | eiam:CreateAp plicationClientS ecret |   | CreateApplicati |   |   |   | *Secret acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | eApplicati | create |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   | onClientSecret |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/{#Application |   |   |   |   |
|   |   |   |   |   |   |   | Id}/secret/* |   |   |   |   |
|   | eiam:ListApplic ations |   | ListApplications |   |   |   | *Application acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | pplications | list |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/applicatio |   |   |   |   |
|   |   |   |   |   |   |   | n/* |   |   |   |   |
|   | eiam:GetDomai nDnsChallenge |   | GetDomainDns Challenge |   |   |   | *Domain acs:eiam: |   |   |   |   |
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | omainDns enge | get |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/domain/* |   |   |   |   |

|   | eiam:ListCondit ionalAccessPoli ciesForUser |   | ListConditionalA ccessPoliciesFor |   |   |   | *ConditionalAcces sPolicy acs:eiam: |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   | acs:eiam: |   |   |   |
|   |   |   |   |   |   |   | {#regionId}: |   |   |   |   |
|   |   |   |   | PoliciesFor | list |   |   |   |   |   |   |
|   |   |   |   |   |   |   | {#accountId}:in |   | N/A | N/A |   |
|   |   | rUser | User |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   | stance/{#Instan |   |   |   |   |
|   |   |   |   |   |   |   | ceId}/condition |   |   |   |   |
|   |   |   |   |   |   |   | alaccesspolicy/* |   |   |   |   |

**Resource**

The following table lists the resources defined by placeholder-${productName}. Specify them in the `Resource` element of RAM policy statements to grant permissions for specific operations. They are uniquely identified by ARNs. Format: `acs:{#ramcode}:{#regionId}:`

```
{#accountId}:{#resourceType} :
```

`acs` : The initialism of Alibaba Cloud service, which indicates the public cloud of Alibaba Cloud. `{#ramcode}` : The code used in RAM to indicate an Alibaba Cloud service. `{#regionId}` : The . If the resource covers all regions, set it to an asterisk (*). `{#accountId}` : The ID of the Alibaba Cloud account. If the resource covers all Alibaba Cloud accounts, set it to an asterisk (*). `{#resourceType}` : The service-defined resource identifier. It supports a hierarchical structure, which is similar to a file path. If the statement covers global resources, set it to an asterisk (*).

| Resource type | ARN |
|---|---|
| FederatedCrede ntialProvider | acs:eiam:{#regionId}: {#accountId}:instance/{#InstanceId}/federatedcredentialprovider/{#Federated CredentialProviderId} acs:eiam:{#regionId}: {#accountId}:instance/{#InstanceId}/federatedcredentialprovider/* |
| Brand | acs:eiam:{#regionId}:{#accountId}:instance/{#InstanceId}/brand/{#BrandId} acs:eiam:{#regionId}:{#accountId}:instance/{#InstanceId}/brand/* |
| Application | acs:eiam:{#regionId}: {#accountId}:instance/{#InstanceId}/application/{#ApplicationId} acs:eiam:{#regionId}:{#accountId}:instance/{#InstanceId}/application/* |
| User | acs:eiam:{#regionId}:{#accountId}:instance/{#InstanceId}/user/{#UserId} acs:eiam:{#regionId}:{#accountId}:instance/{#InstanceId}/user/* |

| Domain | acs:eiam:{#regionId}:{#accountId}:instance/{#InstanceId}/domain/* acs:eiam:{#regionId}: {#accountId}:instance/{#InstanceId}/domain/{#DomainId} |
|---|---|
| IdentityProvider | acs:eiam:{#regionId}: {#accountId}:instance/{#InstanceId}/identityprovider/{#IdentityProviderId} acs:eiam:{#regionId}:{#accountId}:instance/{#InstanceId}/identityprovider/* |
| ApplicationAcco unt | acs:eiam:{#regionId}: {#accountId}:instance/{#InstanceId}/application/{#ApplicationId}/applicationa ccount/* acs:eiam:{#regionId}: {#accountId}:instance/{#InstanceId}/application/{#ApplicationId}/applicationa ccount/{#ApplicationAccountId} |
| AuthenticationS ource | acs:eiam:{#regionId}:{#accountId}:instance/{#InstanceId} |
| Instance | acs:eiam:{#regionId}:{#accountId}:instance/{#InstanceId} acs:eiam:{#regionId}:{#accountId}:instance/* |
| NetworkAccessE ndpoint | acs:eiam:{#regionId}: {#accountId}:instance/{#InstanceId}/networkaccessendpoint/* acs:eiam:{#regionId}: {#accountId}:instance/{#InstanceId}/networkaccessendpoint/{#NetworkAcces sEndpointId} |
| OrganizationalU nit | acs:eiam:{#regionId}: {#accountId}:instance/{#InstanceId}/organizationalunit/{#OrganizationalUnitI d} acs:eiam:{#regionId}: {#accountId}:instance/{#InstanceId}/organizationalunit/* |
| ConditionalAcce ssPolicy | acs:eiam:{#regionId}: {#accountId}:instance/{#InstanceId}/conditionalaccesspolicy/{#ConditionalAcc essPolicyId} acs:eiam:{#regionId}: {#accountId}:instance/{#InstanceId}/conditionalaccesspolicy/* |
| Secret | acs:eiam:{#regionId}: {#accountId}:instance/{#InstanceId}/application/{#ApplicationId}/secret/{#Se cretId} acs:eiam:{#regionId}: {#accountId}:instance/{#InstanceId}/application/{#ApplicationId}/secret/* |

| Group | acs:eiam:{#regionId}:{#accountId}:instance/{#InstanceId}/group/{#GroupId} acs:eiam:{#regionId}:{#accountId}:instance/{#InstanceId}/group/* |
|---|---|
| NetworkZone | acs:eiam:{#regionId}: {#accountId}:instance/{#InstanceId}/networkzone/{#NetworkZoneId} acs:eiam:{#regionId}:{#accountId}:instance/{#InstanceId}/networkzone/* |
| DomainProxyTo ken | acs:eiam:{#regionId}: {#accountId}:instance/{#InstanceId}/domain/{#DomainId}/domainproxytoken /{#DomainProxyTokenId} acs:eiam:{#regionId}: {#accountId}:instance/{#InstanceId}/domain/{#DomainId}/domainproxytoken /* |
| ApplicationFede ratedCredential | acs:eiam:{#regionId}: {#accountId}:instance/{#InstanceId}/application/{#ApplicationId}/applicationf ederatedcredential/{#ApplicationFederatedCredentialId} acs:eiam:{#regionId}: {#accountId}:instance/{#InstanceId}/application/{#ApplicationId}/applicationf ederatedcredential/* acs:eiam:{#regionId}: {#accountId}:instance/{#InstanceId}/application/*/applicationfederatedcredent ial/* |
| ApplicationToke n | acs:eiam:{#regionId}: {#accountId}:instance/{#InstanceId}/application/{#ApplicationId}/applicationt oken/* acs:eiam:{#regionId}: {#accountId}:instance/{#InstanceId}/application/{#ApplicationId}/applicationt oken/{#ApplicationTokenId} |
| SynchronizationJ ob | acs:eiam:{#regionId}: {#accountId}:instance/{#InstanceId}/synchronizationjob/* acs:eiam:{#regionId}: {#accountId}:instance/{#InstanceId}/synchronizationjob/{#SynchronizationJob Id} |
| ApplicationTem plate | acs:eiam:{#regionId}: {#accountId}:applicationtemplate/{#ApplicationTemplateId} |
| NetworkAccessP ath | acs:eiam:{#regionId}: {#accountId}:instance/{#InstanceId}/networkaccessendpoint/{#NetworkAcces sEndpointId}/networkaccesspath/* |

**Condition**

IDaaS does not define service-specific condition keys. For information about common condition keys that are defined by Apsara Stack, see Policy elements.

**Related operations**

You can create a custom policy and attach the policy to a RAM user, RAM user group, or RAM role. For more information, see the following topics: Create a custom policy Grant permissions to a RAM user Grant permissions to a RAM user group Grant permissions to a RAM role

### API catalog

#### Instances

##### UpdateApsaraEiamInstanceDescription

Modifies the description of an instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Descriptio n | Strin g | Query | No | This instance is used in the production environment. | The description of the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateApsaraEiamInstanceDescription &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### DeleteApsaraEiamInstance

Deletes an instance

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteApsaraEiamInstance &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### CreateApsaraEiamInstance

Creates an instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| Descriptio n | Strin g | Query | No | Demo instance for test | The description of the instance. The description can be up to 256 characters in length. |
| UserQuota | Long | Query | No | 1000 | The user quota. |
| Applicatio nQuota | Long | Query | No | 100 | The application quota. |
| IdentityPr oviderQuo ta | Long | Query | No | 100 | The identity provider (IdP) quota. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| InstanceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The instance ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateApsaraEiamInstance &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "InstanceId":"idaas_ue2jvisn35ea5lmthk267xxxxx"
```

##### UpdateApsaraEiamInstanceQuota

Changes the instance specifications.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| UserQuota | Long | Query | No | 1000 | The user quota. |
| Applicatio nQuota | Long | Query | No | 100 | The application quota that can be used. |
| IdentityPr oviderQuo ta | Long | Query | No | 1000 | The identity provider (IdP) quota that can be used. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateApsaraEiamInstanceQuota &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### ListApsaraEiamInstances

Queries a list of Employee Identity and Access Management (EIAM) instances of Identity as a Service (IDaaS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| PageNum ber | Long | Query | No | 1 | The page number. |
| PageSize | Long | Query | No | 10 | The number of entries per page. |
| Status | Strin g | Query | No | running | The status of the instance. Valid values: creating running |
| InstanceId s | Array | Query | No | ["idaas ue2jvisn35eaaat _ hk267xxxxx", "idaas ue2jvisbb5ea5lm _ thk267xxxxx"] | The instance IDs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Instances | Array | Instance list | The instances. |
| -InstanceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The instance ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -CreateTime | Long | 1652085686179 | The time when the instance was created. This value is a UNIX timestamp. Unit: milliseconds. |
| -Status | String | running | The status of the instance. Valid values: creating running |
| -Description | String | Used in the production environment | The description of the instance. |
| - DefaultEndpoi nt | Struct | Object | The default domain name of the instance. |
| --Endpoint | String | example- xxx.aliyunidaas.co m | The endpoint of the instance. |
| --Status | String | resolved | The status of the network endpoint. Valid values: resolved and unresolved. |
| -UserStock | Struct | User quota | The user quota. |
| --StockTotal | Long | 1000 | The total number of users that can be created. |
| --StockUsed | Long | 200 | The number of users created. |
| -- StockRemainin g | Long | 800 | The remaining number of users that can be created. |
| - ApplicationSto ck | Struct | Application quota | The application quota. |
| --StockTotal | Long | 100 | The total number of applications that can be created. |
| --StockUsed | Long | 20 | The number of applications created. |
| -- StockRemainin g | Long | 80 | The remaining number of applications that can be created. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| - IdentityProvid erStock | Struct | IdP quota | The identity provider (IdP) quota. |
| --StockTotal | Long | 100 | The total number of IdPs that can be created. |
| --StockUsed | Long | 20 | The number of IdPs created. |
| -- StockRemainin g | Long | 80 | The remaining number of IdPs that can be created. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| TotalCount | Long | 100 | The total number of instances. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListApsaraEiamInstances &<Common request parameters>
```

Sample responses `JSON` format

```json
 "Instances":[
   "Status":"running",
   "UserStock":[
     "StockUsed":200,
     "StockTotal":1000,
     "StockRemaining":800
```

`],`

```json
   "ApplicationStock":[
     "StockUsed":20,
     "StockTotal":100,
     "StockRemaining":80
```

`],`

```json
   "IdentityProviderStock":[
     "StockUsed":20,
     "StockTotal":100,
     "StockRemaining":80
```

`],`

```json
   "Description":"Used in the production environment",
   "InstanceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
   "CreateTime":1652085686179,
   "DefaultEndpoint":[
     "Status":"resolved",
     "Endpoint":"example-xxx.aliyunidaas.com"
```

`]` `],`

```json
 "TotalCount":100,
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### GetInstanceLicense

Queries the valid license of an Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM) instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk2676xxxx | The instance ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| License | Struct | Struct | The returned license. |
| -LicenseId | String | license 1234xxxx _ | The unique identifier of the license. |
| -LicenseStatus | String | valid | The status of the license. |
| - LicenseCharge Type | String | prepay | The charge type of the license. |
| - LicenseConfigJ son | String | {"modules": [{"features": [{"name":"urn:alib aba:idaas:license: module:ud:custom Field","status":"ena bled"}]…… {"name":"urn:aliba ba:idaas:license:ta g:enterprise","stat us":"enabled"}],"v ersion":"1.0"} | The detailed configurations of the license. The value is a JSON-formatted string. |
| - LicenseCreate Time | Long | 1720509699000 | The time when the license was created. This value is a UNIX timestamp. |
| - PurchaseChan nel | String | alibaba cloud _ | The purchase channel of the license. |
| - PurchaseInsta nceId | String | eiam-cn-xxxxx | The unique identifier of the external product corresponding to the license. |
| -Edition | String | free | The license edition. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -UserQuota | Long | 100 | The user quota corresponding to the license. |
| -StartTime | Long | 1720509699000 | The start time of the validity period of the license. This value is a UNIX timestamp. |
| -EndTime | Long | 1723996800000 | The end time of the validity period of the license. This value is a UNIX timestamp. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetInstanceLicense &InstanceId=idaas_ue2jvisn35ea5lmthk2676xxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "License":{
  "EndTime":1723996800000,
  "LicenseConfigJson":"{\"modules\":[{\"features\":
[{\"name\":\"urn:alibaba:idaas:license:module:ud:customField\",\"status\":\"enabled\"}]
```

……

```json
{\"name\":\"urn:alibaba:idaas:license:tag:enterprise\",\"status\":\"enabled\"}],\"version :\"1.0\"}",
  "LicenseCreateTime":1720509699000,
  "PurchaseInstanceId":"eiam-cn-xxxxx",
  "LicenseChargeType":"prepay",
  "LicenseStatus":"valid",
  "UserQuota":100,
  "StartTime":1720509699000,
  "PurchaseChannel":"alibaba_cloud",
  "LicenseId":"license_1234xxxx",
  "Edition":"free"
```

#### Applications

##### Basics

###### CreateApplication

Creates an application on an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk2676xxxx | The instance ID. |
| Applicatio nName | Strin g | Query | Yes | Ram Account SSO | The application name. |
| Descriptio n | Strin g | Query | No | RAM user SSO application | The description of the application. |
| LogoUrl | Strin g | Query | No | https://oss.cn- hangzhou.aliyuncs.com/l ogo.png | The URL of the application logo. |
| Applicatio nSourceTy pe | Strin g | Query | Yes | urn:alibaba:idaas:app:so urce:standard | The type of the application source. Valid values: urn:alibaba:idaas:app: source:template: application template. urn:alibaba:idaas:app: source:standard: standard protocol. |
| SsoType | Strin g | Query | Yes | saml2 | The Single Sign-On (SSO) protocol. Valid values: saml2: the Security Assertion Markup Language (SAML) 2.0 protocol. oidc: the OpenID Connect (OIDC) protocol. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Applicatio nTemplat eId | Strin g | Query | No | template cloud ram _ _ | The ID of the application template. You must specify this parameter if you set ApplicationSourceType to urn:alibaba:idaas:app:so urce:template. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| ApplicationId | String | app mkv7rgt4d7i4 _ u7zqtzev2xxxx | The application ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateApplication &InstanceId=idaas_ue2jvisn35ea5lmthk2676xxxx &ApplicationName=Ram Account SSO &ApplicationSourceType=urn:alibaba:idaas:app:source:standard &SsoType=saml2 &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "ApplicationId":"app_mkv7rgt4d7i4u7zqtzev2xxxx"
```

###### DeleteApplication

Deletes an Employee Identity and Access Management (EIAM) application of Identity as a Service (IDaaS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteApplication &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### UpdateApplicationDescription

Modifies the description of an Employee Identity and Access Management (EIAM) application of Identity as a Service (IDaaS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk2676xxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| Descriptio n | Strin g | Query | No | A demo application that is used for test | The description of the application. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateApplicationDescription &InstanceId=idaas_ue2jvisn35ea5lmthk2676xxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### EnableApplication

Enables an Employee Identity and Access Management (EIAM) application.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=EnableApplication &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### DisableApplication

Disables an enabled application in Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM). All features of an IDaaS EIAM application cannot be used if you disable the application.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DisableApplication &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### GetApplication

Queries the detailed information about an Employee Identity and Access Management (EIAM) application.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |

| Developer Gui | de·API R | eference |   |   | IDaa |
|---|---|---|---|---|---|
| Parame ter | Typ e | Positi on | Require d | Example | Description |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| Application | Struct | Struct | The detailed information about the application. |
| - ApiInvokeStat us | String | disabled | The status of Developer API for the application. Valid values: enabled disabled |
| -ApplicationId | String | app mkv7rgt4d7i4 _ u7zqtzev2mxxxx | The application ID. |
| - ApplicationNa me | String | SAML application | The application name. |
| - ApplicationSou rceType | String | urn:alibaba:idaas:a pp:source:template | The source of the application. Valid values: urn:alibaba:idaas:app:source:template: application template urn:alibaba:idaas:app:source:standard: standard protocol |
| - ApplicationTe mplateId | String | apt rpa tdsxxx _ _ | The ID of the template based on which the application is created. This parameter is returned only if the application is created based on a template. |
| - AuthorizationT ype | String | authorize required _ | The authorization type of the application. Valid values: authorize required: Only the user with _ explicit authorization can access the application. default all: By default, all users can _ access the application. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -ClientId | String | app mkv7rgt4d7i4 _ u7zqtzev2mxxxx | The client ID of the application. |
| -CreateTime | Long | 1649830226000 | The time when the application was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| -Description | String | application for testing | The description of the application. |
| -Features | String | ["sso", "provision"] | The features supported by the application. The value is a JSON array. Valid values: sso: The application supports Single Sign-On (SSO). provision: The application supports account synchronization. api invoke: The application supports _ custom API operations. |
| -InstanceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The instance ID. |
| -LogoUrl | String | https://img.alicdn.c om/imgextra/i4/O1 CN01lvYwpv1aGow QXDML9 !!600000 _ 0003303-0-tps- 580-580.jpg | The URL of the application icon. |
| - ManagedServi ceCode | String | rpa | The service code of the cloud service that hosts the application template. |
| - ServiceManag ed | Boolean | true | Indicates whether the application template is hosted by a cloud service. |
| -SsoType | String | saml2 | The SSO protocol. Valid values: saml2: the Security Assertion Markup Language (SAML) 2.0 protocol. oidc: the OpenID Connect (OIDC) protocol. |
| -Status | String | enabled | The status of the application. Valid values: enabled disabled |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -UpdateTime | Long | 1649830226000 | The time when the application was last modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| - ApplicationVisi bility | String | Hidden | Indicates whether the application is visible. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetApplication &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "Application":{
  "Status":"enabled",
  "ApplicationVisibility":"",
  "ApplicationName":"SAML application",
  "ApplicationTemplateId":"apt_rpa_tdsxxx",
  "Description":"application for testing",
  "ServiceManaged":true,
  "InstanceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
"LogoUrl":"https://img.alicdn.com/imgextra/i4/O1CN01lvYwpv1aGowQXDML9_!!6000000003303-0 -tps-580-580.jpg",
  "CreateTime":1649830226000,
  "ApplicationSourceType":"urn:alibaba:idaas:app:source:template",
  "SsoType":"saml2",
  "ApiInvokeStatus":"disabled",
  "ManagedServiceCode":"rpa",
  "UpdateTime":1649830226000,
  "ClientId":"app_mkv7rgt4d7i4u7zqtzev2mxxxx",
  "Features":"[\"sso\", \"provision\"]",
  "ApplicationId":"app_mkv7rgt4d7i4u7zqtzev2mxxxx",
  "AuthorizationType":"authorize_required"
```

###### ListApplications

Queries the information about one or more Employee Identity and Access Management (EIAM) applications by page.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| PageNum ber | Long | Query | No | 1 | The page number. |
| PageSize | Long | Query | No | 20 | The number of entries per page. |
| Applicatio nIds | Array | Query | No | Ram Account SSO | The application ID. You can specify multiple application IDs. |
| Applicatio nName | Strin g | Query | No | Ram Account SSO | The application name. Only fuzzy match from the leftmost character is supported. |
| Authorizat ionType | Strin g | Query | No | authorize required _ | The authorization type of the application. Valid values: authorize required: _ Only the user with explicit authorization can access the application. default all: By default, _ all users can access the application. |
| Status | Strin g | Query | No | enabled | The status of the application. Valid values: enabled disabled |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Long | 100 | The total number of entries returned. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| Applications | Array | Array | The information about the applications returned. |
| -InstanceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The instance ID. |
| -ApplicationId | String | app mkv7rgt4d7i4 _ u7zqtzev2mxxxx | The application ID. |
| -ClientId | String | app mkv7rgt4d7i4 _ u7zqtzev2mxxxx | The client ID of the application. |
| -LogoUrl | String | https://img.alicdn.c om/imgextra/i4/O1 CN01lvYwpv1aGow QXDML9 !!600000 _ 0003303-0-tps- 580-580.jpg | The URL of the application icon. |
| - ApplicationNa me | String | SAML application | The application name. |
| -Description | String | A single application whose code is pkces | The description of the application. |
| -SsoType | String | saml2 | The Single Sign-On (SSO) protocol. Valid values: saml2: the Security Assertion Markup Language (SAML) 2.0 protocol. oidc: the OpenID Connect (OIDC) protocol. |
| - ApplicationSou rceType | String | urn:alibaba:idaas:a pp:source:standard | The source of the application. Valid values: urn:alibaba:idaas:app:source:template: application template urn:alibaba:idaas:app:source:standard: standard protocol |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Features | String | ["sso", "provision"] | The features supported by the application. The value is a JSON array. Valid values: sso: The application supports SSO. provision: The application supports account synchronization. api invoke: The application supports _ custom API operations. |
| -Status | String | enabled | The status of the application. Valid values: enabled disabled |
| -CreateTime | Long | 1649830226000 | The time when the application was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| -UpdateTime | Long | 1649830226000 | The time when the application was last modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| - ServiceManag ed | Boolean | true | Indicates whether the application template is hosted by a cloud service. |
| - ManagedServi ceCode | String | rpa | The service code of the cloud service that hosts the application template. |
| - ApplicationTe mplateId | String | apt rpa tdsxxx _ _ | The ID of the template based on which the application is created. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListApplications &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "TotalCount":100,
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "Applications":[
   "Status":"enabled",
   "ApplicationName":"SAML application",
   "Description":"A single application whose code is pkces",
   "ApplicationTemplateId":"",
   "ServiceManaged":true,
   "InstanceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
"LogoUrl":"https://img.alicdn.com/imgextra/i4/O1CN01lvYwpv1aGowQXDML9_!!6000000003303-0 -tps-580-580.jpg",
   "CreateTime":1649830226000,
   "ApplicationSourceType":"urn:alibaba:idaas:app:source:standard",
   "SsoType":"saml2",
   "ManagedServiceCode":"rpa",
   "UpdateTime":1649830226000,
   "ClientId":"app_mkv7rgt4d7i4u7zqtzev2mxxxx",
   "Features":"[\"sso\", \"provision\"]",
   "ApplicationId":"app_mkv7rgt4d7i4u7zqtzev2mxxxx"
```

`]`

###### ListApplicationsForNetworkZone

Queries a list of applications associated with a network zone.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The ID of the Identity-as- a-Service Enterprise Identity Access Management (IDaaS EIAM) instance. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| NextToke n | Strin g | Query | No | NTxxxxxexample | The token used for the next query. You must specify the token that is obtained from the previous query as the value of NextToken. |
| PreviousT oken | Strin g | Query | No | test | The token used to query the previous page. You must specify the token that is obtained from the previous query as the value of PreviousToken. |
| MaxResult s | Integ er | Query | No | 10 | The maximum number of entries returned per page. Default value: 20. Maximum value: 100. |
| NetworkZ oneId | Strin g | Query | Yes | zone123456 | The ID of the network zone associated with the application. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Applications | Array | Array | The applications. |
| -InstanceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The ID of the IDaaS EIAM instance. |
| -ApplicationId | String | app mkv7rgt4d7i4 _ u7zqtzev2mxxxx | The application ID. |
| - ApplicationNa me | String | SAML application | The name of the application. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| TotalCount | Long | 100 | The total number of entries returned. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| NextToken | String | NTxxxexample | The token used for the next query. You must specify the token that is obtained from the previous query as the value of NextToken. |
| PreviousToken | String | test | The token used to query the previous page. You must specify the token that is obtained from the previous query as the value of PreviousToken. |
| MaxResults | Integer | 10 | The maximum number of entries returned per page. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListApplicationsForNetworkZone &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &NetworkZoneId=zone123456 &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "TotalCount":100,
 "PreviousToken":"test",
 "Applications":[
   "ApplicationName":"SAML application",
   "InstanceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
   "ApplicationId":"app_mkv7rgt4d7i4u7zqtzev2mxxxx"
```

`],`

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "NextToken":"NTxxxexample",
 "MaxResults":10
```

###### ListApplicationsForGroup

Queries a list of applications that an Enterprise Identity Access Management (EIAM) group can access.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| PageNum ber | Long | Query | No | 1 | The page number. |
| PageSize | Long | Query | No | 20 | The number of entries per page. |
| Applicatio nIds | Array | Query | No | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The list of application IDs. A maximum of 100 application IDs are supported. |
| GroupId | Strin g | Query | Yes | group miu8e4t4d7i4u7u _ wezgr54xxxx | The group ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Long | 100 | The total number of entries returned. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| Applications | Array | Array | The list of applications that the EIAM group can access. |
| -ApplicationId | String | app mkv7rgt4d7i4 _ u7zqtzev2mxxxx | The application ID. |
| - HasDirectAuth orization | Boolean | true | Indicates whether the EIAM group has direct permissions on the application. Valid values: true: The EIAM group has direct permissions on the application. false: The EIAM group does not have direct permissions on the application. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| - HasInheritAuth orization | Boolean | false | Indicates whether the EIAM group has inherited permissions on the application. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListApplicationsForGroup &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &GroupId=group_miu8e4t4d7i4u7uwezgr54xxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "TotalCount":100,
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "Applications":[
   "HasDirectAuthorization":true,
   "ApplicationId":"app_mkv7rgt4d7i4u7zqtzev2mxxxx",
   "HasInheritAuthorization":false
```

`]`

###### GetApplicationTemplate

Queries the information about an application template in Identity as a Service (IDaaS) Enterprise Identity Access Management (EIAM).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Applicatio nTemplat eId | Strin g | Query | Yes | apt ramuser xxxx _ _ | The application template ID. This parameter does not have a default value. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. This parameter is left empty by default. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| ApplicationTe mplate | Struct | object | The information about the application template. |
| -SsoTypes | String | saml2 | Single sign-on (SSO) protocols are supported. Valid values: saml2: saml2 oidc: oidc |
| - ApplicationTe mplateId | String | apt ramintlrole ixx _ _ xxx | The application template ID. |
| - ApplicationTe mplateName | String | Application template 1 | The name of the application template. |
| -Description | String | OpenID Connect (OIDC) application template | The description of the application template. |
| -LogoUrl | String | https://example.co m/imgextra/i4/O1C N01xTLxLb1WtyKk sHW1H !!6000000 _ 002847-2-tps-xxx- xxx.png | The URL of the application template logo. |
| - HelpDocument Url | String | https://example.co m/document detail _ /409xxx.html | The URL of the help document corresponding to the application template. |
| -CreateTime | Long | 1730341123000 | The time when the application template was created. |
| -UpdateTime | Long | 1730341124000 | The time when the application template was last updated. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| - ServiceManag ed | Boolean | true | Indicates whether the application template is hosted by a cloud service. |
| - ManagedServi ceCode | String | bastionhost | The service code of the cloud service that hosts the application template. |
| - ServiceConsol eUrl | String | https://example.co m/?p=bastion | The console URL of the cloud service that hosts the application template. |
| -SaleInfo | Struct | object | The sales information about the application template. |
| --AlwaysFree | Boolean | true | Indicates whether the application template is permanently free. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=GetApplicationTemplate &ApplicationTemplateId=apt_ramuser_xxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "ApplicationTemplate":{
  "HelpDocumentUrl":"https://example.com/document_detail/409xxx.html",
  "ManagedServiceCode":"bastionhost",
  "SaleInfo":{
   "AlwaysFree":""
```

`},`

```json
  "ApplicationTemplateId":"apt_ramintlrole_ixxxxx",
  "Description":"OIDC application template",
  "ServiceManaged":true,
  "ServiceConsoleUrl":"https://example.com/?p=bastion",
  "LogoUrl":"https://example.com/imgextra/i4/O1CN01xTLxLb1WtyKksHW1H_!!6000000002847-2-
tps-xxx-xxx.png",
  "CreateTime":1730341123000,
  "UpdateTime":1730341124000,
  "ApplicationTemplateName":"Application template 1",
  "SsoTypes":"saml2"
```

`},`

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### UpdateApplicationInfo

Modifies the basic information of an Employee Identity and Access Management (EIAM) application.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| Applicatio nName | Strin g | Query | Yes | Ram Account SSO | The application name. |
| LogoUrl | Strin g | Query | No | https://example.aliyuncs .com/logo.png | The URL of the application logo. |
| Applicatio nVisibility | Array | Query | No | web | Specifies whether the application is visible. |
| ClientToke n | Strin g | Query | No | client-token-example | The client token that is used to ensure the idempotence of the request. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=UpdateApplicationInfo &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &ApplicationName=Ram Account SSO &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

**1.4.2.1.12.**

###### ListApplicationsForNetworkAccessEndpoint

Queries a list of applications associated with a network endpoint.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| NextToke n | Strin g | Query | No | NTxxxxxexample | The query token. |
| MaxResult s | Long | Query | No | 20 | The number of entries to return on each page. |
| NetworkA ccessEndp ointId | Strin g | Query | Yes | nae mxzj4c44ctyectkggt _ g4mxxxxx | The ID of the network endpoint. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ApplicationsFo rNetworkAcces sEndpoint | Array | object | The list of applications associated with the network endpoint. |
| -InstanceId | String | idaas 6ed5syotlwd _ rgmbzn7qn5xxxxx | The instance ID. |
| -ApplicationId | String | app m5nzr3kk4njk _ co2nnc4wjxxxxx | The application ID. |
| - ApplicationNa me | String | cloudSSO | The name of the application. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| TotalCount | Long | 100 | The total number of entries returned. |
| NextToken | String | NTxxxexample | The query token returned in this call. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=ListApplicationsForNetworkAccessEndpoint &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &NetworkAccessEndpointId=nae_mxzj4c44ctyectkggtg4mxxxxx &<Common request parameters>
```

Sample responses `JSON` format

```json
 "TotalCount":100,
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "NextToken":"NTxxxexample",
 "ApplicationsForNetworkAccessEndpoint":[
   "ApplicationName":"cloudSSO",
   "InstanceId":"idaas_6ed5syotlwdrgmbzn7qn5xxxxx",
   "ApplicationId":"app_m5nzr3kk4njkco2nnc4wjxxxxx"
```

`]`

##### SSO

###### EnableApplicationSso

Enables the single sign-on (SSO) feature for an application in Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=EnableApplicationSso &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### DisableApplicationSso

Disables the single sign-on (SSO) feature for an application in Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM). This way, employees cannot log in to the application by using SSO.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DisableApplicationSso &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### SetApplicationSsoConfig

Configures the single sign-on (SSO) attributes of an Enterprise Identity Access Management (EIAM) application.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| SamlSsoC onfig | Struc t | Query | No | Object | The Security Assertion Markup Language (SAML)-based SSO configuration attributes of the application. |
| - SpSsoAcs Url | Strin g |   | No | https://signin.aliyun.com /saml-role/sso | The Assertion Consumer Service (ACS) URL of the application in SAML. |
| - SpEntityId | Strin g |   | No | urn:alibaba:cloudcomput ing | The entity ID of the application in SAML. |
| - NameIdFo rmat | Strin g |   | No | urn:oasis:names:tc:SAM L:1.1:nameid- format:unspecified | The format of the NameID element in the SAML assertion. Valid values: urn:oasis:names:tc:SAM L:1.1:nameid- format:unspecified: No format is specified. How to resolve the NameID element depends on the application. urn:oasis:names:tc:SAM L:1.1:nameid- format:emailAddress: The NameID element must be an email address. urn:oasis:names:tc:SAM L:2.0:nameid- format:persistent: The NameID element must be persistent. urn:oasis:names:tc:SAM L:2.0:nameid- format:transient: The NameID element must be transient. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| - NameIdVa lueExpres sion | Strin g |   | No | user.email | The expression that is used to generate the value of NameID in the SAML assertion. |
| - DefaultRel ayState | Strin g |   | No | https://home.console.ali yun.com | The default value of the RelayState attribute. If the SSO request is initiated in EIAM, the RelayState attribute in the SAML response is set to this default value. |
| - Signature Algorithm | Strin g |   | No | RSA-SHA256 | The algorithm that is used to calculate the signature for the SAML assertion. |
| - Response Signed | Boole an |   | No | true | Specifies whether to calculate the signature for the response. You cannot set ResponseSigned and AssertionSigned to false at the same time. Valid values: true: signs the response. false: does not sign the assertion. |
| - AssertionS igned | Boole an |   | No | true | Specifies whether to calculate the signature for the assertion. You cannot set ResponseSigned and AssertionSigned to false at the same time. Valid values: true: signs the assertion. false: does not sign the assertion. |
| - AttributeS tatements | Array |   | No | Array | The additional user attributes in the SAML assertion. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| -- AttributeS tatements Item | Struc t |   | No | Object | An additional user attribute. |
| --- AttributeN ame | Strin g |   | No | https://www.aliyun.com/ SAML- Role/Attributes/RoleSess ionName | The attribute name in the SAML assertion. |
| --- AttributeV alueExpre ssion | Strin g |   | No | user.username | The expression that is used to generate the value of the attribute in the SAML assertion. |
| - IdPEntityId | Strin g |   | No | https://example.com/ | The entity ID of the identity provider (IdP) in the SAML protocol. The value can be in the URL or URN format. |
| - OptionalR elayStates | Array |   | No | Array | The optional RelayState configurations. |
| -- OptionalR elayStates Item | Struc t |   | No | Object | The optional RelayState configuration. |
| --- RelayStat e | Strin g |   | No | https://ram.console.aliyu n.com/ | The value of RelayState. |
| --- DisplayNa me | Strin g |   | No | Ram | The display name of RelayState. |
| OidcSsoC onfig | Struc t | Query | No | struct | The OIDC-based SSO configuration attributes of the application. |
| - RedirectU ris | Array |   | No | ["https://example.com/oi dc/login/callback","https: //example.com/oidc/logi n/callback1 "] | The list of redirect URIs that are supported by the application. |
| - PostLogou tRedirectU ris | Array |   | No | ["https://example.com/oi dc/login/callback","https: //example.com/oidc/logi n/callback1 "] | The list of post-logout redirect URIs that are supported by the application. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| - GrantType s | Array |   | No | ["authorization code"] _ | The OIDC grant type that is supported. Valid values: authorization code: The _ authorization code grant type. implicit: The implicit grant type. refresh token: The _ refresh token grant type. urn:ietf:params:oauth:gr ant-type: The device authorization grant type. password: The resource owner password credentials grant type. |
| - Response Types | Array |   | No | ["token id token"] _ | The ResponseType parameter in the OIDC protocol. This parameter is valid only when GrantTypes is set to implicit. Valid values: token: returns only an access token. id token: _ returns only an ID token. token id token: returns _ both an access token and an ID token. |
| - GrantScop es | Array |   | No | ["openid"] | The scope parameter in the OIDC protocol. This parameter specifies the scope of user information that can be returned by the userinfo endpoint or included in the ID token. Valid values: openid: An OIDC standard parameter that indicates the unique ID of the user. profile: The detailed information about the user. email: The email address of the user. phone: The phone number of the user. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| - Password TotpMfaR equired | Boole an |   | No | true | Specifies whether time- based one-time password (TOTP) authentication is required in password mode. This parameter is valid only when GrantTypes for the OIDC application is set to password. |
| - Password Authentic ationSour ceId | Strin g |   | No | ia password _ | The ID of the identity source for the resource owner password credentials grant type. This parameter is valid only when GrantTypes for the OIDC application is set to password. |
| - PkceRequi red | Boole an |   | No | true | Specifies whether the SSO of the application requires Proof Key for Code Exchange (PKCE) (RFC 7636). |
| - PkceChall engeMeth ods | Array |   | No | S256 | The algorithm used to compute the code challenge in PKCE. Valid values: plain: The code challenge is the same as the code verifier. S256: The SHA-256 algorithm. |
| - AccessTok enEffectiv eTime | Long |   | No | 1200 | The validity period of the issued access token. Unit: seconds. Default value: 1200. |
| - CodeEffec tiveTime | Long |   | No | 60 | The validity period of the issued code. Unit: seconds. Default value: 60. |
| - IdTokenEff ectiveTim e | Long |   | No | 300 | The validity period of the issued ID token. Unit: seconds. Default value: 300. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| - RefreshTo kenEffecti ve | Long |   | No | 86400 | The validity period of the issued refresh token. Unit: seconds. Default value: 86400. |
| - CustomCl aims | Array |   | No | Array | The custom claims that are returned for the ID token. |
| -- CustomCl aimsItem | Struc t |   | No | object | The custom claim that is returned for the ID token. |
| --- ClaimNam e | Strin g |   | No | "Role" | The name of the claim. |
| --- ClaimValu eExpressi on | Strin g |   | No | user.dict.applicationRole | The expression that is used to generate the value of the claim. |
| - SubjectIdE xpression | Strin g |   | No | user.userid | The custom expression that is used to generate the subject ID returned for the ID token. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InitLoginT ype | Strin g | Query | No | only app init sso _ _ _ | The initial SSO method. Valid values: only app init sso: _ _ _ Only application- initiated SSO is allowed. This method is selected by default when the SSO protocol of the application is an OIDC protocol. If this method is selected when the SSO protocol of the application is SAML, the InitLoginUrl parameter is required. idaas or app init sso: _ _ _ _ IDaaS-initiated SSO and application- initiated SSO are allowed. This method is selected by default when the SSO protocol of the application is SAML. If this method is selected when the SSO protocol of the application is an OIDC protocol, the InitLoginUrl parameter is required. |
| InitLoginU rl | Strin g | Query | No | http://127.0.0.1:8000/st art login? _ enterprise code=ABCDE _ F | The initial webhook URL of SSO. This parameter is required when the SSO protocol of the application is an OIDC protocol and the InitLoginType parameter is set to idaas or app init sso. or _ _ _ _ when the SSO protocol of the application is SAML and the InitLoginType parameter is set to only app init sso. _ _ _ |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClientToke n | Strin g | Query | No | client-examplexxx | A client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see How to ensure idempotence. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SetApplicationSsoConfig &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### GetApplicationSsoConfig

Queries the single sign-on (SSO) configuration attributes of an application in Identity-as-a- Service Enterprise Identity Access Management (IDaaS EIAM)).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| ApplicationSso Config | Struct | Struct | The SSO configuration information of the application. |
| -SsoStatus | String | enabled | The SSO feature status of the application. Valid values: enabled: The feature is enabled. disabled: The feature is disabled. |
| -InitLoginType | String | only app init sso _ _ _ | The initial SSO method. Valid values: only app init sso: Only application- _ _ _ initiated SSO is allowed. This method is selected by default when the SSO protocol of the application is an OpenID Connect (OIDC) protocol. If this method is selected when the SSO protocol of the application is Security Assertion Markup Language (SAML), the InitLoginUrl parameter is required. idaas or app init sso: IDaaS-initiated _ _ _ _ SSO and application-initiated SSO are allowed. This method is selected by default when the SSO protocol of the application is SAML. If this method is selected when the SSO protocol of the application is an OIDC protocol, the InitLoginUrl parameter is required. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -InitLoginUrl | String | http://127.0.0.1:80 00/start login? _ enterprise code=A _ BCDEF | The initial webhook URL of SSO. This parameter is required when the SSO protocol of the application is an OIDC protocol and the InitLoginType parameter is set to idaas or app init sso or when the _ _ _ _ SSO protocol of the application is SAML and the InitLoginType parameter is set to only app init sso. _ _ _ |
| - SamlSsoConfig | Struct | Struct | The SAML-based SSO configuration attributes of the application. This parameter is returned only when the SSO protocol of the application is SAML 2.0. |
| --SpSsoAcsUrl | String | https://signin.aliyu n.com/saml- role/sso | The Assertion Consumer Service (ACS) URL of the application in SAML. |
| --SpEntityId | String | urn:alibaba:cloudc omputing | The entity ID of the application in SAML. |
| -- NameIdFormat | String | urn:oasis:names:tc :SAML:1.1:nameid- format:unspecified | The format of the NameID element in the SAML assertion. |
| -- NameIdValueE xpression | String | user.username | The expression that is used to generate the value of NameID in the SAML assertion. |
| -- DefaultRelaySt ate | String | https://home.conso le.aliyun.com | The default value of the RelayState attribute. If the SSO request is initiated in EIAM, the RelayState attribute in the SAML response is set to this default value. |
| -- SignatureAlgor ithm | String | RSA-SHA256 | The algorithm that is used to calculate the signature for the SAML assertion. |
| -- ResponseSign ed | Boolean | true | Specifies whether to calculate the signature for the response. You cannot set ResponseSigned and AssertionSigned to false at the same time. Valid values: true false |
| -- AssertionSigne d | Boolean | true | Specifies whether to calculate the signature for the assertion. You cannot set ResponseSigned and AssertionSigned to false at the same time. Valid values: true false |

| Parameter | Type | Example | Description |
|---|---|---|---|
| --IdPEntityId | String | http://test****.cn/a dfs/services/trust | The entity ID obtained after the IdP metadata file is parsed. |
| -- AttributeState ments | Array | Array | The additional user attributes in the SAML assertion. |
| --- AttributeName | String | https://www.aliyun. com/SAML- Role/Attributes/Rol eSessionName | The attribute name in the SAML assertion. |
| --- AttributeValue Expression | String | user.username | The expression that is used to generate the value of the attribute in the SAML assertion. |
| -- OptionalRelay States | Array | Array | The optional relay status. |
| ---RelayState | String | https://cloudsso.co nsole.aliyun.com | The relay status. |
| --- DisplayName | String | test | The display name. |
| - OidcSsoConfig | Struct | struct | The OIDC-based SSO configuration attributes of the application. This parameter is returned only when the SSO protocol of the application is an OIDC protocol. |
| -- PasswordTotp MfaRequired | Boolean | true | Specifies whether time-based one-time password (TOTP) authentication is required in password mode. This parameter is returned only when the value of the GrantTypes parameter includes the password mode. |
| -- PasswordAuth enticationSour ceId | String | ia password _ | The ID of the identity authentication source in password mode. This parameter is returned only when the value of the GrantTypes parameter includes the password mode. |
| -- PkceRequired | Boolean | true | Specifies whether the SSO of the application requires Proof Key for Code Exchange (PKCE) (RFC 7636). |

| DaaS |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -- AccessTokenEf fectiveTime | Long | 1200 | The validity period of the issued access token. Unit: seconds. Default value: 1200. |
| -- CodeEffective Time | Long | 60 | The validity period of the issued code. Unit: seconds. Default value: 60. |
| -- IdTokenEffecti veTime | Long | 1200 | The validity period of the issued ID token. Unit: seconds. Default value: 300. |
| -- RefreshTokenE ffective | Long | 86400 | The validity period of the issued refresh token. Unit: seconds. Default value: 86400. |
| -- SubjectIdExpr ession | String | user.userid | The custom expression that is used to generate the subject ID returned for the ID token. |
| -- CustomClaims | Array | Array | The custom claims that are returned for the ID token. |
| ---ClaimName | String | userOuIds | The claim name. |
| --- ClaimValueExp ression | String | ObjectToJsonString (user.organizationa lUnits) | The expression that is used to generate the value of the claim. |
| --RedirectUris | String | https://www.examp le.com | The list of redirect URIs that are supported by the application. |
| -- PostLogoutRed irectUris | String | https://www.examp le.com/uri | The list of logout redirect URIs that are supported by the application. |
| --GrantTypes | String | authorization code _ | The list of grant types that are supported for OIDC protocols. |
| -- ResponseType s | String | token id token _ | The response types that are supported by the application. This parameter is returned when the value of the GrantTypes parameter includes the implicit mode. |
| --GrantScopes | String | profile, email | The permissions of the Developer API feature. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -- PkceChallenge Methods | String | S256 | The algorithms that are used to calculate the code challenge for PKCE. |
| - ProtocolEndpoi ntDomain | Struct | Struct | The configuration of the metadata endpoint provided by the application. |
| -- SamlSsoEndpo int | String | https://l1seshcn.ali yunidaas.com/login /app/app mltuxdw _ d4lq4eer6tmtlmax m5e/saml2/sso | The request receiving URL of the SAML protocol. This parameter is returned only when the SSO protocol of the application is SAML 2.0. |
| -- SamlMetaEndp oint | String | https://l1seshcn.ali yunidaas.com/api/v 2/app mltuxdwd4l _ q4eer6tmtlmaxm5 e/saml2/meta | The metadata URL of the SAML protocol. This parameter is returned only when the SSO protocol of the application is SAML 2.0. |
| --OidcIssuer | String | https://eiam-api- cn- hangzhou.aliyuncs. com/v2/idaas ue2j _ visn35ea5lmthk26 76rypm/app mltta _ 64q65enci54slingv vsgq/oidc | The information about the OIDC issuer. This parameter is returned only when the SSO protocol of the application is an OIDC protocol. |
| -- OidcJwksEndp oint | String | https://eiam-api- cn- hangzhou.aliyuncs. com/v2/idaas ue2j _ visn35ea5lmthk26 76rypm/app mltta _ 64q65enci54slingv vsgq/oidc/jwks | The JSON Web Key Set (JWKS) URL of the OIDC issuer. This parameter is returned only when the SSO protocol of the application is an OIDC protocol. |
| -- Oauth2Authori zationEndpoint | String | https://l1seshcn.ali yunidaas.com/login /app/app mltta64q _ 65enci54slingvvsg q/oauth2/authorize | The OAuth2.0 authorization endpoint. This parameter is returned only when the SSO protocol of the application is an OIDC protocol. |
| -- Oauth2Revoke Endpoint | String | https://eiam-api- cn- hangzhou.aliyuncs. com/v2/idaas ue2j _ visn35ea5lmthk26 76rypm/app mltta _ 64q65enci54slingv vsgq/oauth2/revok e | The OAuth2.0 token revocation endpoint. This parameter is returned only when the SSO protocol of the application is an OIDC protocol. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -- Oauth2TokenE ndpoint | String | https://eiam-api- cn- hangzhou.aliyuncs. com/v2/idaas ue2j _ visn35ea5lmthk26 76rypm/app mltta _ 64q65enci54slingv vsgq/oauth2/token | The OAuth2.0 token endpoint. This parameter is returned only when the SSO protocol of the application is an OIDC protocol. |
| -- Oauth2Device AuthorizationE ndpoint | String | https://eiam-api- cn- hangzhou.aliyuncs. com/v2/idaas ue2j _ visn35ea5lmthk26 76rypm/app mltta _ 64q65enci54slingv vsgq/oauth2/devic e/code | The OAuth2.0 device authorization endpoint. This parameter is returned only when the SSO protocol of the application is an OIDC protocol. |
| -- Oauth2Userinf oEndpoint | String | https://eiam-api- cn- hangzhou.aliyuncs. com/v2/idaas ue2j _ visn35ea5lmthk26 76rypm/app mltta _ 64q65enci54slingv vsgq/oauth2/userin fo | The OIDC UserInfo endpoint. This parameter is returned only when the SSO protocol of the application is an OIDC protocol. |
| -- OidcLogoutEn dpoint | String | https://l1seshcn.ali yunidaas.com/login /app/app mltta64q _ 65enci54slingvvsg q/oauth2/logout | The OIDC relying party (RP)-initiated logout endpoint. This parameter is returned only when the SSO protocol of the application is an OIDC protocol. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetApplicationSsoConfig &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "ApplicationSsoConfig":{
  "ProtocolEndpointDomain":{
   "SamlMetaEndpoint":"",
   "OidcIssuer":"",
   "Oauth2DeviceAuthorizationEndpoint":"",
   "Oauth2UserinfoEndpoint":"",
   "OidcJwksEndpoint":"",
   "Oauth2RevokeEndpoint":"",
```

```json
   "Oauth2TokenEndpoint":"",
   "OidcLogoutEndpoint":"",
   "Oauth2AuthorizationEndpoint":"",
   "SamlSsoEndpoint":""
```

`},`

```json
  "SamlSsoConfig":{
   "AttributeStatements":[
     "AttributeValueExpression":"",
     "AttributeName":""
```

`],`

```json
   "NameIdValueExpression":"",
   "ResponseSigned":"",
   "OptionalRelayStates":[
     "RelayState":"",
     "DisplayName":""
```

`],`

```json
   "SpEntityId":"",
   "SpSsoAcsUrl":"",
   "DefaultRelayState":"",
   "SignatureAlgorithm":"",
   "AssertionSigned":"",
   "NameIdFormat":"",
   "IdPEntityId":""
```

`},`

```json
  "SsoStatus":"enabled",
  "InitLoginType":"only_app_init_sso",
  "InitLoginUrl":"http://127.0.0.1:8000/start_login?enterprise_code=ABCDEF",
  "OidcSsoConfig":{
   "ResponseTypes":"",
   "PasswordAuthenticationSourceId":"",
   "PasswordTotpMfaRequired":"",
   "SubjectIdExpression":"",
   "PkceChallengeMethods":"",
   "RefreshTokenEffective":"",
   "CustomClaims":[
     "ClaimName":"",
     "ClaimValueExpression":""
```

`],`

```json
   "PostLogoutRedirectUris":"",
   "PkceRequired":"",
   "AccessTokenEffectiveTime":"",
   "GrantScopes":"",
   "IdTokenEffectiveTime":"",
   "RedirectUris":"",
   "CodeEffectiveTime":"",
   "GrantTypes":""
```

##### Application authorization

###### AuthorizeApplicationToUsers

Grants the permissions to access an application to multiple accounts in Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM) at a time.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk2676xxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| UserIds | Array | Query | Yes | user d6sbsuumeta4h66 _ ec3il7yxxxx | The IDs of the accounts to which you want to grant permissions. You can grant permissions to a maximum of 100 accounts at a time. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AuthorizeApplicationToUsers &InstanceId=idaas_ue2jvisn35ea5lmthk2676xxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &UserIds=user_d6sbsuumeta4h66ec3il7yxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

**1.4.2.3.2.**

###### AuthorizeApplicationToOrganizationalUnits

Grants the access permissions on an application to multiple Employee Identity and Access Management (EIAM) organizations at a time.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk2676xxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| Organizati onalUnitId s | Array | Query | Yes | ou wovwffm62xifdziem7 _ an7xxxxx | The IDs of the organizations. You can grant the access permissions to a maximum of 100 organizations at a time. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AuthorizeApplicationToOrganizationalUnits &InstanceId=idaas_ue2jvisn35ea5lmthk2676xxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &OrganizationalUnitIds=ou_wovwffm62xifdziem7an7xxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### AuthorizeApplicationToGroups

Grants the permissions to access an application to multiple account groups in Identity-as-a- Service Enterprise Identity Access Management (IDaaS EIAM) at a time.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk2676xxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| GroupIds | Array | Query | Yes | group miu8e4t4d7i4u7u _ wezgr54xxxx | The IDs of the account groups to which you want to grant permissions. You can grant permissions to a maximum of 100 account groups at a time. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AuthorizeApplicationToGroups &InstanceId=idaas_ue2jvisn35ea5lmthk2676xxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &GroupIds=group_miu8e4t4d7i4u7uwezgr54xxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### RevokeApplicationFromUsers

Revokes the access permissions on an application from multiple Employee Identity and Access Management (EIAM) accounts at a time.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| UserIds | Array | Query | Yes | user d6sbsuumeta4h66 _ ec3il7yxxxx | The IDs of the accounts. You can revoke the access permissions from a maximum of 100 accounts at a time. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=RevokeApplicationFromUsers &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &UserIds=user_d6sbsuumeta4h66ec3il7yxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

**1.4.2.3.5.**

###### RevokeApplicationFromOrganizationalUnits

Revokes the permissions to access an application from multiple organizations in Identity-as-a- Service Enterprise Identity Access Management (IDaaS EIAM) at a time.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Organizati onalUnitId s | Array | Query | Yes | ou wovwffm62xifdziem7 _ an7xxxxx | The IDs of the organizations to from you want to revoke permissions. You can revoke permissions from a maximum of 100 organizations at a time. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=RevokeApplicationFromOrganizationalUnits &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &OrganizationalUnitIds=ou_wovwffm62xifdziem7an7xxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### RevokeApplicationFromGroups

Revokes the permissions to access an application from multiple account groups at a time in Identity as a Service (IDaaS) Enterprise Identity Access Management (EIAM).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| GroupIds | Array | Query | Yes | group miu8e4t4d7i4u7u _ wezgr54xxxx | The IDs of the account groups from which you want to revoke permissions. You can revoke permissions from a maximum of 100 account groups at a time. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=RevokeApplicationFromGroups &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &GroupIds=group_miu8e4t4d7i4u7uwezgr54xxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### UpdateApplicationAuthorizationType

Modifies the authorization type of an Employee Identity and Access Management (EIAM) application.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| Authorizat ionType | Strin g | Query | Yes | authorize required _ | The authorization type of the EIAM application. Valid values: authorize required: _ Only the user with explicit authorization can access the application. default all: By default, _ all users can access the application. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateApplicationAuthorizationType &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &AuthorizationType=authorize_required &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### ListUsersForApplication

Queries the accounts that are allowed to access an Employee Identity and Access Management (EIAM) application. The return results include the IDs of the accounts. If you need to obtain the details of the accounts, call the GetUser operation.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| PageNum ber | Long | Query | No | 1 | The page number. |
| PageSize | Long | Query | No | 20 | The number of entries per page. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| UserIds | Array | Query | No | user d6sbsuumeta4h66 _ ec3il7yxxxx | The IDs of the accounts. You can revoke the access permissions from a maximum of 100 accounts at a time. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Long | 100 | The total number of entries returned. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| Users | Array | Struct | The account IDs. |
| -UserId | String | user d6sbsuumeta _ 4h66ec3il7yxxxx | The account ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListUsersForApplication &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &<Common request parameters>
```

Sample responses `JSON` format

```json
 "TotalCount":100,
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "Users":[
   "UserId":"user_d6sbsuumeta4h66ec3il7yxxxx"
```

`]`

###### ListOrganizationalUnitsForApplication

Queries the organizations that are allowed to access an Enterprise Identity Access Management (EIAM) application by page. The return result includes the IDs of the organizations. If you want to obtain the details of the organizations, call the GetOrganizationalUnit operation.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| PageNum ber | Long | Query | No | 1 | The page number. |
| PageSize | Long | Query | No | 20 | The number of entries per page. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Organizati onalUnitId s | Array | Query | No | ou wovwffm62xifdziem7 _ an7xxxxx | The IDs of the organizations that are allowed to access the application. You can query a maximum of 100 organization IDs at a time. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Long | 100 | The total number of entries returned. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| Organizational Units | Array | Array | The IDs of the organizations that are allowed to access the application. |
| - Organizational UnitId | String | ou wovwffm62xifd _ ziem7an7xxxxx | The organization ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListOrganizationalUnitsForApplication &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "TotalCount":100,
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "OrganizationalUnits":[
   "OrganizationalUnitId":"ou_wovwffm62xifdziem7an7xxxxx"
```

`]`

###### ListGroupsForApplication

Queries the account groups that are granted permissions to access an application and displays the results by page. The IDs of the account groups are returned. To query the detailed information about the account groups, call the GetGroup operation.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| PageNum ber | Long | Query | No | 1 | The page number. |
| PageSize | Long | Query | No | 20 | The number of entries per page. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| GroupIds | Array | Query | No | group miu8e4t4d7i4u7u _ wezgr54xxxx | The IDs of the account groups that are allowed to access the application. You can query a maximum of 100 account groups at a time. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Long | 100 | The total number of entries returned. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| Groups | Array | Array | The group IDs. |
| -GroupId | String | group miu8e4t4d7i _ 4u7uwezgr54xxxx | The group ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListGroupsForApplication &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "TotalCount":100,
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "Groups":[
   "GroupId":"group_miu8e4t4d7i4u7uwezgr54xxxx"
```

`]`

###### ListApplicationsForOrganizationalUnit

Queries the applications that an Enterprise Identity Access Management (EIAM) organization can access. The return result includes the IDs of the applications. To query the detailed information about the applications, call the GetApplication operation.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| PageNum ber | Long | Query | No | 1 | The page number. |
| PageSize | Long | Query | No | 20 | The number of entries per page. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Applicatio nIds | Array | Query | No | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The IDs of the applications that the EIAM organization can access. You can query a maximum of 100 application IDs at a time. |
| Organizati onalUnitId | Strin g | Query | Yes | ou wovwffm62xifdziem7 _ an7xxxxx | The EIAM organization ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Long | 100 | The total number of entries returned. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| Applications | Array | Struct | The applications that the EIAM organization can access. |
| -ApplicationId | String | app mkv7rgt4d7i4 _ u7zqtzev2mxxxx | The application ID. |
| - HasDirectAuth orization | Boolean | true | Indicates whether the EIAM organization has direct permissions on the application. |
| - HasInheritAuth orization | Boolean | false | Indicates whether the EIAM organization has inherited permissions on the application. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListApplicationsForOrganizationalUnit &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &OrganizationalUnitId=ou_wovwffm62xifdziem7an7xxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "TotalCount":100,
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "Applications":[
   "HasDirectAuthorization":"",
   "ApplicationId":"app_mkv7rgt4d7i4u7zqtzev2mxxxx",
   "HasInheritAuthorization":""
```

`]`

###### ListApplicationsForUser

Queries the applications that an Employee Identity and Access Management (EIAM) account can access. The return result includes the IDs of the applications. If you want to obtain the details of the applications, call the GetApplication operation.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| PageNum ber | Long | Query | No | 1 | The page number. |
| PageSize | Long | Query | No | 20 | The number of entries per page. |
| Applicatio nIds | Array | Query | No | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The IDs of the applications that the EIAM organization can access. You can query a maximum of 100 application IDs at a time. |
| UserId | Strin g | Query | Yes | user d6sbsuumeta4h66 _ ec3il7yxxxx | The account ID. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| QueryMod e | Strin g | Query | No | OnlyDirect | The query mode. Default value: OnlyDirect . Valid values: OnlyDirect: Only the direct permissions are queried. Direct permissions are the permissions that are directly granted to the account. IncludeInherit: Both the permissions that are directly granted to the account and the inherited permissions are queried. Inherited permissions are the permissions that an account inherits from the parent organization or the group to which the account belongs. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Long | 100 | The total number of entries returned. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| Applications | Array | Array | The applications that the EIAM organization can access. |
| -ApplicationId | String | app mkv7rgt4d7i4 _ u7zqtzev2mxxxx | The ID of the application. |
| - HasDirectAuth orization | Boolean | true | Indicates whether the EIAM account has direct permissions on the application. Valid values: true: The EIAM account has direct permissions on the application. false: The EIAM account does not have direct permissions on the application. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| - HasInheritAuth orization | Boolean | false | Indicates whether the EIAM account has inherited permissions on the application. Valid values: true: A parent organization or an organization to which the EIAM account belongs has direct permissions on the application. false: A parent organization or an organization to which the EIAM account belongs does not have direct permissions on the application. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListApplicationsForUser &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &UserId=user_d6sbsuumeta4h66ec3il7yxxxx &<Common request parameters>
```

Sample responses `JSON` format

```json
 "TotalCount":100,
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "Applications":[
   "HasDirectAuthorization":true,
   "ApplicationId":"app_mkv7rgt4d7i4u7zqtzev2mxxxx",
   "HasInheritAuthorization":false
```

`]`

##### Client keys

###### CreateApplicationClientSecret

Creates a client key for an Enterprise Identity Access Management (EIAM) application. An EIAM application can have at most two client keys.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| ApplicationClie ntSecret | Struct | Struct | The information about the client keys. |
| -ClientId | String | app mkv7rgt4d7i4 _ u7zqtzev2mxxxx | The client ID of the application. |
| -SecretId | String | sci k52x2ru63rlkfli _ na5utgkxxxx | The client key ID of the application. |
| -ClientSecret | String | CSEHDcHcrUKHw1 CuxkJEHPveWRXBG qVqRsxxxx | The client key secret of the application. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateApplicationClientSecret &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "ApplicationClientSecret":{
  "ClientSecret":"CSEHDcHcrUKHw1CuxkJEHPveWRXBGqVqRsxxxx",
  "SecretId":" sci_k52x2ru63rlkflina5utgkxxxx",
  "ClientId":"app_mkv7rgt4d7i4u7zqtzev2mxxxx"
```

###### DeleteApplicationClientSecret

Deletes a client key for an application in Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM)).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| SecretId | Strin g | Query | Yes | sci k52x2ru63rlkflina5ut _ gkxxxx | The ID of the client key that you want to delete for the application. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteApplicationClientSecret &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &SecretId= sci_k52x2ru63rlkflina5utgkxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### DisableApplicationClientSecret

Disables a client key of an Enterprise Identity Access Management (EIAM) application.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| SecretId | Strin g | Query | Yes | sci k52x2ru63rlkflina5ut _ gkxxxx | The client key ID of the application. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DisableApplicationClientSecret &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &SecretId=sci_k52x2ru63rlkflina5utgkxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### EnableApplicationClientSecret

Enables a client key for an application in Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| SecretId | Strin g | Query | Yes | sci k52x2ru63rlkflina5ut _ gkxxxx | The ID of the client key that you want to enable for the application. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=EnableApplicationClientSecret &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &SecretId=sci_k52x2ru63rlkflina5utgkxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### ListApplicationClientSecrets

Queries all client keys of an application in Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM). The returned key secrets are masked. To obtain unmasked key secrets, call the ObtainApplicationClientSecret operation.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Long | 100 | The total number of entries returned. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| ApplicationClie ntSecrets | Array | Array | The information about the client keys. |
| -InstanceId | String | idaas wdziy4vnjt33 _ ehhf7z2o2nxxxx | The instance ID. |
| -ApplicationId | String | app mkv7rgt4d7i4 _ u7zqtzev2mxxxx | The application ID. |
| -ClientId | String | app mkv7rgt4d7i4 _ u7zqtzev2mxxxx | The client ID of the application. |
| -SecretId | String | sci k52x2ru63rlkfli _ na5utgkxxxx | The client key ID of the application. |
| -ClientSecret | String | eyJh*************** ******************* ******************* ******************* ******************* **********OQ | The client key secret of the application. The returned value is masked. |

| DaaS |   |   | Developer Guide·API Referenc |
|---|---|---|---|
| Parameter | Type | Example | Description |
| -Status | String | enabled | The status of the client key. Valid values: enabled: The client key is enabled. disabled: The client key is disabled. |
| -LastUsedTime | Long | 1649830226000 | The time when the client key was last used. This value is a UNIX timestamp. Unit: milliseconds. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListApplicationClientSecrets &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "TotalCount":100,
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "ApplicationClientSecrets":[
   "Status":"enabled",
   "InstanceId":"idaas_wdziy4vnjt33ehhf7z2o2nxxxx",
"ClientSecret":"eyJh*********************************************************************
******************************OQ",
   "SecretId":"sci_k52x2ru63rlkflina5utgkxxxx",
   "LastUsedTime":1649830226000,
   "ClientId":"app_mkv7rgt4d7i4u7zqtzev2mxxxx",
   "ApplicationId":"app_mkv7rgt4d7i4u7zqtzev2mxxxx"
```

`]`

###### ObtainApplicationClientSecret

Queries a client key of an Enterprise Identity Access Management (EIAM) application. The returned key is masked. To query the unmasked key, call the ListApplicationClientSecrets operation.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| SecretId | Strin g | Query | Yes | sci k52x2ru63rlkflina5ut _ gkxxxx | The client key ID of the application. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| ApplicationClie ntSecret | Struct | Struct | The information about the client key. |
| -InstanceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The instance ID. |
| -ApplicationId | String | app mkv7rgt4d7i4 _ u7zqtzev2mxxxx | The application ID. |
| -ClientId | String | app mkv7rgt4d7i4 _ u7zqtzev2mxxxx | The client ID of the application. |
| -SecretId | String | sci k52x2ru63rlkfli _ na5utgkxxxx | The client key ID of the application. |
| -ClientSecret | String | CSEHDcHcrUKHw1 CuxkJEHPveWRXBG qVqRsxxxx | The client key secret of the application. |
| -Status | String | enabled | The status of the client key. Valid values: enabled: The client key is enabled. disabled: The client key is disabled. |
| -LastUsedTime | Long | 1649830226000 | The time when the client key was last used. The value is a UNIX timestamp. Unit: milliseconds. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ObtainApplicationClientSecret &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &SecretId= sci_k52x2ru63rlkflina5utgkxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "ApplicationClientSecret":{
  "Status":"enabled",
  "InstanceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
  "ClientSecret":"CSEHDcHcrUKHw1CuxkJEHPveWRXBGqVqRsxxxx",
  "SecretId":" sci_k52x2ru63rlkflina5utgkxxxx",
  "LastUsedTime":1649830226000,
  "ClientId":"app_mkv7rgt4d7i4u7zqtzev2mxxxx",
  "ApplicationId":"app_mkv7rgt4d7i4u7zqtzev2mxxxx"
```

**1.4.2.4.7.**

###### UpdateApplicationClientSecretExpirationTime

Updates the expiration time of a client key for an application in Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The ID of the application in IDaaS. |
| SecretId | Strin g | Query | Yes | sci k52x2ru63rlkflina5ut _ gkxxxx | The client key. |

| Developer Gui | de·API R | eference |   |   | IDaa |
|---|---|---|---|---|---|
| Parame ter | Typ e | Positi on | Require d | Example | Description |
| Expiration Time | Long | Query | Yes | 86400 | The validity period of the client key. This value is a UNIX timestamp. Unit: milliseconds. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateApplicationClientSecretExpirationTime &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &SecretId=sci_k52x2ru63rlkflina5utgkxxxx &ExpirationTime=86400 &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### Application tokens

###### CreateApplicationToken

Creates an application token.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| Applicatio nTokenTy pe | Strin g | Query | Yes | bearer token _ | The type of the application token. |
| Expiration Time | Long | Query | No | 1735530123762 | The expiration time. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ApplicationTok ens | Struct | object | The detailed information about the application token. |
| - ApplicationTok enId | String | token ndfxxigahelf _ ne2y2hodehrxxxx | The ID of the application token. |
| - ApplicationTok en | String | SATFwqX8zxGf83pJ cJw78KFGjmrft4er WeZYBGS8oE7NN6 qoE217yaJpUdMb1 UuuGqhDiF43sCA4 CF91CTL5iGntqwyL uaAcS9FJ9HfGadE5 a7TjiwVafwrBYkt3X XX | The application token. |
| - ApplicationTok enType | String | bearer token _ | The type of the application token. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=CreateApplicationToken &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &ApplicationTokenType=bearer_token &<Common request parameters>
```

Sample responses `JSON` format

```json
 "ApplicationTokens":{
  "ApplicationTokenId":"token_ndfxxigahelfne2y2hodehrxxxx",
  "ApplicationTokenType":"bearer_token",
"ApplicationToken":"SATFwqX8zxGf83pJcJw78KFGjmrft4erWeZYBGS8oE7NN6qoE217yaJpUdMb1UuuGqhDi 3sCA4CF91CTL5iGntqwyLuaAcS9FJ9HfGadE5a7TjiwVafwrBYkt3XXX"
```

`},`

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### EnableApplicationToken

Enables an application token.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| Applicatio nTokenId | Strin g | Query | Yes | token sfrwerxxxxxxxxxx _ xxxx | The application token ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=EnableApplicationToken &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &ApplicationTokenId=token_sfrwerxxxxxxxxxxxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### DisableApplicationToken

Disables an application token.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| Applicatio nTokenId | Strin g | Query | Yes | token sfrwerxxxxxxxxxx _ xxxx | The application token ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DisableApplicationToken &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &ApplicationTokenId=token_sfrwerxxxxxxxxxxxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### UpdateApplicationTokenExpirationTime

Updates the expiration time of an application token.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| Applicatio nTokenId | Strin g | Query | Yes | token sfrwerxxxxxxxxxx _ xxxx | The application token ID. |
| Expiration Time | Long | Query | Yes | 1735530123762 | The expiration time of the application token. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=UpdateApplicationTokenExpirationTime &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &ApplicationTokenId=token_sfrwerxxxxxxxxxxxxxx &ExpirationTime=1735530123762 &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### ListApplicationTokens

Queries a list of application tokens.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| Applicatio nTokenTy pe | Strin g | Query | Yes | bearer token _ | The type of the application token. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ApplicationTok ens | Array | array | The application token. |
| -AliUid | Long | 1973166921975 | The Alibaba Cloud account ID. |

| Developer Guide·A | PI Reference |   | IDaa |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -InstanceId | String | idaas ki6hd7ihir4y _ bawogqk6kqxxxx | The ID of the IDaaS EIAM instance. |
| -ApplicationId | String | app m7ar5tms4dw _ tggavalk3j3mxxxx | The application ID. |
| - ApplicationTok enId | String | token ndfxxigahelf _ ne2y2hodehrxxxx | The ID of the application token. |
| - ApplicationTok enType | String | bearer token _ | The type of the application token. |
| - ApplicationTok en | String | SATFwqX8zxGf83pJ cJw78KFGjmrft4er WeZYBGS8oE7NN6 qoE217yaJpUdMb1 UuuGqhDiF43sCA4 CF91CTL5iGntqwyL uaAcS9FJ9HfGadE5 a7TjiwVafwrBYktxx xx | The application token. |
| -Status | String | enabled | Indicates whether the application token is enabled. |
| -Description | String | jwqtts-0430 | The description of the application token. |
| - ExpirationTim e | Long | 1747796654000 | The expiration time. |
| -LastUsedTime | Long | 1747796654000 | The time when the application token was used for the last time. |
| -CreateTime | Long | 1747796654000 | The time when application token was created. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=ListApplicationTokens &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &ApplicationTokenType=bearer_token &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "ApplicationTokens":[
   "Status":"enabled",
   "ApplicationTokenId":"token_ndfxxigahelfne2y2hodehrxxxx",
   "Description":"jwqtts-0430",
   "InstanceId":"idaas_ki6hd7ihir4ybawogqk6kqxxxx",
   "LastUsedTime":1747796654000,
   "CreateTime":1747796654000,
   "ApplicationTokenType":"bearer_token",
"ApplicationToken":"SATFwqX8zxGf83pJcJw78KFGjmrft4erWeZYBGS8oE7NN6qoE217yaJpUdMb1UuuGqhDi 3sCA4CF91CTL5iGntqwyLuaAcS9FJ9HfGadE5a7TjiwVafwrBYktxxxx",
   "ApplicationId":"app_m7ar5tms4dwtggavalk3j3mxxxx",
   "ExpirationTime":1747796654000,
   "AliUid":1973166921975
```

`],`

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### ObtainApplicationToken

Queries an application token.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| Applicatio nTokenId | Strin g | Query | Yes | token sfrwerxxxxxxxxxx _ xxxx | The application token ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| ApplicationTok en | Struct | object | The application token. |
| -InstanceId | String | idaas ki6hd7ihir4y _ bawogqk6kqxxxx | The ID of the IDaaS EIAM instance. |
| -ApplicationId | String | app na2r73a65s7o _ 4zbs7nj5gxxxx | The application ID. |
| - ApplicationTok enId | String | token m7aso6v4ef _ vu2otfq3jdzxxxx | The application token ID. |
| - ApplicationTok enType | String | bearer token _ | The type of the application token. |
| - ApplicationTok en | String | SATFwqX8zxGf83pJ cJw78KFGjmrft4er WeZYBGS8oE7NN6 qoE217yaJpUdMb1 UuuGqhDiF43sCA4 CF91CTL5iGntqwyL uaAcS9FJ9HfGadE5 a7TjiwVafwrBxxxxx | The application token. |
| -Status | String | enabled | Specifies whether the application token is valid. |
| - ExpirationTim e | Long | 1735610950000 | The expiration time. |
| -LastUsedTime | Long | 1735610930000 | The time when the application token was used for the last time. |
| -CreateTime | Long | 1735610930000 | The time when the application token was created. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=ObtainApplicationToken &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &ApplicationTokenId=token_sfrwerxxxxxxxxxxxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "ApplicationToken":{
  "Status":"enabled",
  "ApplicationTokenId":"token_m7aso6v4efvu2otfq3jdzxxxx",
  "InstanceId":"idaas_ki6hd7ihir4ybawogqk6kqxxxx",
  "LastUsedTime":1735610930000,
  "CreateTime":1735610930000,
  "ApplicationTokenType":"bearer_token",
"ApplicationToken":"SATFwqX8zxGf83pJcJw78KFGjmrft4erWeZYBGS8oE7NN6qoE217yaJpUdMb1UuuGqhDi 3sCA4CF91CTL5iGntqwyLuaAcS9FJ9HfGadE5a7TjiwVafwrBxxxxx",
  "ApplicationId":"app_na2r73a65s7o4zbs7nj5gxxxx",
  "ExpirationTime":1735610950000
```

###### DeleteApplicationToken

Deletes an application token.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| Applicatio nTokenId | Strin g | Query | Yes | token sfrwerxxxxxxxxxx _ xxxx | The application token ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DeleteApplicationToken &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &ApplicationTokenId=token_sfrwerxxxxxxxxxxxxxx &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### Application accounts

###### AddApplicationAccountToUser

Adds an application account for an EIAM application.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | eiam-111ccc1111 | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app 11111 _ | The application ID. |
| UserId | Strin g | Query | Yes | user example _ | The user ID |
| Applicatio nUsernam e | Strin g | Query | Yes | zhangsan | The username of the application account. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| ApplicationAcc ountId | String | aac m6z7awz5kres _ i2ezgajsbkxxxx | The application account ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=AddApplicationAccountToUser &InstanceId=eiam-111ccc1111 &ApplicationId=app_11111 &UserId=user_example &ApplicationUsername=zhangsan &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "ApplicationAccountId":"aac_m6z7awz5kresi2ezgajsbkxxxx"
```

###### ListApplicationAccounts

Queries a list of application accounts that belong to an Employee Identity and Access Management (EIAM) application by page.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | eiam-111ccc1111 | The instance ID. |
| PageNum ber | Long | Query | No | 1 | The page number. |
| PageSize | Long | Query | No | 20 | The number of entries per page. |

| Developer Gui | de·API R | eference |   |   | IDaa |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Applicatio nId | Strin g | Query | Yes | app 11111 _ | The application ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Long | 100 | The total number of entries returned. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| ApplicationAcc ounts | Array | object | The details about the account. |
| -InstanceId | String | idaas eznwtkkauclj _ izh6qqu7ptxxxx | The ID of the EIAM instance. |
| -ApplicationId | String | app m43o4h5adeo _ 5klvbbxgxxxxx | The application ID. |
| - ApplicationAcc ountId | String | aac m66smhbq5kr _ ept7nza54hxxxx | The application account ID. |
| -UserId | String | user tkmboufpnvp _ bitdpzrlngxzxxxx | The user ID. |
| - ApplicationUse rname | String | test | The username of the account. |
| -CreateTime | Long | 1737510353000 | The time when the account was created. |
| - ApplicationUse rAttributes | Array | object | The user attributes. |
| -- AttributeName | String | sex | The attribute name. |
| -- AttributeType | String | Female | The attribute type. |
| -- AttributeValue Expression | String | user.username | The attribute. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=ListApplicationAccounts &InstanceId=eiam-111ccc1111 &ApplicationId=app_11111 &<Common request parameters>
```

Sample responses `JSON` format

```json
 "TotalCount":100,
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "ApplicationAccounts":[
   "InstanceId":"idaas_eznwtkkaucljizh6qqu7ptxxxx",
   "UserId":"user_tkmboufpnvpbitdpzrlngxzxxxx",
   "CreateTime":1737510353000,
   "ApplicationUserAttributes":[
     "AttributeValueExpression":"",
     "AttributeType":"",
     "AttributeName":""
```

`],`

```json
   "ApplicationId":"app_m43o4h5adeo5klvbbxgxxxxx",
   "ApplicationAccountId":"aac_m66smhbq5krept7nza54hxxxx",
   "ApplicationUsername":"test"
```

`]`

###### ListApplicationAccountsForUser

Queries all application accounts of a user for an Enterprise Identity Access Management (EIAM) application.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | eiam-111ccc1111 | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app 11111 _ | The application ID. |

|   | Developer Gui | de·API R | eference |   |   | IDaa | S |
|---|---|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| UserId | Strin g | Query | Yes | user example _ | The user ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Long | 100 | The total number of entries returned. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| ApplicationAcc ounts | Array | object | The information about application accounts. |
| -InstanceId | String | idaas ki6hd7ihir4y _ bawogqk6xxxxx | The ID of the EIAM instance. |
| -ApplicationId | String | app na2r76irswrwf _ gpkz7xvcj7xxxxx | The application ID. |
| - ApplicationAcc ountId | String | aac m6e3ukegwvb _ cb2fne7j32xxxxxx | The application account ID. |
| -UserId | String | user tkmboufpnvp _ bitdpzrlng6mxxxxx | The user ID. |
| - ApplicationUse rname | String | test | The name of the application account. |
| -CreateTime | Long | 1754359439000 | The creation time. |
| - ApplicationUse rAttributes | Array | object | Account attributes. |
| -- AttributeName | String | sex | The attribute name. |
| -- AttributeType | String | The ID card number. | The attribute type. |
| -- AttributeValue Expression | String | user.username | The expression that is used to generate the value of the attribute in the SAML assertion. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=ListApplicationAccountsForUser &InstanceId=eiam-111ccc1111 &ApplicationId=app_11111 &UserId=user_example &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "TotalCount":100,
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "ApplicationAccounts":[
   "InstanceId":"idaas_ki6hd7ihir4ybawogqk6xxxxx",
   "UserId":"user_tkmboufpnvpbitdpzrlng6mxxxxx",
   "CreateTime":1754359439000,
   "ApplicationUserAttributes":[
     "AttributeValueExpression":"",
     "AttributeType":"",
     "AttributeName":""
```

`],`

```json
   "ApplicationId":"app_na2r76irswrwfgpkz7xvcj7xxxxx",
   "ApplicationAccountId":"aac_m6e3ukegwvbcb2fne7j32xxxxxx",
   "ApplicationUsername":"test"
```

`]`

###### RemoveApplicationAccountFromUser

Deletes the application account of an employee under the current application.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | eiam-111ccc1111 | The instance ID. |

| Developer Gui | de·API R | eference |   |   | IDaa |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Applicatio nId | Strin g | Query | Yes | app 11111 _ | The application ID. |
| UserId | Strin g | Query | Yes | user example _ | The user ID. |
| Applicatio nAccountI d | Strin g | Query | Yes | act example _ | The application account ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=RemoveApplicationAccountFromUser &InstanceId=eiam-111ccc1111 &ApplicationId=app_11111 &UserId=user_example &ApplicationAccountId=act_example &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### Open API operations

###### EnableApplicationApiInvoke

Enables the Developer API feature for an application in Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=EnableApplicationApiInvoke &InstanceId= idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### DisableApplicationApiInvoke

Disables the Developer API feature for an Employee Identity and Access Management (EIAM) application.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DisableApplicationApiInvoke &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### SetApplicationGrantScope

Configures the permissions of the Developer API feature of an Employee Identity and Access Management (EIAM) application.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |

| DaaS |   |   |   | Dev | eloper Guide·API Referenc |
|---|---|---|---|---|---|
| Parame ter | Typ e | Positi on | Require d | Example | Description |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| GrantScop es | Array | Query | No | urn:alibaba:idaas:scope: user:read all _ | The permissions of the Developer API feature. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SetApplicationGrantScope &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### GetApplicationGrantScope

Queries the permissions of the Developer API feature of an Employee Identity and Access Management (EIAM) application.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| ApplicationGra ntScope | Struct | None | The permissions of the Developer API feature. |
| -GrantScopes | String | ["urn:alibaba:idaas :scope:user:read al _ l","urn:alibaba:idaa s:scope:user:mana geall"] | The permissions of the Developer API feature. Valid values: urn:alibaba:idaas:scope:user:read all: the _ permissions to query all users. urn:alibaba:idaas:scope:user:manage all: _ the permissions to manage all users. urn:alibaba:idaas:scope:organizational uni _ t:read all: the permissions to query all _ organizations. urn:alibaba:idaas:scope:organizational uni _ t:manage all: the permissions to manage _ all organizations. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetApplicationGrantScope &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "ApplicationGrantScope":{
  "GrantScopes":"
[\"urn:alibaba:idaas:scope:user:read_all\",\"urn:alibaba:idaas:scope:user:manageall\"]"
```

##### Application account synchronization

###### DisableApplicationProvisioning

Disables the account synchronization feature for an application in Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DisableApplicationProvisioning &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### EnableApplicationProvisioning

Enables the account synchronization feature for an Employee Identity and Access Management (EIAM) application.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=EnableApplicationProvisioning &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### SetApplicationProvisioningConfig

Configures the account synchronization feature for an Enterprise Identity Access Management (EIAM) application.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| ProvisionP rotocolTyp e | Strin g | Query | Yes | idaas callback _ | The type of account synchronization protocol . Valid values: idaas callback: _ custom event callback protocol of IDaaS. scim2: System for Cross-domain Identity Management (SCIM) protocol. |
| CallbackPr ovisioning Config | Struc t | Query | No | Struct | The configuration of event callback synchronization. This parameter is required when ProvisionProtocolType is set to idaas callback. _ |
| - CallbackU rl | Strin g |   | No | https://example.com/eve nt/callback | The URL that the application uses to receive IDaaS event callbacks. |
| - EncryptKe y | Strin g |   | No | ad3b248**************** **********b3561a73d7 | The symmetric encryption and decryption key for IDaaS event callbacks. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| - EncryptRe quired | Boole an |   | No | true | Specifies whether to encrypt IDaaS event callback messages. Valid values: true: encrypts the messages. false: transmits the messages in plaintext. |
| - ListenEve ntScopes | Array |   | No | system error _ | The types of IDaaS event callback messages that are supported by the listener. |
| ScimProvi sioningCo nfig | Struc t | Query | No | Struct | The configuration of SCIM-based IDaaS synchronization. This parameter is required when ProvisionProtocolType is set to scim2. |
| - ScimBase Url | Strin g |   | No | https://example.com/sci m | The base URL that the application uses to receive the SCIM protocol for IDaaS synchronization. |
| - AuthnConf iguration | Struc t |   | No | Struct | The configuration of SCIM-based synchronization. |
| -- AuthnMod e | Strin g |   | No | oauth2 | The authorization mode for the SCIM-based API operation. |
| -- GrantType | Strin g |   | No | bearer token _ | The grant type for the SCIM-based API operation. |
| -- AuthnPara m | Struc t |   | No | Struct | The configuration parameters related to authorization. |
| --- AccessTok en | Strin g |   | No | k52x2ru63rlkflina5utgkx xxx | The access token. |

| I | DaaS |   |   |   | Dev | eloper Guide·API Referenc | e |
|---|---|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| --- TokenEnd point | Strin g |   | No | https://www.example.co m/oauth/token | The token endpoint. |
| ---ClientId | Strin g |   | No | mkv7rgt4d7i4u7zqtzev2 mxxxx | The client ID of the application. |
| --- ClientSecr et | Strin g |   | No | CSEHDcHcrUKHw1CuxkJ EHPveWRXBGqVqRsxxx x | The client key secret of the application. |
| --- AuthnMet hod | Strin g |   | No | client secret basic _ _ | The authentication mode for the SCIM- based API operation. |
| - Provisioni ngActions | Array |   | No | rollback | The resource operations based on the SCIM protocol. |
| - FullPushS copes | Array |   | No | User:Read | The full synchronization scope of the SCIM protocol. |
| ProvisionP assword | Boole an | Query | No | true | Specifies whether to synchronize the password in IDaaS user event callbacks. Valid values: true: synchronizes the password. false: does not synchronize the password. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SetApplicationProvisioningConfig &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &ProvisionProtocolType=idaas_callback &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### SetApplicationProvisioningScope

Configures the account synchronization scope of an application in Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM). This scope is the same as the scope within which developers can call the Developer API operations to query and manage accounts.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| Organizati onalUnitId s | Array | Query | No | [ou wovwffm62xifdziem _ 7an7xxxxx] | The organizations that are authorized for account synchronization. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| GroupIds | Array | Query | No | group miu8e4t4d7i4u7u _ wezgr54xxxx | The account group IDs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SetApplicationProvisioningScope &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

###### GetApplicationProvisioningScope

Queries the account synchronization scope of an Employee Identity and Access Management (EIAM) application. This scope also specifies the accounts that Developer API can query and manage.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| ApplicationPro visioningScope | Struct | Struct | The account synchronization scope. |
| -UsedQuota | Integer | 150 | The quota used. |
| -MaxQuota | Integer | 100 | Indicates that the quota limit for a system or resource is 100, such as 100 users or 100 GB of storage space. |
| - Organizational UnitIds | String | [ou xxx001] _ | The organizations that are authorized for account synchronization. |
| -GroupIds | String | pg- 0000000000001,p g-0000000000002 | The group IDs. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetApplicationProvisioningScope &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "ApplicationProvisioningScope":{
  "GroupIds":"",
  "MaxQuota":"",
  "UsedQuota":"",
  "OrganizationalUnitIds":""
```

###### GetApplicationProvisioningConfig

Queries the configuration of the account synchronization feature for an application in Identityas-a-Service Enterprise Identity Access Management (IDaaS EIAM).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ApplicationPro visioningConfi g | Struct | Struct | The configuration of the account synchronization feature for the application. |
| -InstanceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The instance ID. |
| -ApplicationId | String | app mkv7rgt4d7i4 _ u7zqtzev2mxxxx | The application ID. |
| - ProvisionProto colType | String | idaas callback _ | The synchronization protocol type of the application. Valid values: idaas callback: custom event callback _ protocol of IDaaS. scim2: System for Cross-domain Identity Management (SCIM) protocol. |
| - ProvisionJwksE ndpoint | String | https://eiam-api- cn- hangzhou.aliyuncs. com/v2/idaas ue2j _ visn35ea5lmthk26 7xxxxx/app mkv7r _ gt4d7i4u7zqtzev2 mxxxx/provisioning /jwks | The public key endpoint for signature verification of the synchronization callback information. |
| - ProvisionPass word | Boolean | true | Specifies whether to synchronize the password in IDaaS user event callbacks. Valid values: true: synchronize the password. false: do not synchronize the password. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Status | String | enabled | The status of the IDaaS account synchronization feature. Valid values: enabled: The account synchronization feature is enabled. disabled: The account synchronization feature is disabled. |
| - ConfigOperate Mode | String | standard | The rendering mode of the account synchronization page. Valid values: standard: standard mode template: template mode |
| - CallbackProvisi oningConfig | Struct | Struct | The configuration of the custom event callback protocol of IDaaS. |
| --CallbackUrl | String | https://example.co m/event/callback | The URL that the application uses to receive IDaaS event callbacks. |
| --EncryptKey | String | 1adfdfdfd******111 | The symmetric encryption and decryption key for IDaaS event callbacks. |
| -- EncryptRequir ed | Boolean | true | Specifies whether to encrypt IDaaS event callback messages. Valid values: true: encrypt the messages. false: transmit the messages in plaintext. |
| -- ListenEventSc opes | String | deviceStatus | The types of IDaaS event callback messages that are supported by the listener. |
| - ScimProvisioni ngConfig | Struct | Struct | The configuration of SCIM-based IDaaS synchronization. |
| --ScimBaseUrl | String | https://example.co m/scim | The base URL that the application uses to receive the SCIM protocol for IDaaS synchronization. |
| -- ProvisioningAc tions | String | Detach | The resource operations based on the SCIM protocol. |
| -- FullPushScope s | String | exampleValue | The full synchronization scope based on the SCIM protocol. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -- AuthnConfigur ation | Struct | Struct | The configuration parameters related to SCIM-based synchronization. |
| ---AuthnMode | String | oauth2 | The authorization mode for the SCIM- based API operation. |
| ---GrantType | String | bearer token _ | The grant type for the SCIM-based API operation. |
| ---AuthnParam | Struct | Struct | The configuration parameters related to authorization. |
| ---- AccessToken | String | k52x2ru63rlkflina5 utgkxxxx | The access token. |
| ---- TokenEndpoint | String | https://www.examp le.com/oauth/token | The token endpoint. |
| ----ClientId | String | app mkv7rgt4d7i4 _ u7zqtzev2mxxxx | The client ID of the application. |
| ----ClientSecret | String | CSEHDcHcrUKHw1 CuxkJEHPveWRXBG qVqRsxxxx | The client key secret of the application. |
| ---- AuthnMethod | String | client secret basic _ _ | The authentication mode for the SCIM- based API operation. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetApplicationProvisioningConfig &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "ApplicationProvisioningConfig":{
  "ProvisionJwksEndpoint":"https://eiam-api-cn-
hangzhou.aliyuncs.com/v2/idaas_ue2jvisn35ea5lmthk267xxxxx/app_mkv7rgt4d7i4u7zqtzev2mxxxx/ ovisioning/jwks",
  "Status":"enabled",
  "ProvisionPassword":true,
  "CallbackProvisioningConfig":{
   "CallbackUrl":"",
   "EncryptKey":"",
   "ListenEventScopes":"",
   "EncryptRequired":""
```

`},`

```json
  "InstanceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
  "ScimProvisioningConfig":{
   "ScimBaseUrl":"",
   "ProvisioningActions":"",
   "AuthnConfiguration":{
    "AuthnParam":{
     "TokenEndpoint":"",
     "AuthnMethod":"",
     "AccessToken":"",
     "ClientSecret":"",
     "ClientId":""
```

`},`

```json
    "GrantType":"",
    "AuthnMode":""
```

`},`

```json
   "FullPushScopes":""
```

`},`

```json
  "ConfigOperateMode":"standard",
  "ApplicationId":"app_mkv7rgt4d7i4u7zqtzev2mxxxx",
  "ProvisionProtocolType":"idaas_callback"
```

`},`

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

#### Account management

##### CreateUser

Creates an account in Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM) for an IDaaS EIAM instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Username | Strin g | Query | Yes | user 001 _ | The name of the account. The name can be up to 64 characters in length and can contain letters, digits, underscores ( ), periods _ (.), at signs (@), and hyphens (-). |
| DisplayNa me | Strin g | Query | No | name 001 _ | The display name of the account. The display name can be up to 64 characters in length. |
| Password | Strin g | Query | No | 123456 | The password of the account. For more information about the password format, see the "Password Policies" topic. |
| PhoneRegi on | Strin g | Query | No | 86 | The area code of a mobile number. The area code contains 1 to 6 digits without the plus sign (+). |
| PhoneNu mber | Strin g | Query | No | 12345678901 | The mobile number. The mobile number must be 6 to 15 digits in length. |
| PhoneNu mberVerifi ed | Boole an | Query | No | true | Specifies whether the mobile number is a trusted mobile number. This parameter is required if the PhoneNumber parameter is specified. If you have no special business requirements, set this parameter to true. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Email | Strin g | Query | No | example@example.com | The email address. The prefix of the email address can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). The prefix can be up to 64 characters in length. |
| EmailVerif ied | Boole an | Query | No | true | Specifies whether the email address is a trusted email address. This parameter is required if the Email parameter is specified. If you have no special business requirements, set this parameter to true. |
| UserExter nalId | Strin g | Query | No | user d6sbsuumeta4h66 _ ec3il7yxxxx | The external ID of the account, which can be used to associate with an external system. The external ID can be up to 64 characters in length. If you do not specify this parameter, the external ID is the account ID. |
| PrimaryOr ganization alUnitId | Strin g | Query | Yes | ou wovwffm62xifdziem7 _ an7xxxxx | The ID of the primary organization. |
| Organizati onalUnitId s | Array | Query | No | [ou wovwffm62xifdziem _ 7an7xxxxx] | The IDs of organizations to which the account belongs. An account can belong to multiple organizations. |
| Descriptio n | Strin g | Query | No | description text | The description of the account. The description can be up to 256 characters in length. |
| CustomFie lds | Array | Query | No | description | The custom extended fields. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PasswordI nitializatio nConfig | Struc t | Query | No | Struct | The password initialization configurations. |
| - PasswordI nitializatio nPolicyPri ority | Strin g |   | No | true | The priority of the password initialization policy. |
| - PasswordF orcedUpd ateStatus | Strin g |   | No | false | Specifies whether to enable forcible password change upon first login. |
| - UserNotifi cationCha nnels | Array |   | No | sms | The methods for receiving password notifications. |
| - PasswordI nitializatio nType | Strin g |   | No | random | The password initialization method. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| UserId | String | user d6sbsuumeta _ 4h66ec3il7yxxxx | The account ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateUser &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &Username=user_001 &PrimaryOrganizationalUnitId=ou_wovwffm62xifdziem7an7xxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "UserId":"user_d6sbsuumeta4h66ec3il7yxxxx"
```

##### UpdateUser

Updates the basic information about an account in Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| UserId | Strin g | Query | Yes | user d6sbsuumeta4h66 _ ec3il7yxxxx | The account ID. |
| Username | Strin g | Query | No | username test _ | The name of the account. The name can be up to 64 characters in length and can contain letters, digits, underscores ( ), periods _ (.), at signs (@), and hyphens (-). |
| DisplayNa me | Strin g | Query | No | test name _ | The display name of the account. The display name can be up to 64 characters in length. |
| PhoneRegi on | Strin g | Query | No | 86 | The area code of the mobile number. For example, the area code of a mobile number in the Chinese mainland is 86, without 00 or the plus sign (+). This parameter is required if the PhoneNumber parameter is specified. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PhoneNu mber | Strin g | Query | No | 156xxxxxxxxx | The mobile number. The mobile number must be 6 to 15 digits in length. |
| PhoneNu mberVerifi ed | Boole an | Query | No | true | Indicates whether the mobile number is a trusted mobile number. This parameter is required if the PhoneNumber parameter is specified. If you have no special business requirements, set this parameter to true. |
| Email | Strin g | Query | No | example@example.com | The email address. The prefix of the email address can contain letters, digits, periods (.), underscores ( ), and _ hyphens (-). |
| EmailVerif ied | Boole an | Query | No | true | Indicates whether the email address is verified. This field is required if an email address is specified. If you have no special requirement, set this parameter to true. |
| CustomFie lds | Array | Query | No | {'StartTime':true, 'RuleName':true} | The custom extended fields. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateUser &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &UserId=user_d6sbsuumeta4h66ec3il7yxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### DeleteUser

Deletes an Enterprise Identity Access Management (EIAM) account. If you delete an EIAM account, the information related to the account is cleared.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| UserId | Strin g | Query | Yes | user d6sbsuumeta4h66 _ ec3il7yxxxx | The account ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteUser &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &UserId=user_d6sbsuumeta4h66ec3il7yxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### AddUserToOrganizationalUnits

Adds an Enterprise Identity Access Management (EIAM) account to multiple Identity as a Service (IDaaS) EIAM organizations. If the account already exists in an organization, a success response is returned.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| UserId | Strin g | Query | Yes | user d6sbsuumeta4h66 _ ec3il7yxxxx | The account ID. |
| Organizati onalUnitId s | Array | Query | Yes | [ou wovwffm62xifdziem _ 7an7xxxxx] | The organization IDs. You can add an account to a maximum of 100 organizations. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AddUserToOrganizationalUnits &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &UserId=user_d6sbsuumeta4h66ec3il7yxxxx &OrganizationalUnitIds= &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### RemoveUserFromOrganizationalUnits

Removes an account in Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM) from multiple IDaaS EIAM organizations. You cannot remove an account from a primary organization.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| UserId | Strin g | Query | Yes | user d6sbsuumeta4h66 _ ec3il7yxxxx | The account ID. |
| Organizati onalUnitId s | Array | Query | Yes | [ou wovwffm62xifdziem _ 7an7xxxxx] | The organization IDs. You can remove an account from a maximum of 100 organizations. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=RemoveUserFromOrganizationalUnits &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &UserId=user_d6sbsuumeta4h66ec3il7yxxxx &OrganizationalUnitIds= &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### UpdateUserPassword

Changes the password of an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS). The password must meet the complexity rules in the IDaaS console.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| UserId | Strin g | Query | Yes | user d6sbsuumeta4h66 _ ec3il7yxxxx | The account ID. |
| Password | Strin g | Query | Yes | 123456 | The new password of the account. For more information, refer to the complexity rules in the IDaaS console. |
| PasswordF orcedUpd ateStatus | Strin g | Query | No | enabled | Specifies whether to enable the forced password change feature. Default value: disabled. Valid values: enabled disabled |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| UserNotifi cationCha nnels | Array | Query | No | sms | The password notification method. Valid values: email sms |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateUserPassword &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &UserId=user_d6sbsuumeta4h66ec3il7yxxxx &Password=123456 &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### UpdateUserDescription

Modifies the description of an Enterprise Identity Access Management (EIAM) account.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| UserId | Strin g | Query | Yes | user d6sbsuumeta4h66 _ ec3il7yxxxx | The account ID. |
| Descriptio n | Strin g | Query | No | this is a test. | The description of the account. The description can be up to 256 characters in length. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateUserDescription &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &UserId=user_d6sbsuumeta4h66ec3il7yxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### DisableUser

Disables an Enterprise Identity Access Management (EIAM) account. If the account is already disabled, a success response is returned.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| UserId | Strin g | Query | Yes | user d6sbsuumeta4h66 _ ec3il7yxxxx | The ID of the account. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DisableUser &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &UserId=user_d6sbsuumeta4h66ec3il7yxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### EnableUser

Enables an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |

| DaaS |   |   |   | Dev | eloper Guide·API Referenc |
|---|---|---|---|---|---|
| Parame ter | Typ e | Positi on | Require d | Example | Description |
| UserId | Strin g | Query | Yes | user d6sbsuumeta4h66 _ ec3il7yxxxx | The account ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=EnableUser &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &UserId=user_d6sbsuumeta4h66ec3il7yxxxx &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### UnlockUser

Unlocks an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| UserId | Strin g | Query | Yes | user d6sbsuumeta4h66 _ ec3il7yxxxx | The account ID. |

| Developer Gui | de·API R | eference |   |   | IDaa |
|---|---|---|---|---|---|
| Parame ter | Typ e | Positi on | Require d | Example | Description |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UnlockUser &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &UserId=user_d6sbsuumeta4h66ec3il7yxxxx &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### SetUserPrimaryOrganizationalUnit

Configures the primary organization to which an Employee Identity and Access Management (EIAM) account belongs. The account is removed from its original primary organization and added to the new primary organization.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| UserId | Strin g | Query | Yes | user d6sbsuumeta4h66 _ ec3il7yxxxx | The account ID. |

| DaaS |   |   |   | Dev | eloper Guide·API Referenc |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Organizati onalUnitId | Strin g | Query | Yes | ou wovwffm62xifdziem7 _ an7xxxxx | The ID of the primary organization to which you want to add the account. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SetUserPrimaryOrganizationalUnit &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &UserId=user_d6sbsuumeta4h66ec3il7yxxxx &OrganizationalUnitId=ou_wovwffm62xifdziem7an7xxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### GetUser

Queries the detailed information about an Enterprise Identity Access Management (EIAM) account.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| UserId | Strin g | Query | Yes | user d6sbsuumeta4h66 _ ec3il7yxxxx | The ID of the account. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| User | Struct | Struct | The data object of the account. |
| -UserId | String | user d6sbsuumeta _ 4h66ec3il7yxxxx | The ID of the account. |
| -Username | String | name001 | The username of the account. |
| -DisplayName | String | display name001 _ | The display name of the account. |
| -PasswordSet | Boolean | false | Specifies whether a password is set. |
| -PhoneRegion | String | 86 | The country code of the mobile number. For example, the country code of China is 86 without 00 or a plus sign (+). |
| -PhoneNumber | String | 156xxxxxxx | The mobile number of the user who owns the account. |
| - PhoneNumber Verified | Boolean | true | Indicates whether the mobile number has been verified. A value of true indicates that the mobile number has been verified by the user or has been set to the verified status by the administrator. A value of false indicates that the mobile number has not been verified. |
| -Email | String | user@example.co m | The email address of the user who owns the account. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -EmailVerified | Boolean | true | Indicates whether the email address has been verified. A value of true indicates that the email address has been verified by the user or has been set to the verified status by the administrator. A value of false indicates that the email address has not been verified. |
| - UserExternalId | String | user d6sbsuumeta _ 4h66ec3il7yxxxx | The external ID of the account, which can be used to map external data to the data of the account in IDaaS EIAM. By default, the external ID is the account ID. Note: For accounts with the same source type and source ID, each account has a unique external ID. |
| - UserSourceTy pe | String | build in _ | The source type of the account. Valid values: build in: The account was created in _ IDaaS. ding talk: The account was imported _ from DingTalk. ad: The account was imported from Microsoft Active Directory (AD). ldap: The account was imported from a Lightweight Directory Access Protocol (LDAP) service. we com: The account was imported _ from WeCom. |
| -UserSourceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The source ID of the account. If the account was created in IDaaS, its source ID is the ID of the IDaaS instance. If the account was imported, its source ID is the enterprise ID in the source. For example, if the account was imported from DingTalk, its source ID is the corpId value of the enterprise in DingTalk. |
| -Status | String | enabled | The status of the account. Valid values: enabled: The account is enabled. disabled: The account is disabled. |
| - AccountExpire Time | Long | 1652085686179 | The time when the account expires. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| - PasswordExpir eTime | Long | 1652085686179 | The time when the password of the account expires. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. If a value -1 is returned, the password does not expire. If no value is returned, the password does not expire. If a UNIX timestamp is returned, the password expired at the point of time that the timestamp indicates. |
| -RegisterTime | Long | 1652085686179 | The time when the account was registered. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| - LockExpireTim e | Long | 1652085686179 | The time when the account lock expires. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| -CreateTime | Long | 1652085686179 | The time when the account was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| -UpdateTime | Long | 1652085686179 | The time when the account was last updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| -Description | String | Test account | The description of the account. |
| - PrimaryOrgani zationalUnitId | String | ou wovwffm62xifd _ ziem7an7xxxxx | The ID of the primary organizational unit to which the account belongs. |
| -InstanceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The instance ID. |
| -Locked | Boolean | false | Indicates whether the role is locked. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| - ExtensionAttri butes | Map | test | The extended information. |
| - PreferredLang uage | String | es | The preferred language of the user. |
| - Organizational Units | Array | Array | The organizational units to which the account belongs. |
| -- Organizational UnitId | String | ou wovwffm62xifd _ ziem7an7xxxxx | The ID of the organizational unit. |
| -- Organizational UnitName | String | test organizational _ Unit name _ | The name of the organizational unit. |
| --Primary | Boolean | true | Indicates whether the organization is the primary organization. |
| -CustomFields | Array | Array | The extended fields that describe the account. |
| --FieldName | String | age | The name of the extended field. |
| --FieldValue | String | 10 | The value of the extended field. |
| -Groups | Array | Array | The groups to which the account belongs. |
| --GroupId | String | group d6sbsuumet _ a4h66ec3il7yxxxx | The group ID. |
| --GroupName | String | Test organization | The group name. |
| --Description | String | Test organization | The group description. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetUser &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &UserId=user_d6sbsuumeta4h66ec3il7yxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "User":{
  "UserSourceType":"build_in",
  "Email":"user@example.com",
  "Description":"Test account",
  "AccountExpireTime":1652085686179,
  "PasswordExpireTime":1652085686179,
  "Locked":"",
  "ExtensionAttributes":"",
  "DisplayName":"display_name001",
  "PrimaryOrganizationalUnitId":"ou_wovwffm62xifdziem7an7xxxxx",
  "PreferredLanguage":"",
  "PhoneRegion":"86",
  "Status":"enabled",
  "PhoneNumberVerified":true,
  "InstanceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
  "CreateTime":1652085686179,
  "EmailVerified":true,
  "RegisterTime":1652085686179,
  "PasswordSet":false,
  "Username":"name001",
  "LockExpireTime":1652085686179,
  "UserId":"user_d6sbsuumeta4h66ec3il7yxxxx",
  "OrganizationalUnits":[
    "OrganizationalUnitId":"",
    "Primary":"",
    "OrganizationalUnitName":""
```

`],`

```json
  "CustomFields":[
    "FieldValue":"",
    "FieldName":""
```

`],`

```json
  "UpdateTime":1652085686179,
  "PhoneNumber":"156xxxxxxx",
  "Groups":[
    "GroupName":"",
    "Description":"",
    "GroupId":""
```

`],`

```json
  "UserSourceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
  "UserExternalId":"user_d6sbsuumeta4h66ec3il7yxxxx"
```

`},`

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### ListUsers

Queries the details of accounts in Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM) by page.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| PageNum ber | Long | Query | No | 1 | The page number. Default value: 1. |
| PageSize | Long | Query | No | 20 | The number of entries per page. Default value: 20. Maximum value: 100. |
| UserIds | Array | Query | No | user d6sbsuumeta4h66 _ ec3il7yxxxx | The account IDs. |
| Username StartsWith | Strin g | Query | No | name 001 _ | The prefix of the account name. The left match query is used. If you specify this parameter, the query follows the leftmost matching principle. |
| DisplayNa meStarts With | Strin g | Query | No | name | The prefix of the display name of the account. If you specify this parameter, the query follows the leftmost matching principle. |
| PhoneRegi on | Strin g | Query | No | 86 | The area code of the mobile number. For example, the area code of a mobile number in the Chinese mainland is 86, without 00 or the plus sign (+). |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PhoneNu mber | Strin g | Query | No | 156xxxxxxx | The mobile number of the user who owns the account. |
| Email | Strin g | Query | No | user@example.com | The email address of the user who owns the account. |
| UserExter nalId | Strin g | Query | No | id wovwffm62xifdziem7 _ an7xxxxx | The external ID of the account, which can be used to map external data to the data of the account in IDaaS EIAM. Note: For accounts with the same source type and source ID, each account has a unique external ID. |
| UserSourc eId | Strin g | Query | No | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The source ID of the account. If the account was created in IDaaS, its source ID is the ID of the IDaaS instance. If the account was imported, its source ID is the enterprise ID in the source. For example, if the account was imported from DingTalk, its source ID is the corpId value of the enterprise in DingTalk. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| UserSourc eType | Strin g | Query | No | build in _ | The source type of the account. Valid values: build in: The account _ was created in IDaaS. ding talk: The _ account was imported from DingTalk. ad: The account was imported from Microsoft Active Directory (AD). ldap: The account was imported from a Lightweight Directory Access Protocol (LDAP) service. we com: The account _ was imported from WeCom. |
| Status | Strin g | Query | No | enable | The status of the account. Valid values: enabled: The account is enabled. disabled: The account is disabled. |
| Organizati onalUnitId | Strin g | Query | No | ou wovwffm62xifdziem7 _ an7xxxxx | The organization ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Long | 100 | The total number of entries returned. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| Users | Array | Array | The queried accounts. |
| -UserId | String | user d6sbsuumeta _ 4h66ec3il7yxxxx | The account ID. |
| -Username | String | name001 | The name of the account. |

| DaaS |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -DisplayName | String | display name001 _ | The display name of the account. |
| -PasswordSet | Boolean | false | Indicates whether a password is set. |
| -PhoneRegion | String | 86 | The area code of the mobile number. For example, the area code of a mobile number in the Chinese mainland is 86, without 00 or the plus sign (+). |
| -PhoneNumber | String | 156xxxxxxx | The mobile number of the user who owns the account. |
| - PhoneNumber Verified | Boolean | true | Indicates whether the mobile number has been verified. A value of true indicates that the mobile number has been verified by the user or has been set to the verified status by the administrator. A value of false indicates that the mobile number has not been verified. |
| -Email | String | user@example.co m | The email address of the user who owns the account. |
| -EmailVerified | Boolean | true | Indicates whether the email address has been verified. A value of true indicates that the email address has been verified by the user or has been set to the verified status by the administrator. A value of false indicates that the email address has not been verified. |
| - UserExternalId | String | user d6sbsuumeta _ 4h66ec3il7yxxxx | The external ID of the account, which can be used to map external data to the data of the account in IDaaS EIAM. By default, the external ID is the account ID. Note: For accounts with the same source type and source ID, each account has a unique external ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| - UserSourceTy pe | String | build in _ | The source type of the account. Valid values: build in: The account was created in _ IDaaS. ding talk: The account was imported _ from DingTalk. ad: The account was imported from Microsoft AD. ldap: The account was imported from an LDAP service. |
| -UserSourceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The source ID of the account. If the account was created in IDaaS, its source ID is the ID of the IDaaS instance. If the account was imported, its source ID is the enterprise ID in the source. For example, if the account was imported from DingTalk, its source ID is the corpId value of the enterprise in DingTalk. |
| -Status | String | enabled | The status of the account. Valid values: enabled: The account is enabled. disabled: The account is disabled. |
| - AccountExpire Time | Long | 1652085686179 | The time when the account expires. This value is a UNIX timestamp. Unit: milliseconds. |
| - PasswordExpir eTime | Long | 1652085686179 | The time when the password expires. This value is a UNIX timestamp. Unit: milliseconds. |
| -RegisterTime | Long | 1652085686179 | The time when the account was registered. This value is a UNIX timestamp. Unit: milliseconds. |
| - LockExpireTim e | Long | 1652085686179 | The time when the account lock expires. This value is a UNIX timestamp. Unit: milliseconds. |
| -CreateTime | Long | 1652085686179 | The time when the account was created. This value is a UNIX timestamp. Unit: milliseconds. |
| -UpdateTime | Long | 1652085686179 | The time when the account was last modified. This value is a UNIX timestamp. Unit: milliseconds. |

| I | DaaS |   |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Description | String | Test organization | The description of the account. |
| -InstanceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The instance ID. |
| -Locked | Boolean | false | Indicates whether the account is locked. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListUsers &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "TotalCount":100,
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "Users":[
   "UserSourceType":"build_in",
   "Status":"enabled",
   "Email":"user@example.com",
   "Description":null,
   "PhoneNumberVerified":true,
   "InstanceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
   "CreateTime":1652085686179,
   "AccountExpireTime":1652085686179,
   "EmailVerified":true,
   "PasswordExpireTime":1652085686179,
   "RegisterTime":1652085686179,
   "Locked":"",
   "PasswordSet":false,
   "Username":"name001",
   "LockExpireTime":1652085686179,
   "UserId":"user_d6sbsuumeta4h66ec3il7yxxxx",
   "DisplayName":"display_name001",
   "UpdateTime":1652085686179,
   "PhoneNumber":"156xxxxxxx",
   "UserSourceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
   "UserExternalId":"user_d6sbsuumeta4h66ec3il7yxxxx",
   "PhoneRegion":"86"
```

`]`

#### Organization management

##### CreateOrganizationalUnit

Creates an organization in Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM) within a specific organization.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Organizati onalUnitN ame | Strin g | Query | Yes | test ou name _ _ | The name of the organization. The name can be up to 64 characters in length. |
| ParentId | Strin g | Query | Yes | ou wovwffm62xifdziem7 _ an7xxxxx | The parent organization ID. |
| Organizati onalUnitE xternalId | Strin g | Query | No | ou wovwffm62xifdziem7 _ an7xxxxx | The external ID of the organization, which can be used to associate the organization with an external system. By default, the external ID is the organization ID. The external ID can be up to 64 characters in length. |
| Descriptio n | Strin g | Query | No | description | The description of the organization. The description can be up to 256 characters in length. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Organizational UnitId | String | ou wovwffm62xifd _ ziem7an7xxxxx | The organization ID. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateOrganizationalUnit &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &OrganizationalUnitName=test_ou_name &ParentId=ou_wovwffm62xifdziem7an7xxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "OrganizationalUnitId":"ou_wovwffm62xifdziem7an7xxxxx",
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### Deletes an EIAM organization

Deletes an Employee Identity and Access Management (EIAM) organization in Identity as a Service (IDaaS). If the organization contains EIAM accounts or child organizations, the delete operation fails.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Organizati onalUnitId | Strin g | Query | Yes | ou wovwffm62xifdziem7 _ an7xxxxx | The organization ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteOrganizationalUnit &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &OrganizationalUnitId=ou_wovwffm62xifdziem7an7xxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### UpdateOrganizationalUnit

Updates the basic information about an organization in Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM). By default, if you do not specify the request parameters, the organization is not modified.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Organizati onalUnitId | Strin g | Query | Yes | ou wovwffm62xifdziem7 _ an7xxxxx | The organization ID. |
| Organizati onalUnitN ame | Strin g | Query | No | ou name _ | The name of the organization. The name can be up to 64 characters in length and must be unique in the same parent organization. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateOrganizationalUnit &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &OrganizationalUnitId=ou_wovwffm62xifdziem7an7xxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### DeleteOrganizationalUnitChildren

Deletes information about an Employee Identity and Access Management (EIAM) organization and forcefully deletes all accounts and sub-organizations in the organization.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Organizati onalUnitId | Strin g | Query | Yes | ou wovwffm62xifdziem7 _ an7xxxxx | The organization ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteOrganizationalUnitChildren &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &OrganizationalUnitId=ou_wovwffm62xifdziem7an7xxxxx &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### UpdateOrganizationalUnitParentId

Updates the parent organization ID of an organization in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM). In this case, the organization is moved from a parent node to a new node.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Organizati onalUnitId | Strin g | Query | Yes | ou wovwffm62xifdziem7 _ an7xxxxx | The organization ID. |
| ParentId | Strin g | Query | Yes | ou wovwffm62xifdziem7 _ an7xxxxx | The parent organization ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateOrganizationalUnitParentId &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &OrganizationalUnitId=ou_wovwffm62xifdziem7an7xxxxx &ParentId=ou_wovwffm62xifdziem7an7xxxxx &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### UpdateOrganizationalUnitDescription

Modifies the description of an Employee Identity and Access Management (EIAM) organization.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Organizati onalUnitId | Strin g | Query | Yes | ou wovwffm62xifdziem7 _ an7xxxxx | The organization ID. |
| Descriptio n | Strin g | Query | No | organizationalUnit test _ | The description of the organization. The value can be up to 256 characters in length. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateOrganizationalUnitDescription &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &OrganizationalUnitId=ou_wovwffm62xifdziem7an7xxxxx &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### Query the information about the root EIAM

**organization in IDaaS**

Queries the information about the root Employee Identity and Access Management (EIAM) organization in Identity as a Service (IDaaS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Organizational Unit | Struct | Struct | The data objects of the organization. |

| DaaS |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -InstanceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The instance ID. |
| - Organizational UnitId | String | ou wovwffm62xifd _ ziem7an7xxxxx | The EIAM organization ID. |
| - Organizational UnitName | String | name001 | The organization name. |
| -CreateTime | Long | 1652085686179 | The time when the organizational unit was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| -UpdateTime | Long | 1652085686179 | The time when the organizational unit was last updated. The value is a UNIX timestamp. Unit: milliseconds. |
| -Description | String | Test organization | The organization description. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetRootOrganizationalUnit &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &<Common request parameters>
```

Sample success responses

```
 JSON format
```

```json
 "OrganizationalUnit":{
  "OrganizationalUnitId":"ou_wovwffm62xifdziem7an7xxxxx",
  "Description":"Test organization",
  "InstanceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
  "CreateTime":1652085686179,
  "UpdateTime":1652085686179,
  "OrganizationalUnitName":"name001"
```

`},`

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### Queries the information about an EIAM

**organization.**

Queries the information about an Employee Identity and Access Management (EIAM) organization in Identity as a Service (IDaaS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Organizati onalUnitId | Strin g | Query | Yes | ou wovwffm62xifdziem7 _ an7xxxxx | The organization ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Organizational Unit | Struct | Struct | The information about the array object. |
| - Organizational UnitId | String | ou wovwffm62xifd _ ziem7an7xxxxx | The organization ID. |
| - Organizational UnitName | String | test organizational _ Unit name _ | The organization name. |

| DaaS |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -ParentId | String | ou wovwffm62xifd _ ziem7an7xxxxx | The parent organization ID. |
| - Organizational UnitExternalId | String | ou wovwffm62xifd _ ziem7an7xxxxx | The external ID of the organization. The external ID can be used to map external data to the data of the EIAM organization in IDaaS. By default, the external ID is the organization ID. For organizations with the same source type and source ID, each organization has a unique external ID. |
| - Organizational UnitSourceTyp e | String | build in _ | The source type of the account. Valid values: build in: The account was created in _ IDaaS. ding talk: The organization was _ imported from DingTalk. ad: The organization was imported from Microsoft Active Directory (AD). ldap: The organization was imported from a Lightweight Directory Access Protocol (LDAP) service. we com: The organization was imported _ from WeCom. |
| - Organizational UnitSourceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The source ID of the organization. If the organization was created in IDaaS, its source ID is the ID of the IDaaS instance. If the organization was imported, its source ID is the enterprise ID in the source. For example, if the organization was imported from DingTalk, its source ID is the corpId value of the enterprise in DingTalk. |
| -CreateTime | Long | 1652085686179 | The time when the organization was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| -UpdateTime | Long | 1652085686179 | The time when the organization was last updated. The value is a UNIX timestamp. Unit: milliseconds. |
| -Description | String | Test organization | The organization description. |
| -InstanceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The instance ID. |

|   | Developer Guide·A | PI Reference |   | IDaa | S |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Leaf | Boolean | false | Indicates whether the organization is a leaf node. A leaf node indicates that the organization has no child nodes. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetOrganizationalUnit &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &OrganizationalUnitId=ou_wovwffm62xifdziem7an7xxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "OrganizationalUnit":{
  "OrganizationalUnitId":"ou_wovwffm62xifdziem7an7xxxxx",
  "ParentId":"ou_wovwffm62xifdziem7an7xxxxx",
  "Description":"Test organization",
  "InstanceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
  "CreateTime":1652085686179,
  "UpdateTime":1652085686179,
  "OrganizationalUnitSourceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
  "Leaf":false,
  "OrganizationalUnitName":"test_organizationalUnit_name",
  "OrganizationalUnitExternalId":"ou_wovwffm62xifdziem7an7xxxxx",
  "OrganizationalUnitSourceType":"build_in"
```

`},`

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### Query information about EIAM

**organizations in a list**

Queries the information of Employee Identity and Access Management (EIAM) organizations of Identity as a Service (IDaaS) by page.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| PageNum ber | Long | Query | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Long | Query | No | 20 | The number of entries to return on each page. Default value: 20. Maximum value: 100. |
| Organizati onalUnitId s | Array | Query | No | [ou wovwffm62xifdziem _ 7an7xxxxx] | The organization IDs. You can specify a maximum of 100 organization IDs. |
| Organizati onalUnitN ame | Strin g | Query | No | name 001 _ | The organization name. If you specify this parameter, exact match applies to this query. |
| Organizati onalUnitN ameStarts With | Strin g | Query | No | name | The prefix of the organization name. If you specify this parameter, the query follows the leftmost matching principle. |
| ParentId | Strin g | Query | No | ou wovwffm62xifdziem7 _ an7xxxxx | The parent organization ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Long | 1000 | The total number of entries returned. The maximum number of entries returned at a time depends on the value of PageSize. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Organizational Units | Array | Struct | The queried organizations. |
| - Organizational UnitId | String | ou wovwffm62xifd _ ziem7an7xxxxx | The EIAM organization ID. |
| - Organizational UnitName | String | test organizational _ Unit name _ | The name of the organization. |
| -ParentId | String | ou wovwffm62xifd _ ziem7an7xxxxx | The parent organization ID. |
| - Organizational UnitExternalId | String | ou wovwffm62xifd _ ziem7an7xxxxx | The external ID of the organization. The external ID can be used to map external data to the data of the EIAM organization in Identity as a Service (IDaaS). By default, the external ID is the organization ID. For organizations with the same source type and source ID, each organization has a unique external ID. |
| - Organizational UnitSourceTyp e | String | build in _ | The source type of the organization. Valid values: build in: The organization was created _ in IDaaS. ding talk: The organization was _ imported from DingTalk. ad: The organization was imported from Microsoft Active Directory (AD). ldap: The organization was imported from a Lightweight Directory Access Protocol (LDAP) service. we com: The organization was imported _ from WeCom. |
| - Organizational UnitSourceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The source ID of the organization. |
| -CreateTime | Long | 1652085686179 | The time at which the organization was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| -UpdateTime | Long | 1652085686179 | The last time at which the organization was updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Description | String | Test organization | The organization description. |
| -InstanceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The instance ID. |
| -Leaf | Boolean | false | Indicates whether the organization is a leaf node. A leaf node indicates that the organization has no child nodes. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListOrganizationalUnits &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &<Common request parameters>
```

Sample success responses

```json
 JSON format
 "TotalCount":1000,
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "OrganizationalUnits":[
   "OrganizationalUnitId":"ou_wovwffm62xifdziem7an7xxxxx",
   "ParentId":"ou_wovwffm62xifdziem7an7xxxxx",
   "Description":"Test organization",
   "InstanceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
   "CreateTime":1652085686179,
   "UpdateTime":1652085686179,
   "OrganizationalUnitSourceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
   "Leaf":false,
   "OrganizationalUnitName":"test_organizationalUnit_name",
   "OrganizationalUnitExternalId":"ou_wovwffm62xifdziem7an7xxxxx",
   "OrganizationalUnitSourceType":"build_in"
```

`]`

##### ListOrganizationalUnitParents

Queries a list of all parent organizations of an organization in Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM). The results are sorted in descending order based on the level of the parent organizations of the IDaaS EIAM organization.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Organizati onalUnitId | Strin g | Query | Yes | ou wovwffm62xifdziem7 _ an7xxxxx | The organization ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| Parents | Array | Array | The parent organizations. |
| - Organizational UnitId | String | ou 4lag76zc2km5s _ sg5vsmm2lznvu | The organization ID. |
| -ParentId | String | ou x3beoyepv2ls5i _ wuge3xhjkwbm | The parent organization ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListOrganizationalUnitParents &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &OrganizationalUnitId=ou_wovwffm62xifdziem7an7xxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "Parents":[
   "OrganizationalUnitId":"ou_4lag76zc2km5ssg5vsmm2lznvu",
   "ParentId":"ou_x3beoyepv2ls5iwuge3xhjkwbm"
```

`]`

#### account group management

##### Create an EIAM account group in IDaaS

Creates an Employee Identity and Access Management (EIAM) account group in Identity as a Service (IDaaS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| GroupNa me | Strin g | Query | Yes | name test _ | The group name. The name can be up to 64 characters in length. |
| GroupExte rnalId | Strin g | Query | No | group d6sbsuumeta4h6 _ 6ec3il7yxxxx | The external ID of the group, which can be used to associate the group with an external system. By default, the external ID is the group ID. The value can be up to 64 characters in length. |
| Descriptio n | Strin g | Query | No | this is a test. | The group description. The description can be up to 256 characters in length. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| GroupId | String | group d6sbsuumet _ a4h66ec3il7yxxxx | The group ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateGroup &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &GroupName=name_test &<Common request parameters>
```

Sample success responses

```json
 JSON format
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "GroupId":"group_d6sbsuumeta4h66ec3il7yxxxx"
```

##### AddUsersToGroup

Adds Employee Identity and Access Management (EIAM) accounts of Identity as a Service (IDaaS) to an EIAM account group.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |

| DaaS |   |   |   | Dev | eloper Guide·API Referenc |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| GroupId | Strin g | Query | Yes | group d6sbsuumeta4h6 _ 6ec3il7yxxxx | The group ID. |
| UserIds | Array | Query | Yes | [ou 001] _ | The account IDs. A maximum of 100 accounts can be specified. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AddUsersToGroup &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &GroupId=group_d6sbsuumeta4h66ec3il7yxxxx &UserIds=[ou_001] &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### DeleteGroup

Deletes the information of an account group in Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| GroupId | Strin g | Query | Yes | group d6sbsuumeta4h6 _ 6ec3il7yxxxx | The account group ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteGroup &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &GroupId=group_d6sbsuumeta4h66ec3il7yxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### RemoveUsersFromGroup

Removes multiple accounts in Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM) from an IDaaS EIAM account group.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |

| DaaS |   |   |   | Dev | eloper Guide·API Referenc |
|---|---|---|---|---|---|
| Parame ter | Typ e | Positi on | Require d | Example | Description |
| GroupId | Strin g | Query | Yes | group d6sbsuumeta4h6 _ 6ec3il7yxxxx | The account group ID. |
| UserIds | Array | Query | Yes | [ou 001] _ | The account IDs. A maximum of 100 accounts can be removed from an account group. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=RemoveUsersFromGroup &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &GroupId=group_d6sbsuumeta4h66ec3il7yxxxx &UserIds=[ou_001] &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### UpdateGroup

Updates the information about an account group in Employee Identity and Access Management (EIAM) of Identity as a Service (IDaaS). If the information is empty, the account group is not updated by default.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| GroupId | Strin g | Query | Yes | group d6sbsuumeta4h6 _ 6ec3il7yxxxx | The group ID. |
| GroupNa me | Strin g | Query | No | name test _ | The group name. |
| GroupExte rnalId | Strin g | Query | No | group d6sbsuumeta4h6 _ 6ec3il7yxxxx | The group external ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateGroup &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &GroupId=group_d6sbsuumeta4h66ec3il7yxxxx &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### UpdateGroupDescription

Updates the description of an Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM) account group.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| GroupId | Strin g | Query | Yes | group d6sbsuumeta4h6 _ 6ec3il7yxxxx | The group ID. |
| Descriptio n | Strin g | Query | No | group d6sbsuumeta4h6 _ 6ec3il7yxxxx | The description of the account group. The value can be up to 256 characters in length. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateGroupDescription &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &GroupId=group_d6sbsuumeta4h66ec3il7yxxxx &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### GetGroup

Queries the details of an account group in Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| GroupId | Strin g | Query | Yes | group d6sbsuumeta4h6 _ 6ec3il7yxxxx | The account group ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Group | Struct | Struct | The information about the account group. |
| -GroupId | String | group d6sbsuumet _ a4h66ec3il7yxxxx | The account group ID. |
| -GroupName | String | group name _ | The name of the account group. |
| -Description | String | test group _ | The description of the account group. |
| - GroupExternalI d | String | group d6sbsuumet _ a4h66ec3il7yxxxx | The external ID of the account group, which can be used to associate the account group with an external system. By default, the external ID is the account group ID. |
| - GroupSourceT ype | String | build in _ | The source type of the account group. Only build in may be returned, which _ indicates that the group was created in IDaaS. Valid value: build in: The account group was created _ in IDaaS. |
| - GroupSourceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The source ID of the account group. By default, the source ID is the instance ID. |
| -CreateTime | Long | 1652085686179 | The time when the account group was created. This value is a UNIX timestamp. Unit: milliseconds. |
| -UpdateTime | Long | 1652085686179 | The time when the account group was last updated. This value is a UNIX timestamp. Unit: milliseconds. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -InstanceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The instance ID. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetGroup &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &GroupId=group_d6sbsuumeta4h66ec3il7yxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "Group":{
  "GroupName":"group_name",
  "Description":"test_group",
  "InstanceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
  "CreateTime":1652085686179,
  "UpdateTime":1652085686179,
  "GroupExternalId":"group_d6sbsuumeta4h66ec3il7yxxxx",
  "GroupSourceType":"build_in",
  "GroupSourceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
  "GroupId":"group_d6sbsuumeta4h66ec3il7yxxxx"
```

`},`

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### ListGroups

Queries a list of account groups in Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM)).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| PageNum ber | Long | Query | No | 1 | The page number. |
| PageSize | Long | Query | No | 20 | The number of entries per page. |
| GroupIds | Array | Query | No | [group miu8e4t4d7i4u7 _ uwezgr54xxxx] | The account group IDs. |
| GroupNa me | Strin g | Query | No | name test _ | The name of the account group. If you specify this parameter, the query is based on an exact match. |
| GroupNa meStarts With | Strin g | Query | No | name | The prefix of the name of the account group. If you specify this parameter, the query follows the leftmost matching principle. |
| GroupExte rnalId | Strin g | Query | No | group external id _ _ | The external ID of the account group. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Long | 100 | The total number of entries returned. The maximum number of entries returned at a time depends on the value of PageSize. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| Groups | Array | Array | The queried account groups. |
| -GroupId | String | group d6sbsuumet _ a4h66ec3il7yxxxx | The account group ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -GroupName | String | group name _ | The name of the account group. |
| -Description | String | test group | The description of the account group. |
| - GroupExternalI d | String | group d6sbsuumet _ a4h66ec3il7yxxxx | The external ID of the account group, which can be used to associate the account group with an external system. By default, the external ID is the account group ID. |
| - GroupSourceT ype | String | build in _ | The source type of the account group. Only build in may be returned, which _ indicates that the group was created in IDaaS. Valid value: build in: The account group was created _ in IDaaS. |
| - GroupSourceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The source ID of the account group. If the account group was imported from other services, this value indicates the external source ID. By default, the source ID is the instance ID. |
| -CreateTime | Long | 1652085686179 | The time when the account group was created. This value is a UNIX timestamp. Unit: milliseconds. |
| -UpdateTime | Long | 1652085686179 | The time when the account group was last updated. This value is a UNIX timestamp. Unit: milliseconds. |
| -InstanceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The instance ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListGroups &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "TotalCount":100,
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "Groups":[
   "GroupName":"group_name",
   "Description":"test group",
   "InstanceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
   "CreateTime":1652085686179,
   "UpdateTime":1652085686179,
   "GroupExternalId":"group_d6sbsuumeta4h66ec3il7yxxxx",
   "GroupSourceType":"build_in",
   "GroupSourceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
   "GroupId":"group_d6sbsuumeta4h66ec3il7yxxxx"
```

`]`

##### ListUsersForGroup

Queries a list of accounts that belong to an account group in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| PageNum ber | Long | Query | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Long | Query | No | 20 | The number of entries to return on each page. Default value: 20. Maximum value: 100. |
| GroupId | Strin g | Query | Yes | group d6sbsuumeta4h6 _ 6ec3il7yxxxx | The group ID. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| UserIds | Array | Query | No | [ou 001] _ | The account IDs. A maximum of 100 accounts can be queried. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Long | 1000 | The total number of entries returned. The maximum number of entries returned at a time depends on the value of PageSize. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| Users | Array | Array | The users who own the accounts. |
| -UserId | String | user d6sbsuumeta _ 4h66ec3il7yxxxx | The account ID. |
| - GroupMember RelationSourc eId | String | 1001 | The identifier of the source of the group member relationship generated by the system. |
| - GroupMember RelationSourc eType | String | USER ADDED _ | The group member relationship generated by the system, such as the default group. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListUsersForGroup &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &GroupId=group_d6sbsuumeta4h66ec3il7yxxxx &<Common request parameters>
```

Sample responses `JSON` format

```json
 "TotalCount":1000,
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "Users":[
   "UserId":"user_d6sbsuumeta4h66ec3il7yxxxx",
   "GroupMemberRelationSourceId":"",
   "GroupMemberRelationSourceType":""
```

`]`

##### ListGroupsForUser

Queries a list of account groups to which an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS) belongs.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| PageNum ber | Long | Query | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Long | Query | No | 20 | The number of entries to return on each page. Default value: 20. Maximum value: 100. |
| UserId | Strin g | Query | Yes | user d6sbsuumeta4h66 _ ec3il7yxxxx | The ID of the Apsara Stack tenant account. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Long | 1000 | The total number of entries returned. The maximum number of entries returned at a time depends on the value of PageSize. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| Groups | Array | Array | The list of account groups to which the account belongs. |
| -GroupId | String | group d6sbsuumet _ a4h66ec3il7yxxxx | The ID of the account group. |
| - GroupMember RelationSourc eId | String | idaas igc5glpu2ye _ 7x5iyagkppizxxx | The ID of the source of the group member relationship. |
| - GroupMember RelationSourc eType | String | build in _ | The type of the source of the group members. |

Sample requests

```
http(s)://[Endpoint]/?Action=ListGroupsForUser &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &UserId=user_d6sbsuumeta4h66ec3il7yxxxx &<Common request parameters>
```

Sample responses `JSON` format

```json
 "TotalCount":1000,
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "Groups":[
   "GroupMemberRelationSourceId":"",
   "GroupMemberRelationSourceType":"",
   "GroupId":"group_d6sbsuumeta4h66ec3il7yxxxx"
```

`]`

#### IdP management

##### Create an identity provider

Creates an identity provider (IdP).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| IdentityPr oviderNa me | Strin g | Query | Yes | test | The name of the IdP. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| IdentityPr oviderTyp e | Strin g | Query | Yes | urn:alibaba:idaas:idp:ali baba:dingtalk:push | The synchronization type of the IdP. Valid values: Pull data from DingTalk: urn:alibaba:idaas:idp: alibaba:dingtalk:pull Push data to DingTalk: urn:alibaba:idaas:idp: alibaba:dingtalk:push Pull data from WeCom: urn:alibaba:idaas:idp: tencent:wecom:pull Pull data from Lark: urn:alibaba:idaas:idp: bytedance:lark:pull Pull data from Microsoft Active Directory (AD): urn:alibaba:idaas:idp: microsoft:ad:pull Pull from a Lightweight Directory Access Protocol (LDAP) service: urn:alibaba:idaas:idp: unknown:ldap:pull Standard OpenID Connect (OIDC): urn:alibaba:idaas:idp: standard:oidc OIDC customized for Secure Access Service Edge (SASE): urn:alibaba:idaas:idp: alibaba:sase |
| UdPushCo nfig | Struc t | Query | No | Struct | The configuration push settings. |
| - Increment alCallback Status | Strin g |   | No | enabled | The status of incremental callback. |
| - PeriodicSy ncStatus | Strin g |   | No | disabled | The status of scheduled synchronization. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| - UdSyncSc opeConfig s | Array |   | No | Array | The UD synchronization scope. |
| -- UdSyncSc opeConfig sItem | Struc t |   | No | Struct | The UD synchronization configurations. |
| --- SourceSco pes | Array |   | No | OU=test,DC=idaas,DC= com | The source scope. |
| --- TargetSco pe | Strin g |   | No | ou 6zczfw67fqqpxwcoqa _ 27nuhxxx | The target scope. |
| UdPullCon fig | Struc t | Query | No | Struct | The pulling configurations. |
| - GroupSyn cStatus | Strin g |   | No | disabled | The group synchronization status. |
| - Increment alCallback Status | Strin g |   | No | disabled | The status of incremental synchronization. |
| - PeriodicSy ncStatus | Strin g |   | No | disabled | The status of scheduled synchronization. |
| - UdSyncSc opeConfig | Struc t |   | Yes | Struct | The UD synchronization scope. |
| -- SourceSco pes | Array |   | No | OU=test,DC=idaas,DC= com | The source scope. |
| -- TargetSco pe | Strin g |   | No | ou 6zczfw67fqqpxwcoqa _ 27nuhxxx | The target scope. |
| AuthnConf ig | Struc t | Query | No | Struct | The authentication configurations. |
| - AuthnStat us | Strin g |   | Yes | enabled | The authentication status. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| - AutoUpda tePasswor dStatus | Strin g |   | No | enabled | The status of automatic password update. |
| BindingCo nfig | Struc t | Query | No | Struct | The OIDC IdP account association rule. |
| - AutoMatc hUserProfi leExpressi ons | Array |   | No | Struct | The expression that is used to automatically match user profiles. |
| -- AutoMatc hUserProfi leExpressi onsItem | Struc t |   | No | Struct | The expression that is used to match user profiles. |
| --- Expressio nMapping Type | Strin g |   | Yes | expression | The type of the expression. |
| --- SourceVal ueExpress ion | Strin g |   | Yes | appUser.username | The value expression of the source field. |
| --- TargetFiel d | Strin g |   | Yes | username | The name of the mapped field. |
| --- TargetFiel dDescripti on | Strin g |   | No | Update time | The description of the mapped field. |
| - AutoMatc hUserStat us | Strin g |   | No | enabled | Specifies whether to enable automatic account matching. |
| - MappingBi ndingStat us | Strin g |   | No | enabled | Specifies whether to enable manual account association. |
| DingtalkA ppConfig | Struc t | Query | No | Struct | The DingTalk configurations. |
| -AppKey | Strin g |   | No | rX7zNFbJbGnneg1H2DdI oS73y****** | The AppKey. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| - AppSecret | Strin g |   | No | 1r0ElNPFqLI6qgY08***** ************************* *9TIK3RN 5fk9SEMO _ | The AppSecret. |
| -CorpId | Strin g |   | No | 10001 | The tenant ID. |
| - DingtalkV ersion | Strin g |   | No | 6.0.0 | The current version number of DingTalk. |
| LdapConfi g | Struc t | Query | No | Struct | The AD or LDAP configurations. |
| - Administr atorPassw ord | Strin g |   | No | Admin@123xxx | The password of the administrator account. |
| - Administr atorUsern ame | Strin g |   | No | admin | The name of the system administrator account. |
| - Certificate Fingerprin tStatus | Strin g |   | No | disabled | Specifies whether to verify the certificate fingerprint. |
| - Certificate Fingerprin ts | Array |   | No | A1:B2:C3:D4:E5:F6:G7:H 8:I9:J0 | The certificate fingerprint. |
| - GroupMe mberAttri buteName | Strin g |   | No | memberId | The group member identifier. |
| - GroupObj ectClass | Strin g |   | No | top,group | The group ObjectClass. |
| - GroupObj ectClassC ustomFilte r | Strin g |   | No | test=123 | The group custom filter. |
| - LdapProto col | Strin g |   | No | ldap://internal.example.c om:3890 | The standard protocol that is used to access the LDAP service, which is typically used for authentication and directory queries. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| - LdapServe rHost | Strin g |   | No | ldap.example.com | The hostname or IP address of the LDAP server that is used to establish connections to the LDAP service. |
| - LdapServe rPort | Integ er |   | No | 389 | The default port used by LDAP. |
| - Organizati onUnitObj ectClass | Strin g |   | No | top | The organization ObjectClass. |
| - StartTlsSt atus | Strin g |   | No | disabled | Specifies whether to enable StartTLS. |
| - UserLoginI dentifier | Strin g |   | No | test | The user login identifier. |
| - UserObjec tClass | Strin g |   | No | User001 | The user ObjectClass. |
| - UserObjec tClassCust omFilter | Strin g |   | No | test=123 | The user-defined filter. |
| WeComCo nfig | Struc t | Query | No | Struct | The WeCom configurations. |
| -AgentId | Strin g |   | No | agent@ccc-test | The client ID. |
| - Authorize CallbackD omain | Strin g |   | No | https://callback.example .com/callback | The authorized callback domain. |
| -CorpId | Strin g |   | No | 10001 | The tenant ID. |
| - CorpSecre t | Strin g |   | No | 8h3nF9kLmQxPxxx | The credential key of WeCom. |
| - Trustable Domain | Strin g |   | No | example.com | A sample domain name. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| OidcConfi g | Struc t | Query | No | Struct | The configurations of the OIDC IdP. |
| - AuthnPara m | Struc t |   | No | Struct | The authentication parameters. |
| -- AuthnMet hod | Strin g |   | No | client secret basic _ _ | The supported client secret _ authentication methods. Valid values: client secret basic and _ _ client secret post. _ _ |
| --ClientId | Strin g |   | No | mkv7rgt4d7i4u7zqtzev2 mxxxx | The client ID of the application. |
| -- ClientSecr et | Strin g |   | No | CSEHDcHcrUKHw1CuxkJ EHPveWRXBGqVqRsxxx x | The client secret of the application. |
| - EndpointC onfig | Struc t |   | No | Struct | The endpoint configurations. |
| -- Authorizat ionEndpoi nt | Strin g |   | No | http://example.com/auth | The authorization endpoint. |
| --Issuer | Strin g |   | No | test | The issuer of the certificate. |
| --JwksUri | Strin g |   | No | http://example.com/jwks | The JSON Web Key Set (JWKS) URL of the OIDC issuer. |
| -- TokenEnd point | Strin g |   | No | https://www.example.co m/oauth/token | The token endpoint. |
| -- UserinfoE ndpoint | Strin g |   | No | https://api.example.com/ userinfo | The user information endpoint. |
| - GrantScop es | Array |   | No | profile,email | The valid authorization scope. The value is subject to the OIDC standards and separated by commas (,). |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| - GrantType | Strin g |   | No | token | The return types supported by implicit grant flows. Use OIDC parameters, such as token and id token. _ |
| - PkceChall engeMeth od | Strin g |   | No | S256 | The supported Proof Key for Code Exchange (PKCE) algorithms. |
| - PkceRequi red | Boole an |   | No | true | Specifies whether to enforce PKCE. |
| NetworkA ccessEndp ointId | Strin g | Query | No | nae examplexxxx _ | The ID of the network endpoint. |
| AutoCreat eUserConf ig | Struc t | Query | No | Struct | The configurations of automatic account creation. |
| - AutoCreat eUserStat us | Strin g |   | No | disabled | Specifies whether to automatically create users. |
| - TargetOrg anizationa lUnitIds | Array |   | No | OU123456 | The node at which accounts are automatically created. |
| AutoUpda teUserCon fig | Struc t | Query | No | Struct | The rules of automatic account update. |
| - AutoUpda teUserStat us | Strin g |   | No | disabled | Specifies whether to enable automatic account update. |
| LarkConfi g | Struc t | Query | No | Struct | The Lark configuration. |
| -AppId | Strin g |   | No | 2dfea044-479f-464a- b374-f14d32****** | The application ID. |
| - AppSecret | Strin g |   | No | 1r0ElNPFqLI6qgY08***** ************************* *9TIK3RN 5fk9SEMO _ | The AppSecret. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| - Enterprise Number | Strin g |   | No | test | The enterprise code of your custom Lark application. |
| LogoUrl | Strin g | Query | No | xxxx- image://xxxx 23aqr2ye5 _ 54csg33dqpch5eu3q/tm p/d17d9adc-a943-45e7- ba0c-2838dddea678 | The URL of the application logo. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| IdentityProvid erId | String | idp mwpcwnhrimlr _ 2horxXXXX | The IdP ID. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

Sample requests

```
http(s)://[Endpoint]/?Action=CreateIdentityProvider &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &IdentityProviderName=test &IdentityProviderType=urn:alibaba:idaas:idp:alibaba:dingtalk:push &<Common request parameters>
```

Sample success responses

```json
 JSON format
 "IdentityProviderId":"idp_mwpcwnhrimlr2horxXXXX",
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### Delete an IdP

Deletes an identity provider (IdP).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| IdentityPr oviderId | Strin g | Query | Yes | idp my664lwkhpicbyziro _ g3xxxxx | The IdP ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteIdentityProvider &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &IdentityProviderId=idp_my664lwkhpicbyzirog3xxxxx &<Common request parameters>
```

Sample success responses

```json
 JSON format
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### UpdateIdentityProvider

Updates the basic configuration of an IdP.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| IdentityPr oviderId | Strin g | Query | Yes | idp my664lwkhpicbyziro _ g3xxxxx | The ID of the Identity Provider (IdP). |
| IdentityPr oviderNa me | Strin g | Query | No | test | The name of the IdP. |
| LdapConfi g | Struc t | Query | No | Struct | The basic Active Directory (AD) and Lightweight Directory Access Protocol (LDAP) information. |
| - Administr atorPassw ord | Strin g |   | No | Admin@123xxx | The password of the administrator account. |
| - Administr atorUsern ame | Strin g |   | No | admin | The default username of the administrator account. |
| - Certificate Fingerprin tStatus | Strin g |   | No | test | The fingerprinting status of the certificate. |
| - Certificate Fingerprin ts | Array |   | No | A1:B2:C3:D4:E5:F6:G7:H 8:I9:J0 | The fingerprint of the certificate. |
| - LdapProto col | Strin g |   | No | ldap://example.com:389 | Specifies LDAP to access data within a directory. |
| - LdapServe rHost | Strin g |   | No | ldap.example.com | The hostname or IP address of the LDAP server. |
| - LdapServe rPort | Integ er |   | No | 389 | The default port used by LDAP. |
| - StartTlsSt atus | Strin g |   | No | false | Specifies whether to enable TLS. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| DingtalkA ppConfig | Struc t | Query | No | Struct | The basic DingTalk configuration. |
| -AppKey | Strin g |   | Yes | rX7zNFbJbGnneg1H2DdI oS73y****** | The AppKey. |
| - AppSecret | Strin g |   | Yes | 1r0ElNPFqLI6qgY08***** ************************* *9TIK3RN 5fk9SEMO _ | The AppSecret. |
| WeComCo nfig | Struc t | Query | No | Struct | The Enterprise WeChat information. |
| -AgentId | Strin g |   | No | 202526561358712105 | The client ID. |
| - Authorize CallbackD omain | Strin g |   | No | example.com | The domain name that is used to receive authorization callbacks. |
| - CorpSecre t | Strin g |   | No | 8h3nF9kLmxxx | The internal key used for encryption. |
| - Trustable Domain | Strin g |   | No | example.com | Specifies whether the domain name is a trusted domain name. |
| OidcConfi g | Struc t | Query | No | Struct | The OpenID Connect (OIDC)-related configuration. |
| - AuthnPara m | Struc t |   | No | Struct | The authentication parameters. |
| -- AuthnMet hod | Strin g |   | No | client secret basic _ _ | The authentication method. |
| -- ClientSecr et | Strin g |   | No | CSEHDcHcrUKHw1CuxkJ EHPveWRXBGqVqRsxxx x | The client secret of the application. |
| - EndpointC onfig | Struc t |   | No | Struct | The endpoint configuration. |
| -- Authorizat ionEndpoi nt | Strin g |   | No | http://localhost:8080/oa uth/token | The authentication endpoint. |

| Developer Gui | de·API R | eference |   |   | IDaa |
|---|---|---|---|---|---|
| Parame ter | Typ e | Positi on | Require d | Example | Description |
| --Issuer | Strin g |   | No | test | The issuer. |
| --JwksUri | Strin g |   | No | test | The JSON Web Key (JWK) endpoint. |
| -- TokenEnd point | Strin g |   | No | https://www.example.co m/oauth/token | The token endpoint. |
| -- UserinfoE ndpoint | Strin g |   | No | https://api.example.com/ userinfo | The user information endpoint. |
| - GrantScop es | Array |   | No | ["urn:alibaba:idaas:scop e:user:read all","urn:alib _ aba:idaas:scope:user:m anageall"] | The permissions on API operations. |
| - GrantType | Strin g |   | No | bearer token _ | The authorization type. |
| - PkceChall engeMeth od | Strin g |   | No | test | The Proof Key for Code Exchange (PKCE) challenge method. |
| - PkceRequi red | Boole an |   | No | true | Specifies whether application Single Sign- On (SSO) forcefully requires PKCE. |
| NetworkA ccessEndp ointId | Strin g | Query | No | nae examplexxxx _ | The ID of the network endpoint. |
| LarkConfi g | Struc t | Query | No | Struct | The Lark configuration. |
| -AppId | Strin g |   | No | 2dfea044-479f-464a- b374-f14d32****** | The application ID. |
| - AppSecret | Strin g |   | No | 1r0ElNPFqLI6qgY08***** ************************* *9TIK3RN 5fk9SEMO _ | The AppSecret. |
| LogoUrl | Strin g | Query | No | idaas- image://idaas 23aqr2ye _ 554csg33dqpch5exxxx/t mp/d17d9adc-a943- 45e7-ba0c- 2838dddea678xxxx | The URL of the application logo. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateIdentityProvider &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &IdentityProviderId=idp_my664lwkhpicbyzirog3xxxxx &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### Obtain an IdP

Obtains an identity provider (IdP).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| IdentityPr oviderId | Strin g | Query | Yes | idp my664lwkhpicbyziro _ g3xxxxx | The IdP ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| IdentityProvid erDetail | Struct | Struct | The information about the IdP. |
| - AdvancedStat us | String | disabled | The advanced features. Valid values: disabled enabled |
| - AuthnSourceS upplier | String | urn:alibaba:idaas:i dp:bytedance:lark | The source authentication service, such as Okta, Google, and Azure Active Directory (AD). Valid values: DingTalk: urn:alibaba:idaas:idp:alibaba:dingtalk LDAP: urn:alibaba:idaas:idp:unknown:ldap Apsara Stack IDaaS: urn:alibaba:idaas:idp:alibaba:idaas WeCom: urn:alibaba:idaas:idp:tencent:wecom Lark: urn:alibaba:idaas:idp:bytedance:lark Microsoft AD: urn:alibaba:idaas:idp:microsoft:ad Azure AD: urn:alibaba:idaas:idp:microsoft:aad Apsara Stack Secure Access Service Edge (SASE): urn:alibaba:idaas:idp:alibaba:sase |
| - AuthnSourceT ype | String | urn:alibaba:idaas:a uthntype:oidc | The authentication method, such as OIDC and SAML. Valid values: OIDC: urn:alibaba:idaas:authntype:oidc SAML: urn:alibaba:idaas:authntype:saml2 |
| -AuthnStatus | String | disabled | Specifies whether the corresponding IdP supports authentication. Valid values: disabled enabled |
| -CreateTime | Long | 1726021079000 | The time when the IdP is created. The value is a UNIX timestamp. Unit: milliseconds. |

| DaaS |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Description | String | for poc test | The IdP description. |
| - IdentityProvid erExternalId | String | idp xxxx _ | The external ID of the IdP. |
| - IdentityProvid erId | String | idp mwpcwnhrimlr _ 2horx7xgg7pp7y | The IdP ID. |
| - IdentityProvid erName | String | test | The IdP name. |
| - IdentityProvid erType | String | urn:alibaba:idaas:i dp:alibaba:dingtalk :push | The synchronization type of the IdP. Valid values: Pull data from DingTalk: urn:alibaba:idaas:idp:alibaba:dingtalk:p ull Push data to DingTalk: urn:alibaba:idaas:idp:alibaba:dingtalk:p ush Pull data from WeCom: urn:alibaba:idaas:idp:tencent:wecom:pu ll Pull data from Lark: urn:alibaba:idaas:idp:bytedance:lark:pul l Pull data from Microsoft AD: urn:alibaba:idaas:idp:microsoft:ad:pull Pull data from LDAP: urn:alibaba:idaas:idp:unknown:ldap:pull Standard OIDC: urn:alibaba:idaas:idp:standard:oidc OIDC customized for SASE: urn:alibaba:idaas:idp:alibaba:sase |
| -InstanceId | String | idaas x2df3bak3u _ wnapqm6xxxx | The instance ID. |
| - LastStatusChe ckJobResult | String | success | The result of the last status check. |
| -LockReason | String | financial | The reason why the IdP is locked. |
| - NetworkAcces sEndpointId | String | nae mx4vsadfe6go _ vkqkwckxxxx | The ID of the network endpoint. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -UdPullStatus | String | disabled | Specifies whether the IdP supports data pulling. Valid values: disabled enabled |
| -UdPushStatus | String | disabled | Specifies whether data push is enabled for the IdP. Valid values: disabled enabled |
| -UpdateTime | Long | 1726021079000 | The time when the IdP is updated. The value is a UNIX timestamp. Unit: milliseconds. |
| -LogoUrl | String | https://img.alicdn.c om/imgextra/i4/O1 CN01lvYwpv1aGow QXDML9 !!600000 _ 0003303-0-tps- 580-580.jpg | The address of the custom IdP Logo. |
| - DingtalkAppCo nfig | Struct | DingTalk basic configuration | The basic DingTalk configuration. |
| --AppKey | String | 41reopmwoy9s | The AppKey of DingTalk. |
| --AppSecret | String | REOQ6Cl55kriOd8 NOBeqWYLKpHR4p 6fdZxxxx | The AppSecret of DingTalk. |
| --CorpId | String | 375604363323769 0761 | The CorpID of DingTalk. |
| -- DingtalkVersio n | String | public dingtalk _ | The version of DingTalk. Valid values: DingTalk Standard: public dingtalk _ DingTalk Exclusive: private dingtalk _ |
| - DingtalkProvisi oningConfig | Struct | Authorized DingTalk department | The authorized DingTalk department. |
| --CorpId | String | ding xxxxx _ | The CorpID of the DingTalk. |
| --CorpName | String | Test enterprise | The DingTalk corporate name. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -- AuthedDepart mentIds | Array | Authorized DingTalk department | The authorized DingTalk department. |
| ---DeptId | String | 123xxx444 | The ID of the DingTalk department. |
| ---DeptName | String | Test department | The name of the DingTalk department. |
| --AuthedUsers | Array | List of authorized DingTalk accounts | A list of authorized DingTalk accounts. |
| ---Name | String | Victor XX | The name of the DingTalk user. |
| ---UserId | String | 130308333929200 479 | The user ID of the DingTalk user. |
| -LarkConfig | Struct | Lark configuration | The Lark configuration. |
| --AppId | String | cli a7a99f53a3171 _ 00c | The CorpID of the self-managed application in Lark. |
| --AppSecret | String | *** | The AppSecret of the self-managed application in Lark. |
| -- EnterpriseNum ber | String | FX1231xxxx | The enterprise code of Lark. |
| -LdapConfig | Struct | Information about the AD or LDAP IdP | The information about the AD or LDAP IdP. |
| -- AdministratorP assword | String | Admin@123 | The AD or LDAP administrator password. |
| -- Administrator Username | String | admin | The AD or LDAP administrator account. |
| -- CertificateFing erprintStatus | String | enable | Specifies whether to verify the thumbprint certificate. Valid values: disabled enabled |
| --LdapProtocol | String | ldap | The communication protocol of AD or LDAP. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -- LdapServerHo st | String | 127.xx.xx.100 | The address of the ADor LDAP server. |
| -- LdapServerPor t | Integer | 389 | The AD/LDAP service port. |
| -- StartTlsStatus | String | enable | Specifies whether StartTLS is enabled. Valid values: disabled enabled |
| -- CertificateFing erprints | String | ["sdfsadfasdfk","as dsadaasd"] | The certificate fingerprints. |
| -OidcConfig | Struct | Configuration of the OIDC IdP | The configuration of the OIDC IdP. |
| --GrantType | String | authorization code _ | The OIDC authorization type. |
| -- PkceChallenge Method | String | S256 | The PKCE algorithm. Valid values: S256: SHA256 plain: plaintext |
| -- PkceRequired | Boolean | true | Specifies whether to use PKCE in AuthorizationCode mode. |
| --GrantScopes | String | ["ou asdaq1addsxz _ dq1xxxx","ou abcd _ efghdsxzdq1xxxx"] | The OIDC authorization scope. |
| --AuthnParam | Struct | Configurations of OIDC client authentication | The configurations of OIDC client authentication. |
| --- AuthnMethod | String | client secret post _ _ | The OIDC authentication method. |
| ---ClientId | String | mkv7rgt4d7i4u7zq tzev2mxxxx | The ID of the OIDC client. |
| ---ClientSecret | String | CSEHDddddddxxxx uxkJEHPveWRXBGq VqRsxxxx | OIDC client key |
| -- EndpointConfi g | Struct | The OIDC endpoint. | The OIDC endpoint. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| --- AuthorizationE ndpoint | String | https://example.co m/oauth/authorize | The OIDC authorization endpoint. |
| ---Issuer | String | https://example.co m/oauth | The information about the OIDC issuer. |
| ---JwksUri | String | https://example.co m/oauth/jwks | The JSON Web Key Set (JWKS) URL of the OIDC issuer. |
| --- TokenEndpoint | String | https://example.co m/oauth/token | The OIDC token endpoint. |
| --- UserinfoEndpo int | String | https://example.co m/oauth/userinfo | The OIDC UserInfo endpoint. |
| -UdPullConfig | Struct | Pulling configuration | The pulling configurations. |
| -- GroupSyncStat us | String | enabled | Specifies whether group synchronization is enabled. Valid values: disabled enabled |
| -- IncrementalCa llbackStatus | String | enabled | The status of incremental callback. This parameter specifies whether to process incremental callback data from the IdP. Valid values: disabled enabled |
| -- UdSyncScopeC onfig | Struct | Synchronization scope | The synchronization scope. |
| ---TargetScope | String | ou 123xxxx _ | The synchronization target. |
| --- SourceScopes | String | ["ou 123xxxx","ou _ _ 123xxxx"] | A list of synchronization sources. |
| -UdPushConfig | Struct | Push configuration | The push configuration. |
| -- IncrementalCa llbackStatus | String | disabled | This field is not in use. Ignore it. |
| -- UdSyncScopeC onfigs | Array | A list of synchronization scopes. | A list of synchronization scopes. |

|   | Developer Guide·A | PI Reference |   | IDaa | S |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ---TargetScope | String | ou 123xxxx _ | The synchronization target. |
| --- SourceScopes | String | [""ou xxx,"ou xxxx _ _ "] | A list of synchronization sources. |
| -WeComConfig | Struct | WeCom configuration | The WeCom configuration. |
| --AgentId | String | 1242350 | The ID of the self-managed application in WeCom. |
| -- AuthorizeCallb ackDomain | String | https://example.co m/xxxx | The authorized callback domain. |
| --CorpId | String | 356201295345457 7801 | The CorpID of the self-managed application in WeCom. |
| --CorpSecret | String | weaseiszjskejskaj1 2sjeszojxxxx | The CorpSecret of the self-managed application in WeCom. |
| -- TrustableDom ain | String | https://example.co m | The trusted domain name. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetIdentityProvider &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &IdentityProviderId=idp_my664lwkhpicbyzirog3xxxxx &<Common request parameters>
```

Sample success responses

```json
 JSON format
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "IdentityProviderDetail":{
  "AuthnSourceSupplier":"urn:alibaba:idaas:idp:bytedance:lark",
  "Description":"for poc test",
  "IdentityProviderId":"idp_mwpcwnhrimlr2horx7xgg7pp7y",
  "AuthnStatus":"disabled",
"LogoUrl":"https://img.alicdn.com/imgextra/i4/O1CN01lvYwpv1aGowQXDML9_!!6000000003303-0 -tps-580-580.jpg",
  "IdentityProviderName":"test",
  "LarkConfig":{
   "AppId":"cli_a7a99f53a317100c",
"EnterpriseNmber""FX1231
```

`"`

```json
   "EnterpriseNumber":"FX1231xxxx",
   "AppSecret":"***"
```

`},`

```json
  "AuthnSourceType":"urn:alibaba:idaas:authntype:oidc",
  "AdvancedStatus":"disabled",
  "UdPushStatus":"disabled",
  "OidcConfig":{
   "PkceRequired":true,
   "AuthnParam":{
    "AuthnMethod":"client_secret_post",
    "ClientSecret":"CSEHDddddddxxxxuxkJEHPveWRXBGqVqRsxxxx",
    "ClientId":"mkv7rgt4d7i4u7zqtzev2mxxxx"
```

`},`

```json
   "GrantScopes":"[\"ou_asdaq1addsxzdq1xxxx\",\"ou_abcdefghdsxzdq1xxxx\"]",
   "EndpointConfig":{
    "JwksUri":"https://example.com/oauth/jwks",
    "TokenEndpoint":"https://example.com/oauth/token",
    "Issuer":"https://example.com/oauth",
    "UserinfoEndpoint":"https://example.com/oauth/userinfo",
    "AuthorizationEndpoint":"https://example.com/oauth/authorize"
```

`},`

```json
   "GrantType":"authorization_code",
   "PkceChallengeMethod":"S256"
```

`},`

```json
  "IdentityProviderType":"urn:alibaba:idaas:idp:alibaba:dingtalk:push",
  "LockReason":"financial",
  "UdPushConfig":{
   "UdSyncScopeConfigs":[
     "SourceScopes":"[\"\"ou_xxx,\"ou_xxxx\"]",
     "TargetScope":"ou_123xxxx"
```

`],`

```json
   "IncrementalCallbackStatus":"disabled"
```

`},`

```json
  "InstanceId":"idaas_x2df3bak3uwnapqm6xxxx",
  "CreateTime":1726021079000,
  "NetworkAccessEndpointId":"nae_mx4vsadfe6govkqkwckxxxx",
  "WeComConfig":{
   "TrustableDomain":"https://example.com",
   "CorpId":"3562012953454577801",
   "AgentId":"1242350",
   "CorpSecret":"weaseiszjskejskaj12sjeszojxxxx",
   "AuthorizeCallbackDomain":"https://example.com/xxxx"
```

`},`

```json
  "LastStatusCheckJobResult":"success",
  "DingtalkAppConfig":{
   "CorpId":"3756043633237690761",
   "AppKey":"41reopmwoy9s",
   "DingtalkVersion":"public_dingtalk",
   "AppSecret":"REOQ6Cl55kriOd8NOBeqWYLKpHR4p6fdZxxxx"
```

`},`

```json
  "DingtalkProvisioningConfig":{
   "AuthedDepartmentIds":[
```

```json
     "DeptName":"Test department",
     "DeptId":"123xxx444"
```

`],`

```json
   "CorpId":"ding_xxxxx",
   "CorpName":"Test enterprise",
   "AuthedUsers":[
     "UserId":"130308333929200479",
     "Name":"Victor XX"
```

`]` `},`

```json
  "UdPullStatus":"disabled",
  "UpdateTime":1726021079000,
  "LdapConfig":{
   "CertificateFingerprints":"[\"sdfsadfasdfk\",\"asdsadaasd\"]",
   "LdapProtocol":"ldap",
   "StartTlsStatus":"enable",
   "LdapServerPort":389,
   "CertificateFingerprintStatus":"enable",
   "AdministratorPassword":"Admin@123",
   "LdapServerHost":"127.xx.xx.100",
   "AdministratorUsername":"admin"
```

`},`

```json
  "UdPullConfig":{
   "UdSyncScopeConfig":{
    "SourceScopes":"[\"ou_123xxxx\",\"ou_123xxxx\"]",
    "TargetScope":"ou_123xxxx"
```

`},`

```json
   "GroupSyncStatus":"enabled",
   "IncrementalCallbackStatus":"enabled"
```

`},`

```json
  "IdentityProviderExternalId":"idp_xxxx"
```

##### ListIdentityProviders

Queries the list of identity providers (IdPs).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| PageNum ber | Long | Query | No | 1 | The page number. |
| PageSize | Long | Query | No | 20 | The number of entries per page. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Long | 100 | The total number of entries returned. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| IdentityProvid ers | Array | Array | The information about IdPs. |
| -InstanceId | String | idaas pbf4dth34l2 _ qb7mydpntXXX | The instance ID. |
| - IdentityProvid erId | String | idp m5b5wd5s2hp _ q4t6iaehhXXX | The IdP ID. |
| - IdentityProvid erExternalId | String | test 123 _ | The external ID of the IdP. |
| -Description | String | Test organization | The description of the IdP. |
| - IdentityProvid erName | String | JWT | The name of the IdP. |
| -UdPullStatus | String | disabled | Indicates whether pulling is supported. Valid values: disabled enabled |

| Parameter | Type | Example | Description |
|---|---|---|---|
| - AuthnSourceT ype | String | urn:alibaba:idaas:a uthntype:oidc | The authentication method. Valid values: urn:alibaba:idaas:idp:standard:oidc: OIDC urn:alibaba:idaas:authntype:saml2: SAML |
| - AuthnSourceS upplier | String | urn:alibaba:idaas:i dp:bytedance:lark | The corresponding authenticated source service. Valid values: urn:alibaba:idaas:idp:alibaba:dingtalk: DingTalk urn:alibaba:idaas:idp:unknown:ldap: LDAP urn:alibaba:idaas:idp:alibaba:idaas: IDaaS urn:alibaba:idaas:idp:tencent:wecom: WeCom urn:alibaba:idaas:idp:bytedance:lark: Lark urn:alibaba:idaas:idp:microsoft:ad: Active Directory (AD) urn:alibaba:idaas:idp:microsoft:aad: Azure Active Directory urn:alibaba:idaas:idp:alibaba:sase: SASE |
| -AuthnStatus | String | disabled | Indicates whether the corresponding IdP supports authentication. Valid values: disabled enabled |
| - IncrementalCa llbackStatus | String | enabled | The status of incremental callbacks, which are used to handle incremental callback data from the IdP. Valid values: disabled enabled |
| - UdPullTargetS cope | String | ou 2buqmxsa3ltyq _ kjgpwfijurXXX | The synchronization target. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| - IdentityProvid erType | String | urn:alibaba:idaas:i dp:bytedance:lark: pull | The synchronization type of the IdP. Valid values: urn:alibaba:idaas:idp:alibaba:dingtalk:p ull: pulls data from DingTalk. urn:alibaba:idaas:idp:alibaba:dingtalk:p ush: pushes data to DingTalk. urn:alibaba:idaas:idp:tencent:wecom:pu ll: pulls data from WeCom. urn:alibaba:idaas:idp:bytedance:lark:pul l: pulls data from Lark. urn:alibaba:idaas:idp:microsoft:ad:pull: pulls data from AD. urn:alibaba:idaas:idp:unknown:ldap:pull : pulls data from LDAP. urn:alibaba:idaas:idp:standard:oidc: standard OIDC. urn:alibaba:idaas:idp:alibaba:sase: OIDC customized for SASE. |
| - AdvancedStat us | String | disabled | Indicates whether advanced settings are enabled. Valid values: disabled enabled |
| -UdPushStatus | String | disabled | Indicates whether pushing is enabled. Valid values: disabled enabled |
| -LockReason | String | financial | The lock reason. |
| - LastStatusChe ckJobResult | String | success | The last status check result. The synchronization task can be triggered only when the status check result of the IdP is success. |
| -CreateTime | Long | 1712561597000 | The time when the IdP was created. The value is a UNIX timestamp. Unit: milliseconds. |
| -UpdateTime | Long | 1712561597000 | The time when the IdP was updated. The value is a UNIX timestamp. Unit: milliseconds. |
| -LogoUrl | String | https://cdn-cn- hangzhou.aliyunida as.com/xx/logos/xx | The URL of the custom logo of the IdP. |

| Developer Guide·A | PI Reference |   | IDaa |
|---|---|---|---|
| Parameter | Type | Example | Description |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListIdentityProviders &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &<Common request parameters>
```

Sample responses `JSON` format

```json
 "TotalCount":100,
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "IdentityProviders":[
   "IdentityProviderId":"idp_m5b5wd5s2hpq4t6iaehhXXX",
   "Description":null,
   "AuthnSourceSupplier":"urn:alibaba:idaas:idp:bytedance:lark",
   "InstanceId":"idaas_pbf4dth34l2qb7mydpntXXX",
   "AuthnStatus":"disabled",
   "LogoUrl":"https://cdn-cn-hangzhou.aliyunidaas.com/xx/logos/xx",
   "CreateTime":1712561597000,
   "IdentityProviderName":"",
   "UdPullTargetScope":"ou_2buqmxsa3ltyqkjgpwfijurXXX",
   "AuthnSourceType":"urn:alibaba:idaas:authntype:oidc",
   "LastStatusCheckJobResult":"success",
   "AdvancedStatus":"disabled",
   "UdPushStatus":"disabled",
   "UdPullStatus":"disabled",
   "UpdateTime":1712561597000,
   "IdentityProviderExternalId":"test_123",
   "IdentityProviderType":"urn:alibaba:idaas:idp:bytedance:lark:pull",
   "LockReason":"financial",
   "IncrementalCallbackStatus":"enabled"
```

`]`

##### Disable data push from an IdP

Disable data push from an identity provider (IdP).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| IdentityPr oviderId | Strin g | Query | Yes | idp my664lwkhpicbyziro _ g3xxxxx | The IdP ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

Sample requests

```
http(s)://[Endpoint]/?Action=DisableIdentityProviderUdPull &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &IdentityProviderId=idp_my664lwkhpicbyzirog3xxxxx &<Common request parameters>
```

Sample success responses

```json
 JSON format
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### Enable synchronization from an IdP

This topic describes how to enable synchronization from an identity provider (IdP).

**Request header**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| IdentityPr oviderId | Strin g | Query | Yes | idp my664lwkhpicbyziro _ g3xxxxx | The IdP ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=EnableIdentityProviderUdPull &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &IdentityProviderId=idp_my664lwkhpicbyzirog3xxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### SetIdentityProviderUdPullConfiguration

Modifies the inbound synchronization configuration for an identity provider (IdP).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |

| I | DaaS |   |   |   | Dev | eloper Guide·API Referenc | e |
|---|---|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| IdentityPr oviderId | Strin g | Query | Yes | idp my664lwkhpicbyziro _ g3xxxxx | The IdP ID. |
| Increment alCallback Status | Strin g | Query | Yes | disabled | The status of incremental callback. This parameter specifies whether to process incremental callback data from the IdP. Valid values: disabled enabled |
| GroupSyn cStatus | Strin g | Query | No | disabled | The status of group synchronization. Valid values: disabled enabled |
| UdSyncSc opeConfig | Struc t | Query | No | object | The inbound synchronization configuration. |
| - SourceSco pes | Array |   | No | ["ou asdaq1addsxzdq1X _ XX","ou asdaq1addsxzd _ q1XXX"] | The list of source nodes for synchronization. |
| - TargetSco pe | Strin g |   | No | ou asdaq1addsxzdq1XX _ X | The destination node for synchronization. |
| PullProtec tedRule | Struc t | Query | No | object | The inbound synchronization protection rule. |
| - UserDelet edThresho ld | Integ er |   | No | 30 | The threshold for the number of users to be deleted. If the number of users to be deleted exceeds this value, the synchronization task is stopped. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| - Organizati onalUnitD eletedThr eshold | Integ er |   | No | 10 | The threshold for the number of organizations to be deleted. If the number of organizations to be deleted exceeds this value, the synchronization task is stopped. |
| - GroupDel etedThres hold | Integ er |   | No | 10 | The threshold for the number of groups to be deleted. If the number of groups to be deleted exceeds this value, the synchronization task is stopped. |
| LdapUdPul lConfig | Struc t | Query | No | object | The configurations of LDAP synchronization. |
| - UserObjec tClass | Strin g |   | No | userPrincipalName, mail | The user ObjectClass. |
| - Organizati onUnitObj ectClass | Strin g |   | No | organizationUnit,top | The organization ObjectClass. |
| - UserObjec tClassCust omFilter | Strin g |   | No | (\|(cn=test) (mail=t***@test.com)) | The user-defined filter. |
| - GroupObj ectClass | Strin g |   | No | group | The group objectClass. |
| - GroupMe mberAttri buteName | Strin g |   | No | member | The group member identifier. |
| - GroupObj ectClassC ustomFilte r | Strin g |   | No | (\|(cn=test) (group=t***@test.com)) | The custom group filter. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PeriodicSy ncStatus | Strin g | Query | No | disabled | The status of scheduled verification. This parameter specifies whether to check data differences between Identity as a Service (IDaaS) and the IdP at regular intervals. Valid values: disabled enabled |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SetIdentityProviderUdPullConfiguration &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &IdentityProviderId=idp_my664lwkhpicbyzirog3xxxxx &IncrementalCallbackStatus=disabled &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### Query the pulling configurations of an IdP

Queries the pulling configurations of an identity provider (IdP).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

**q**

**p**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| IdentityPr oviderId | Strin g | Query | Yes | idp my664lwkhpicbyziro _ g3xxxxx | The IdP ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| UdPullConfigur ation | Struct | Struct | The pulling configurations. |
| -InstanceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The instance ID. |
| - IdentityProvid erId | String | idp my664lwkhpic _ byzirog3xxxxx | The IdP ID. |
| - IncrementalCa llbackStatus | String | enabled | The status of incremental callback. This parameter specifies whether to process incremental callback data from the IdP. Valid values: disabled enabled |
| - PeriodicSyncSt atus | String | enabled | The status of scheduled verification. This parameter specifies whether to check data differences between Identity as a Service (IDaaS) and the IdP at regular intervals. Valid values: disabled enabled |
| - GroupSyncStat us | String | enabled | The status of group synchronization. Valid values disabled enabled |
| - UdSyncScopeC onfig | Struct | Struct | The synchronization scope. |
| --TargetScope | String | ou 6zczfw67fqqpx _ wcoqa27nuhxxx | The target scope. |

| DaaS |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -- SourceScopes | String | OU=test,DC=idaas ,DC=com | The source scope. |
| - PullProtectedR ule | Struct | Struct | The protection rule for data pulling. |
| -- UserDeletedTh reshold | Integer | 30 | Specifies the number of days for which deleted user data is retained. When the specified time period ends, the related data is automatically cleared. |
| -- Organizational UnitDeletedTh reshold | Integer | 30 | Specifies the number of days for which deleted organization data is retained. When the specified time period ends, the related data is permanently cleared. |
| -- GroupDeleted Threshold | Integer | 30 | Specifies that groups that remain inactive for 30 days are considered candidates to be deleted. |
| - LdapUdPullCon fig | Struct | Struct | The pulling configurations on the LDAP side. |
| -- UserObjectCla ss | String | top,person,organiz ationalPerson,user | The user object class. |
| -- OrganizationU nitObjectClass | String | top,organizationalU nit | The organization object class. |
| -- UserObjectCla ssCustomFilter | String | test=123 | The filter conditions that are used to filter users. |
| -- GroupObjectCl ass | String | UserGroup | The group object class. |
| -- GroupMember AttributeName | String | member | The group member identifier. |
| -- GroupObjectCl assCustomFilt er | String | test=123 | The filter conditions that are used to filter groups. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

Sample requests

```
http(s)://[Endpoint]/?Action=GetIdentityProviderUdPullConfiguration &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &IdentityProviderId=idp_my664lwkhpicbyzirog3xxxxx &<Common request parameters>
```

Sample success responses

```json
 JSON format
 "UdPullConfiguration":{
  "LdapUdPullConfig":{
   "GroupObjectClass":"",
   "UserObjectClassCustomFilter":"",
   "GroupObjectClassCustomFilter":"",
   "OrganizationUnitObjectClass":"",
   "UserObjectClass":"",
   "GroupMemberAttributeName":""
```

`},`

```json
  "PeriodicSyncStatus":"enabled",
  "IdentityProviderId":"idp_my664lwkhpicbyzirog3xxxxx",
  "InstanceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
  "PullProtectedRule":{
   "UserDeletedThreshold":"",
   "OrganizationalUnitDeletedThreshold":"",
   "GroupDeletedThreshold":""
```

`},`

```json
  "UdSyncScopeConfig":{
   "SourceScopes":"",
   "TargetScope":""
```

`},`

```json
  "GroupSyncStatus":"enabled",
  "IncrementalCallbackStatus":"enabled"
```

`},`

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

#### Password policies

##### SetForgetPasswordConfiguration

Configures a forgot password policy for an Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM) instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | eiam-111ccc1111 | The instance ID. |
| ForgetPas swordStat us | Strin g | Query | Yes | enabled | The status of the forgot password feature. Valid values: enabled and disabled. |
| Authentic ationChan nels | Array | Query | No | email | The identity authentication channels. Valid values: email and sms. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SetForgetPasswordConfiguration &InstanceId=eiam-111ccc1111 &ForgetPasswordStatus=enabled &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### SetPasswordInitializationConfiguration

Configures a password initialization policy for an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| PasswordI nitializatio nStatus | Strin g | Query | Yes | enabled | Specifies whether to enable the password initialization feature. Valid values: enabled disabled |
| PasswordI nitializatio nType | Strin g | Query | No | random | The password initialization method. This parameter must be specified when PasswordInitializationSta tus is set to enabled. Set the value to random. |
| PasswordF orcedUpd ateStatus | Strin g | Query | No | enabled | Specifies whether to enable forcible password change upon first-time login. Valid values: enabled disabled |
| PasswordI nitializatio nNotificati onChanne ls | Array | Query | No | email | The methods for receiving password initialization notifications. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SetPasswordInitializationConfiguration &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &PasswordInitializationStatus=enabled &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### SetPasswordExpirationConfiguration

Configures a password expiration policy for an Enterprise Identity Access Management (EIAM) instance of Identity as a Service (IDaaS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Password Expiration Status | Strin g | Query | Yes | enabled | Specifies whether to enable the password expiration feature. Valid values: enabled disabled |
| Password ValidMaxD ay | Integ er | Query | No | 180 | The validity period of the password. Unit: day. This parameter must be specified when PasswordExpirationStatu s is set to enabled. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Password Expiration Action | Strin g | Query | No | force update password _ _ | The action to take upon password expiration. This parameter must be specified when PasswordExpirationStatu s is set to enabled. Valid values: forbid login: Users _ cannot log in to IDaaS. force update passwor _ _ d: Users must change the password. remind update passw _ _ ord: IDaaS reminds users to change the password upon each login. |
| Password Expiration Notificatio nStatus | Strin g | Query | No | enabled | Specifies whether to enable the password expiration notification feature. Valid values: enabled disabled |
| Password Expiration Notificatio nChannels | Array | Query | No | login | The methods for receiving password expiration notifications. This parameter must be specified when PasswordExpirationNotifi cationStatus is set to enabled. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Password Expiration Notificatio nDuration | Integ er | Query | No | 7 | The number of days before the expiration date during which password expiration notifications are sent. Unit: day. This parameter must be specified when PasswordExpirationNotifi cationStatus is set to enabled. |
| PasswordF orcedUpd ateDurati on | Integ er | Query | No | 7 | The number of days before which users must change the password to prevent password expiration. Unit: day. You must set this parameter to a value greater than the value of PasswordExpirationNotifi cationDuration. |
| EffectiveA uthenticat ionSourceI ds | Array | Query | No | test | The IDs of authentication sources that are effective. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=SetPasswordExpirationConfiguration &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &PasswordExpirationStatus=enabled &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### SetPasswordHistoryConfiguration

Configures a password history policy for an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Password HistorySta tus | Strin g | Query | Yes | enabled | Specifies whether to enable the password history feature. Valid values: enabled disabled |
| Password HistoryMa xRetentio n | Integ er | Query | No | 3 | The maximum number of recent passwords that can be retained. This parameter is required when PasswordHistoryStatus is set to enabled. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

Sample requests

```
http(s)://[Endpoint]/?Action=SetPasswordHistoryConfiguration &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &PasswordHistoryStatus=enabled &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### SetPasswordComplexityConfiguration

Configures a password complexity policy for an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Password MinLength | Integ er | Query | Yes | 10 | The minimum length of the password. |
| Password Complexit yRules | Array | Query | No | test | The password complexity rules. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

Sample requests

```
http(s)://[Endpoint]/?Action=SetPasswordComplexityConfiguration &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &PasswordMinLength=10 &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### Queries the forgot password policy of an

**EIAM instance**

Queries the forgot password policy of an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| OpenForgetPa sswordConfigu ration | Struct | Struct | The forgot password configurations. |
| -Enable | Boolean | true | Indicates whether Forgot Password is enabled. This parameter is deprecated. Use the forgetPasswordStatus parameter. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -EnableSms | Boolean | true | Indicates whether SMS is used as the authentication method for forgotten passwords. This parameter is deprecated. Use the authenticationChannels parameter. |
| -EnableEmail | Boolean | false | Indicates whether email is used as the authentication method for forgotten passwords. This parameter is deprecated. Use the authenticationChannels parameter. |
| - ForgetPasswor dStatus | String | enabled | The status of the forgot password feature. Valid values: enabled and disabled. |
| - Authentication Channels | String | SocialMedia | The authentication channel. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetForgetPasswordConfiguration &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "OpenForgetPasswordConfiguration":{
  "EnableEmail":false,
  "ForgetPasswordStatus":"enabled",
  "Enable":true,
  "AuthenticationChannels":"",
  "EnableSms":true
```

##### Queries the password initialization

**configurations of an EIAM) instance**

Queries the password initialization configurations of an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| PasswordInitial izationConfigu ration | Struct | Struct | The configurations for password initialization. |
| - PasswordInitial izationStatus | String | enabled | Indicates whether the password initialization feature is enabled. Valid values: enabled disabled |
| - PasswordInitial izationType | String | random | Indicates the password initialization method. Valid values: random |
| - PasswordForce dUpdateStatus | String | enabled | Indicates whether a forcible password change upon first login is enabled. Valid values: enabled disabled |
| - PasswordInitial izationNotifica tionChannels | String | email | The methods for receiving password initialization notifications. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetPasswordInitializationConfiguration &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "PasswordInitializationConfiguration":{
  "PasswordInitializationType":"random",
  "PasswordForcedUpdateStatus":"enabled",
  "PasswordInitializationNotificationChannels":"",
  "PasswordInitializationStatus":"enabled"
```

##### GetPasswordHistoryConfiguration

Queries the password history configurations of an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| PasswordHisto ryConfiguratio n | Struct | Struct | The password history detection configuration. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| - PasswordHisto ryStatus | String | enabled | Indicates the status of the password history feature. Valid values: enabled disabled |
| - PasswordHisto ryMaxRetentio n | Integer | 3 | The number of recent passwords that are retained. |

Sample requests

```
http(s)://[Endpoint]/?Action=GetPasswordHistoryConfiguration &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "PasswordHistoryConfiguration":{
  "PasswordHistoryStatus":"enabled",
  "PasswordHistoryMaxRetention":3
```

##### Queries the password expiration policy of

**an EIAM instance.**

Queries the password expiration policy of an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |

| DaaS |   |   |   | Dev | eloper Guide·API Referenc |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PasswordExpir ationConfigura tion | Struct | Struct | The password expiration configurations. |
| - PasswordExpir ationStatus | String | enabled | Indicates whether the password expiration feature is enabled. Valid values: enabled disabled |
| - PasswordValid MaxDay | Integer | 180 | The validity period of the password. Unit: days. |
| - PasswordExpir ationAction | String | forbid login _ | The action to take upon password expiration. Valid values: forbid login: Prohibit the user from _ using the password to log in to IDaaS. force update password: Users must _ _ change the password. remind update password: IDaaS _ _ reminds users to change the password upon each login. |
| - PasswordExpir ationNotificati onStatus | String | enabled | Specifies whether to enable the password expiration notification feature. Valid values: enabled disabled |
| - PasswordExpir ationNotificati onDuration | Integer | 7 | The number of days before the expiration date during which password expiration notifications are sent. Unit: days. |
| - PasswordForce dUpdateDurati on | Integer | 3 | The number of days before which users must change the password to prevent password expiration. Unit: days. |
| - PasswordExpir ationNotificati onChannels | String | login | The methods for receiving password expiration notifications. |

| Developer Guide·A | PI Reference |   | IDaa |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| - EffectiveAuthe nticationSourc eIds | String | effectiveSource123 | The unique identifiers of valid authentication sources are enabled in the system. The unique identifiers are used to specify the authentication sources that are activated and available for user authentication. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetPasswordExpirationConfiguration &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "PasswordExpirationConfiguration":{
  "PasswordExpirationStatus":"enabled",
  "EffectiveAuthenticationSourceIds":"",
  "PasswordExpirationNotificationChannels":"",
  "PasswordForcedUpdateDuration":3,
  "PasswordValidMaxDay":180,
  "PasswordExpirationNotificationDuration":7,
  "PasswordExpirationAction":"forbid_login",
  "PasswordExpirationNotificationStatus":"enabled"
```

`},`

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### Query the password complexity policy of

**an EIAM instance of IDaaS**

Queries the password complexity policy of an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| PasswordCom plexityConfigu ration | Struct | Struct | The password complexity configurations. |
| - PasswordMinL ength | Integer | 3 | The minimum length of the password. |
| - PasswordCom plexityRules | Array | Array | The password complexity rules. |
| -- PasswordChec kType | String | inclusion upper ca _ _ se | The password check item. Valid values: inclusion upper case: The password _ _ must contain uppercase letters. inclusion lower case: The password _ _ must contain lowercase letters. inclusion special case: The password _ _ must contain one or more of the following special characters: @ % + \ / ' ! # $ ^ ? : , ( ) { } [ ] ~ - . _ inclusion number: The password must _ contain digits. exclusion username: The password _ cannot contain the username. exclusion email: The password cannot _ contain the email address prefix. exclusion phone number: The password _ _ cannot contain the mobile number. exclusion display name: The password _ _ cannot contain the display name. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetPasswordComplexityConfiguration &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &<Common request parameters>
```

Sample success responses

```json
 JSON format
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "PasswordComplexityConfiguration":{
  "PasswordComplexityRules":[
    "PasswordCheckType":""
```

`],`

```json
  "PasswordMinLength":3
```

#### Synchronization

##### ListSynchronizationJobs

Queries a list of synchronization tasks.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| PageNum ber | Long | Query | No | 1 | The page number. Pages start from page 1. |
| PageSize | Long | Query | No | 10 | The number of pages. Maximum value: 100. |
| NextToke n | Strin g | Query | No | NTxxxxxexample | The pagination token that is used in the next request to retrieve a new page of results. If no next page is available, this parameter is not returned. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| MaxResult s | Long | Query | No | 20 | The number of entries per page. Maximum value: 100. |
| TargetTyp e | Strin g | Query | No | identity provider _ | The type of the synchronization destination. Valid values: identity provider: _ Identity provider. application: Application. |
| TargetIds | Array | Query | No | target 001 _ | The IDs of the synchronization destinations. [idp 111XXXX,idp 222X _ _ XXX] |
| StartTime | Long | Query | No | 1649830226000 | The start time of the synchronization task. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| EndTime | Long | Query | No | 1649830226000 | The end time of the synchronization task. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| Direction | Strin g | Query | No | ingress | The direction of the synchronization task. Valid values: ingress egress |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Status | Strin g | Query | No | running | The status of the synchronization task. Valid values: pending: The task is pending. running: The task is running. failed: The task failed. partial success: The _ task is partially successful. success: The task is successful. |
| Filters | Array | Query | No | test=123 | The filter parameters. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Long | 100 | The total number of entries returned. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| NextToken | String | NTxxxexample | A pagination token. It can be used in the next request to retrieve a new page of results. |
| Synchronizatio nJobs | Array | Array | Synchronization tasks. |
| - Synchronizatio nJobId | String | sync 0000347vjovt _ cf41li0fgsd98gn24 q9njxxxxx | The ID of the synchronization task. |
| -TargetType | String | identity provider _ | The type of the synchronization destination. Valid values: identity provider: Identity provider. _ application: Application. |
| -TargetId | String | idp my664lwkhpic _ byzirog3xxxxx | The ID of the synchronization destination. |

| DaaS |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Direction | String | ingress | The direction of the synchronization task. Valid values: ingress: Inbound. egress: Outbound. |
| -StartTime | Long | 1649830226000 | The start time of the synchronization task. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| -EndTime | Long | 1649830226000 | The end time of the synchronization task. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |
| -TriggerType | String | auto | The trigger type of the synchronization task. Valid values: auto: Automatic. manual: Manual. |
| -Status | String | success | The status of the synchronization task. Valid values: pending: The task is pending. running: The task is running. failed: The task failed. partial success: The task is partially _ successful. success: The task is successful. |
| -Description | String | Description | The description of the synchronization task. |
| -Result | Struct | Struct | The result of the synchronization task. |
| -- ErrorMessage | String | The request parameters are invalid. | The error message returned in the case of an error. |
| --ErrorCode | String | ErrorCodeNotFoun d | The error code corresponding to the error message. |
| -- UserStatistics | Struct | object | The user synchronization result statistics. |

|   | Developer Guide·A | PI Reference |   | IDaa | S |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ---Created | Struct | object | The creation result statistics. |
| ----Total | Long | 3 | The total number of items. |
| ----Success | Long | 1 | The number of successful items. |
| ----Failed | Long | 1 | The number of failed items. |
| ----Skipped | Long | 1 | The number of skipped items. |
| ---Updated | Struct | object | The update result statistics. |
| ----Total | Long | 3 | The total number of items. |
| ----Success | Long | 1 | The number of successful items. |
| ----Failed | Long | 1 | The number of failed items. |
| ----Skipped | Long | 1 | The number of skipped items. |
| ---Binded | Struct | object | The binding result statistics. |
| ----Total | Long | 3 | The total number of items. |
| ----Success | Long | 1 | The number of successful items. |
| ----Failed | Long | 1 | The number of failed items. |
| ----Skipped | Long | 1 | The number of skipped items. |
| ---Deleted | Struct | object | The deletion result statistics. |
| ----Total | Long | 3 | The total number of items. |
| ----Success | Long | 1 | The number of successful items. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ----Failed | Long | 1 | The number of failed items. |
| ----Skipped | Long | 1 | The number of skipped items. |
| ---Same | Struct | object | The identical result statistics. |
| ----Total | Long | 3 | The total number of items. |
| ----Success | Long | 1 | The number of successful items. |
| ----Failed | Long | 1 | The number of failed items. |
| ----Skipped | Long | 1 | The number of skipped items. |
| ---Pushed | Struct | object | The notification result statistics. |
| ----Total | Long | 3 | The total number of items. |
| ----Success | Long | 1 | The number of successful items. |
| ----Failed | Long | 1 | The number of failed items. |
| ----Skipped | Long | 1 | The number of skipped items. |
| ---Exported | Struct | object | The exported result statistics. |
| ----Total | Long | 5 | The total number of items. |
| ----Success | Long | 2 | The number of successful items. |
| ----Failed | Long | 3 | The number of failed items. |
| ----Skipped | Long | 1 | The number of skipped items. |
| -- Organizational UnitStatistics | Struct | object | The organization synchronization result statistics. |

| Developer Guide·A | PI Reference |   | IDaa |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ---Created | Struct | object | The creation result statistics. |
| ----Total | Long | 3 | The total number of items. |
| ----Success | Long | 1 | The number of successful items. |
| ----Failed | Long | 1 | The number of failed items. |
| ----Skipped | Long | 1 | The number of skipped items. |
| ---Updated | Struct | object | The update result statistics. |
| ----Total | Long | 3 | The total number of items. |
| ----Success | Long | 1 | The number of successful items. |
| ----Failed | Long | 1 | The number of failed items. |
| ----Skipped | Long | 1 | The number of skipped items. |
| ---Binded | Struct | object | The binding result statistics. |
| ----Total | Long | 3 | The total number of items. |
| ----Success | Long | 1 | The number of successful items. |
| ----Failed | Long | 1 | The number of failed items. |
| ----Skipped | Long | 1 | The number of skipped items. |
| ---Deleted | Struct | object | The deletion result statistics. |
| ----Total | Long | 3 | The total number of items. |
| ----Success | Long | 1 | The number of successful items. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ----Failed | Long | 1 | The number of failed items. |
| ----Skipped | Long | 1 | The number of skipped items. |
| ---Same | Struct | object | The identical result statistics. |
| ----Total | Long | 3 | The total number of items. |
| ----Success | Long | 1 | The number of successful items. |
| ----Failed | Long | 1 | The number of failed items. |
| ----Skipped | Long | 1 | The number of skipped items. |
| ---Pushed | Struct | object | The notification result statistics. |
| ----Total | Long | 3 | The total number of items. |
| ----Success | Long | 1 | The number of successful items. |
| ----Failed | Long | 1 | The number of failed items. |
| ----Skipped | Long | 1 | The number of skipped items. |
| -- GroupStatistic s | Struct | object | The group synchronization result statistics. |
| ---Created | Struct | object | The creation result statistics. |
| ----Total | Long | 3 | The total number of items. |
| ----Success | Long | 1 | The number of successful items. |
| ----Failed | Long | 1 | The number of failed items. |
| ----Skipped | Long | 1 | The number of skipped items. |

| Developer Guide·A | PI Reference |   | IDaa |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ---Updated | Struct | object | The update result statistics. |
| ----Total | Long | 3 | The total number of items. |
| ----Success | Long | 1 | The number of successful items. |
| ----Failed | Long | 1 | The number of failed items. |
| ----Skipped | Long | 1 | The number of skipped items. |
| ---Binded | Struct | object | The binding result statistics. |
| ----Total | Long | 3 | The total number of items. |
| ----Success | Long | 1 | The number of successful items. |
| ----Failed | Long | 1 | The number of failed items. |
| ----Skipped | Long | 1 | The number of skipped items. |
| ---Deleted | Struct | object | The deletion result statistics. |
| ----Total | Long | 3 | The total number of items. |
| ----Success | Long | 1 | The number of successful items. |
| ----Failed | Long | 1 | The number of failed items. |
| ----Skipped | Long | 1 | The number of skipped items. |
| ---Same | Struct | object | The identical result statistics. |
| ----Total | Long | 3 | The total number of entries returned. |
| ----Success | Long | 1 | The number of successful items. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ----Failed | Long | 1 | The number of failed items. |
| ----Skipped | Long | 1 | The number of skipped items. |
| ---Pushed | Struct | object | The notification result statistics. |
| ----Total | Long | 3 | The total number of items. |
| ----Success | Long | 1 | The number of successful items. |
| ----Failed | Long | 1 | The number of failed items. |
| ----Skipped | Long | 1 | The number of skipped items. |
| -- GroupMember Statistics | Struct | object | The group member synchronization result statistics. |
| ---Created | Struct | object | The creation result statistics. |
| ----Total | Long | 3 | The total number of items. |
| ----Success | Long | 1 | The number of successful items. |
| ----Failed | Long | 1 | The number of failed items. |
| ----Skipped | Long | 1 | The number of skipped items. |
| ---Updated | Struct | object | The update result statistics. |
| ----Total | Long | 3 | The total number of items. |
| ----Success | Long | 1 | The number of successful items. |
| ----Failed | Long | 1 | The number of failed items. |
| ----Skipped | Long | 1 | The number of skipped items. |

| Developer Guide·A | PI Reference |   | IDaa |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ---Binded | Struct | object | The binding result statistics. |
| ----Total | Long | 3 | The total number of items. |
| ----Success | Long | 1 | The number of successful items. |
| ----Failed | Long | 1 | The number of failed items. |
| ----Skipped | Long | 1 | The number of skipped items. |
| ---Deleted | Struct | object | The deletion result statistics. |
| ----Total | Long | 3 | The total number of items. |
| ----Success | Long | 1 | The number of successful items. |
| ----Failed | Long | 1 | The number of failed items. |
| ----Skipped | Long | 1 | The number of skipped items. |
| ---Same | Struct | object | The identical result statistics. |
| ----Total | Long | 3 | The total number of items. |
| ----Success | Long | 1 | The number of successful items. |
| ----Failed | Long | 1 | The number of failed items. |
| ----Skipped | Long | 1 | The number of skipped items. |
| ---Pushed | Struct | object | The notification result statistics. |
| ----Total | Long | 3 | The total number of items. |
| ----Success | Long | 1 | The number of successful items. |
| ----Failed | Long | 1 | The number of failed items. |

| DaaS |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ----Skipped | Long | 1 | The number of skipped items. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListSynchronizationJobs &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "TotalCount":100,
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "NextToken":"NTxxxexample",
 "SynchronizationJobs":[
   "Status":"success",
   "TriggerType":"auto",
   "Result":[
     "GroupMemberStatistics":[
       "Same":[
         "Failed":1,
         "Total":3,
         "Skipped":1,
         "Success":1
```

`],`

```json
       "Deleted":[
         "Failed":1,
         "Total":3,
         "Skipped":1,
         "Success":1
```

`],`

```json
       "Binded":[
         "Failed":1,
         "Total":3,
         "Skipped":1,
         "Success":1
```

`],`

```json
       "Created":[
```

```json
         "Failed":1,
         "Total":3,
         "Skipped":1,
         "Success":1
```

`],`

```json
       "Pushed":[
         "Failed":1,
         "Total":3,
         "Skipped":1,
         "Success":1
```

`],`

```json
       "Updated":[
         "Failed":1,
         "Total":3,
         "Skipped":1,
         "Success":1
```

`]` `],`

```json
     "GroupStatistics":[
       "Same":[
         "Failed":1,
         "Total":3,
         "Skipped":1,
         "Success":1
```

`],`

```json
       "Deleted":[
         "Failed":1,
         "Total":3,
         "Skipped":1,
         "Success":1
```

`],`

```json
       "Binded":[
         "Failed":1,
         "Total":3,
         "Skipped":1,
         "Success":1
```

`],`

```json
       "Created":[
         "Failed":1,
"Total":3,
```

```json
         Total:3,
         "Skipped":1,
         "Success":1
```

`],`

```json
       "Pushed":[
         "Failed":1,
         "Total":3,
         "Skipped":1,
         "Success":1
```

`],`

```json
       "Updated":[
         "Failed":1,
         "Total":3,
         "Skipped":1,
         "Success":1
```

`]` `],`

```json
     "ErrorCode":"ErrorCodeNotFound",
     "ErrorMessage":"Request parameter error",
     "OrganizationalUnitStatistics":[
       "Same":[
         "Failed":1,
         "Total":3,
         "Skipped":1,
         "Success":1
```

`],`

```json
       "Deleted":[
         "Failed":1,
         "Total":3,
         "Skipped":1,
         "Success":1
```

`],`

```json
       "Binded":[
         "Failed":1,
         "Total":3,
         "Skipped":1,
         "Success":1
```

`],`

```json
       "Created":[
         "Failed":1,
         "Total":3,
```

`,`

```json
         "Skipped":1,
         "Success":1
```

`],`

```json
       "Pushed":[
         "Failed":1,
         "Total":3,
         "Skipped":1,
         "Success":1
```

`],`

```json
       "Updated":[
         "Failed":1,
         "Total":3,
         "Skipped":1,
         "Success":1
```

`]` `],`

```json
     "UserStatistics":[
       "Same":[
         "Failed":1,
         "Total":3,
         "Skipped":1,
         "Success":1
```

`],`

```json
       "Exported":[
         "Failed":3,
         "Total":5,
         "Skipped":1,
         "Success":2
```

`],`

```json
       "Deleted":[
         "Failed":1,
         "Total":3,
         "Skipped":1,
         "Success":1
```

`],`

```json
       "Binded":[
         "Failed":1,
         "Total":3,
         "Skipped":1,
         "Success":1
```

`],`

```json
       "Created":[
         "Failed":1,
         "Total":3,
         "Skipped":1,
         "Success":1
```

`],`

```json
       "Pushed":[
         "Failed":1,
         "Total":3,
         "Skipped":1,
         "Success":1
```

`],`

```json
       "Updated":[
         "Failed":1,
         "Total":3,
         "Skipped":1,
         "Success":1
```

`]` `]` `],`

```json
   "SynchronizationJobId":"sync_0000347vjovtcf41li0fgsd98gn24q9njxxxxx",
   "Description":"Description",
   "EndTime":1649830226000,
   "TargetType":"identity_provider",
   "StartTime":1649830226000,
   "Direction":"ingress",
   "TargetId":"idp_my664lwkhpicbyzirog3xxxxx"
```

`]`

##### Runs a synchronization task

Runs a synchronization task. A new synchronization task will be created and immediately executed.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| TargetId | Strin g | Query | Yes | idp my664lwkhpicbyziro _ g3ngxxxxx | The ID of the synchronization destination. |
| TargetTyp e | Strin g | Query | Yes | identity provider _ | The type of the synchronization destination. Valid values: identity provider _ application |
| Descriptio n | Strin g | Query | No | Description | The description of the synchronization task. |
| UserIdenti tyTypes | Array | Query | No | 5 | The unique identifiers of users. |
| Synchroni zationSco peConfig | Struc t | Query | No | Struct | The synchronization scope. |
| - Organizati onalUnitId s | Array |   | No | [ou wovwffm62xifdziem _ 7an7xxxxx] | The organization IDs. |
| -GroupIds | Array |   | No | [group miu8e4t4d7i4u7 _ uwezgr54xxxx] | The group IDs. |
| -UserIds | Array |   | No | [user d6sbsuumeta4h66 _ ec3il7yxxxx] | The account IDs. |
| PasswordI nitializatio n | Boole an | Query | No | true | Specifies whether to initialize the password. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Synchronizatio nJobId | String | sync 0000347vjovt _ cf41li0fgsd98gn24 q9nj9xxxxx | The ID of the synchronization task. |

| DaaS |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=RunSynchronizationJob &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &TargetId=idp_my664lwkhpicbyzirog3ngxxxxx &TargetType=identity_provider &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "SynchronizationJobId":"sync_0000347vjovtcf41li0fgsd98gn24q9nj9xxxxx",
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### GetSynchronizationJob

Obtains the information about a single synchronization job.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| Synchroni zationJobI d | Strin g | Query | Yes | sync 0000347vjovtcf41li _ 0fgsd98gn24q9njxxxxx | The synchronization job ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| Synchronizatio nJob | Struct | Struct | The information about the synchronization job. |
| - Synchronizatio nJobId | String | sync 0000347vjovt _ cf41li0fgsd98gn24 q9nj9xxxxx | The synchronization job ID. |
| -TargetType | String | identity provider _ | The type of the synchronization destination. Valid values: identity provider _ application |
| -TargetId | String | idp my664lwkhpic _ byzirog3nxxxxx | The synchronization destination ID. |
| -Direction | String | ingress | The direction of the synchronization job. Valid values: ingress egress |
| -StartTime | Long | 1649830226000 | The start time of the synchronization job. This value is a UNIX timestamp. Unit: milliseconds. |
| -EndTime | Long | 1649830226000 | The end time of the synchronization job. This value is a UNIX timestamp. Unit: milliseconds. |
| -TriggerType | String | auto | The trigger type of the synchronization job. Valid values: auto manual |
| -Status | String | running | The status of the synchronization job. Valid values: pending running failed partial success _ success |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Result | Struct | Struct | The result of the synchronization job. |
| -- ErrorMessage | String | An internal error occurred. | The error message returned in the case of an error. |
| --ErrorCode | String | ErrorCodeNotFoun d | The error code corresponding to the error message. |
| -- UserStatistics | Struct | object | The user synchronization result statistics. |
| ---Created | Struct | object | The creation result statistics. |
| ----Total | Long | 30 | The total number of items. |
| ----Success | Long | 10 | The number of successful items. |
| ----Failed | Long | 10 | The number of failed items. |
| ----Skipped | Long | 10 | The number of skipped items. |
| ---Updated | Struct | object | The update result statistics. |
| ----Total | Long | 30 | The total number of items. |
| ----Success | Long | 10 | The number of successful items. |
| ----Failed | Long | 10 | The number of failed items. |
| ----Skipped | Long | 10 | The number of skipped items. |
| ---Binded | Struct | object | The binding result statistics. |
| ----Total | Long | 30 | The total number of items. |
| ----Success | Long | 10 | The number of successful items. |
| ----Failed | Long | 10 | The number of failed items. |

| Developer Guide·A | PI Reference |   | IDaa |
|---|---|---|---|
| Parameter | Type | Example | Description |
| ----Skipped | Long | 10 | The number of skipped items. |
| ---Deleted | Struct | object | The deletion result statistics. |
| ----Total | Long | 30 | The total number of items. |
| ----Success | Long | 10 | The number of successful items. |
| ----Failed | Long | 10 | The number of failed items. |
| ----Skipped | Long | 10 | The number of skipped items. |
| ---Same | Struct | object | The result statistics about identical group members. |
| ----Total | Long | 30 | The total number of items. |
| ----Success | Long | 10 | The number of successful items. |
| ----Failed | Long | 10 | The number of failed items. |
| ----Skipped | Long | 10 | The number of skipped items. |
| ---Pushed | Struct | object | The notification result statistics. |
| ----Total | Long | 30 | The total number of items. |
| ----Success | Long | 10 | The number of successful items. |
| ----Failed | Long | 10 | The number of failed items. |
| ----Skipped | Long | 10 | The number of skipped items. |
| -- Organizational UnitStatistics | Struct | object | The organization synchronization result statistics. |
| ---Created | Struct | object | The creation result statistics. |

| I | DaaS |   |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ----Total | Long | 30 | The total number of items. |
| ----Success | Long | 10 | The number of successful items. |
| ----Failed | Long | 10 | The number of failed items. |
| ----Skipped | Long | 10 | The number of skipped items. |
| ---Updated | Struct | object | The update result statistics. |
| ----Total | Long | 30 | The total number of items. |
| ----Success | Long | 10 | The number of successful items. |
| ----Failed | Long | 10 | The number of failed items. |
| ----Skipped | Long | 10 | The number of skipped items. |
| ---Binded | Struct | object | The binding result statistics. |
| ----Total | Long | 30 | The total number of items. |
| ----Success | Long | 10 | The number of successful items. |
| ----Failed | Long | 10 | The number of failed items. |
| ----Skipped | Long | 10 | The number of skipped items. |
| ---Deleted | Struct | object | The deletion result statistics. |
| ----Total | Long | 30 | The total number of items. |
| ----Success | Long | 10 | The number of successful items. |
| ----Failed | Long | 10 | The number of failed items. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ----Skipped | Long | 10 | The number of skipped items. |
| ---Same | Struct | object | The result statistics about identical groups. |
| ----Total | Long | 30 | The total number of items. |
| ----Success | Long | 10 | The number of successful items. |
| ----Failed | Long | 10 | The number of failed items. |
| ----Skipped | Long | 10 | The number of skipped items. |
| ---Pushed | Struct | object | The notification result statistics. |
| ----Total | Long | 30 | The total number of items. |
| ----Success | Long | 10 | The number of successful items. |
| ----Failed | Long | 10 | The number of failed items. |
| ----Skipped | Long | 10 | The number of skipped items. |
| -- GroupStatistic s | Struct | object | The group synchronization result statistics. |
| ---Created | Struct | object | The creation result statistics. |
| ----Total | Long | 30 | The total number of items. |
| ----Success | Long | 10 | The number of successful items. |
| ----Failed | Long | 10 | The number of failed items. |
| ----Skipped | Long | 10 | The number of skipped items. |
| ---Updated | Struct | object | The update result statistics. |

| DaaS |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ----Total | Long | 30 | The total number of items. |
| ----Success | Long | 10 | The number of successful items. |
| ----Failed | Long | 10 | The number of failed items. |
| ----Skipped | Long | 10 | The number of skipped items. |
| ---Binded | Struct | object | The binding result statistics. |
| ----Total | Long | 30 | The total number of items. |
| ----Success | Long | 10 | The number of successful items. |
| ----Failed | Long | 10 | The number of failed items. |
| ----Skipped | Long | 10 | The number of skipped items. |
| ---Deleted | Struct | object | The deletion result statistics. |
| ----Total | Long | 30 | The total number of items. |
| ----Success | Long | 10 | The number of successful items. |
| ----Failed | Long | 10 | The number of failed items. |
| ----Skipped | Long | 10 | The number of skipped items. |
| ---Same | Struct | object | The result statistics about identical organizations. |
| ----Total | Long | 30 | The total number of items. |
| ----Success | Long | 10 | The number of successful items. |
| ----Failed | Long | 10 | The number of failed items. |

| Developer Guide·A | PI Reference |   | IDaa |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ----Skipped | Long | 10 | The number of skipped items. |
| ---Pushed | Struct | object | The notification result statistics. |
| ----Total | Long | 30 | The total number of items. |
| ----Success | Long | 10 | The number of successful items. |
| ----Failed | Long | 10 | The number of failed items. |
| ----Skipped | Long | 10 | The number of skipped items. |
| -- GroupMember Statistics | Struct | object | The group member synchronization result statistics. |
| ---Created | Struct | object | The creation result statistics. |
| ----Total | Long | 30 | The total number of items. |
| ----Success | Long | 10 | The number of successful items. |
| ----Failed | Long | 10 | The number of failed items. |
| ----Skipped | Long | 10 | The number of skipped items. |
| ---Updated | Struct | object | The update result statistics. |
| ----Total | Long | 30 | The total number of items. |
| ----Success | Long | 10 | The number of successful items. |
| ----Failed | Long | 10 | The number of failed items. |
| ----Skipped | Long | 10 | The number of skipped items. |
| ---Binded | Struct | object | The binding result statistics. |

| DaaS |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| ----Total | Long | 30 | The total number of items. |
| ----Success | Long | 10 | The number of successful items. |
| ----Failed | Long | 10 | The number of failed items. |
| ----Skipped | Long | 10 | The number of skipped items. |
| ---Deleted | Struct | object | The deletion result statistics. |
| ----Total | Long | 30 | The total number of items. |
| ----Success | Long | 10 | The number of successful items. |
| ----Failed | Long | 10 | The number of failed items. |
| ----Skipped | Long | 10 | The number of skipped items. |
| ---Same | Struct | object | The result statistics about identical users. |
| ----Total | Long | 30 | The total number of items. |
| ----Success | Long | 10 | The number of successful items. |
| ----Failed | Long | 10 | The number of failed items. |
| ----Skipped | Long | 10 | The number of skipped items. |
| ---Pushed | Struct | object | The notification result statistics. |
| ----Total | Long | 30 | The total number of items. |
| ----Success | Long | 10 | The number of successful items. |
| ----Failed | Long | 10 | The number of failed items. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ----Skipped | Long | 10 | The number of skipped items. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetSynchronizationJob &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &SynchronizationJobId=sync_0000347vjovtcf41li0fgsd98gn24q9njxxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "SynchronizationJob":{
  "Status":"running",
  "TriggerType":"auto",
  "Result":{
   "GroupMemberStatistics":{
    "Same":{
     "Failed":10,
     "Total":30,
     "Skipped":10,
     "Success":10
```

`},`

```json
    "Deleted":{
     "Failed":10,
     "Total":30,
     "Skipped":10,
     "Success":10
```

`},`

```json
    "Binded":{
     "Failed":10,
     "Total":30,
     "Skipped":10,
     "Success":10
```

`},`

```json
    "Created":{
     "Failed":10,
     "Total":30,
     "Skipped":10,
     "Success":10
```

`},`

```json
    "Pushed":{
     "Failed":10,
     "Total":30,
     "Skipped":10,
"Success":10
```

```json
     "Success":10
```

`},`

```json
    "Updated":{
     "Failed":10,
     "Total":30,
     "Skipped":10,
     "Success":10
```

`},`

```json
   "GroupStatistics":{
    "Same":{
     "Failed":10,
     "Total":30,
     "Skipped":10,
     "Success":10
```

`},`

```json
    "Deleted":{
     "Failed":10,
     "Total":30,
     "Skipped":10,
     "Success":10
```

`},`

```json
    "Binded":{
     "Failed":10,
     "Total":30,
     "Skipped":10,
     "Success":10
```

`},`

```json
    "Created":{
     "Failed":10,
     "Total":30,
     "Skipped":10,
     "Success":10
```

`},`

```json
    "Pushed":{
     "Failed":10,
     "Total":30,
     "Skipped":10,
     "Success":10
```

`},`

```json
    "Updated":{
     "Failed":10,
     "Total":30,
     "Skipped":10,
     "Success":10
```

`},`

```json
   "ErrorCode":"ErrorCodeNotFound",
   "ErrorMessage":"internal error",
   "OrganizationalUnitStatistics":{
    "Same":{
     "Failed":10,
     "Total":30,
     "Skipped":10,
"Success":10
```

```
     Success:10
```

`},`

```json
    "Deleted":{
     "Failed":10,
     "Total":30,
     "Skipped":10,
     "Success":10
```

`},`

```json
    "Binded":{
     "Failed":10,
     "Total":30,
     "Skipped":10,
     "Success":10
```

`},`

```json
    "Created":{
     "Failed":10,
     "Total":30,
     "Skipped":10,
     "Success":10
```

`},`

```json
    "Pushed":{
     "Failed":10,
     "Total":30,
     "Skipped":10,
     "Success":10
```

`},`

```json
    "Updated":{
     "Failed":10,
     "Total":30,
     "Skipped":10,
     "Success":10
```

`},`

```json
   "UserStatistics":{
    "Same":{
     "Failed":10,
     "Total":30,
     "Skipped":10,
     "Success":10
```

`},`

```json
    "Deleted":{
     "Failed":10,
     "Total":30,
     "Skipped":10,
     "Success":10
```

`},`

```json
    "Binded":{
     "Failed":10,
     "Total":30,
     "Skipped":10,
     "Success":10
```

`},`

```json
    "Created":{
     "Failed":10,
     "Total":30,
```

```json
     "Skipped":10,
     "Success":10
```

`},`

```json
    "Pushed":{
     "Failed":10,
     "Total":30,
     "Skipped":10,
     "Success":10
```

`},`

```json
    "Updated":{
     "Failed":10,
     "Total":30,
     "Skipped":10,
     "Success":10
```

`},`

```json
  "SynchronizationJobId":"sync_0000347vjovtcf41li0fgsd98gn24q9nj9xxxxx",
  "EndTime":1649830226000,
  "TargetType":"identity_provider",
  "StartTime":1649830226000,
  "Direction":"ingress",
  "TargetId":"idp_my664lwkhpicbyzirog3nxxxxx"
```

`XML` format

```xml
<RequestId>0441BD79-92F3-53AA-8657-F8CE4A2B912A</RequestId> <SynchronizationJob>
 <Status>running</Status>
 <TriggerType>auto</TriggerType>
 <Result>
  <GroupMemberStatistics>
   <Same>
    <Failed  />
    <Total  />
    <Skipped  />
    <Success  />
   </Same>
   <Deleted>
    <Failed  />
    <Total  />
    <Skipped  />
    <Success  />
   </Deleted>
   <Binded>
    <Failed  />
    <Total  />
    <Skipped  />
    <Success  />
   </Binded>
   <Created>
<Failed
```

`/>`

```xml
    <Failed  />
    <Total  />
    <Skipped  />
    <Success  />
   </Created>
   <Pushed>
    <Failed  />
    <Total  />
    <Skipped  />
    <Success  />
   </Pushed>
   <Updated>
    <Failed  />
    <Total  />
    <Skipped  />
    <Success  />
   </Updated>
  </GroupMemberStatistics>
  <GroupStatistics>
   <Same>
    <Failed  />
    <Total  />
    <Skipped  />
    <Success  />
   </Same>
   <Deleted>
    <Failed  />
    <Total  />
    <Skipped  />
    <Success  />
   </Deleted>
   <Binded>
    <Failed  />
    <Total  />
    <Skipped  />
    <Success  />
   </Binded>
   <Created>
    <Failed  />
    <Total  />
    <Skipped  />
    <Success  />
   </Created>
   <Pushed>
    <Failed  />
    <Total  />
    <Skipped  />
    <Success  />
   </Pushed>
   <Updated>
    <Failed  />
    <Total  />
    <Skipped  />
    <Success  />
   </Updated>
```

`/``p`

```xml
  </GroupStatistics>
  <ErrorCode  />
  <ErrorMessage  />
  <OrganizationalUnitStatistics>
   <Same>
    <Failed  />
    <Total  />
    <Skipped  />
    <Success  />
   </Same>
   <Deleted>
    <Failed  />
    <Total  />
    <Skipped  />
    <Success  />
   </Deleted>
   <Binded>
    <Failed  />
    <Total  />
    <Skipped  />
    <Success  />
   </Binded>
   <Created>
    <Failed  />
    <Total  />
    <Skipped  />
    <Success  />
   </Created>
   <Pushed>
    <Failed  />
    <Total  />
    <Skipped  />
    <Success  />
   </Pushed>
   <Updated>
    <Failed  />
    <Total  />
    <Skipped  />
    <Success  />
   </Updated>
  </OrganizationalUnitStatistics>
  <UserStatistics>
   <Same>
    <Failed  />
    <Total  />
    <Skipped  />
    <Success  />
   </Same>
   <Deleted>
    <Failed  />
    <Total  />
    <Skipped  />
    <Success  />
   </Deleted>
```

```xml
   <Binded>
    <Failed  />
    <Total  />
    <Skipped  />
    <Success  />
   </Binded>
   <Created>
    <Failed  />
    <Total  />
    <Skipped  />
    <Success  />
   </Created>
   <Pushed>
    <Failed  />
    <Total  />
    <Skipped  />
    <Success  />
   </Pushed>
   <Updated>
    <Failed  />
    <Total  />
    <Skipped  />
    <Success  />
   </Updated>
  </UserStatistics>
 </Result>
 <SynchronizationJobId>sync_0000347vjovtcf41li0fgsd98gn24q9nj9xxxxx
 </SynchronizationJobId>
 <EndTime>1649830226000</EndTime>
 <TargetType>identity_provider</TargetType>
 <StartTime>1649830226000</StartTime>
 <Direction>ingress</Direction>
 <TargetId>idp_my664lwkhpicbyzirog3nxxxxx
 </TargetId>
</SynchronizationJob>
```

#### Endpoints

##### CreateNetworkAccessEndpoint

Creates a dedicated endpoint.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| NetworkA ccessEndp ointName | Strin g | Query | Yes | VPCEndpointForXX | The name of the dedicated endpoint. |
| VpcId | Strin g | Query | Yes | vpc-examplexxx | The ID of the virtual private cloud (VPC) to which the dedicated endpoint is connected. |
| VpcRegio nId | Strin g | Query | Yes | cn-hangzhou | The region ID of the VPC to which the dedicated endpoint is connected. |
| VSwitchId s | Array | Query | No | vsw-examplexxx | The vSwitches that are connected to the dedicated endpoint. |
| ClientToke n | Strin g | Query | No | client-token-example | The client token to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see How to ensure idempotence. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| NetworkAcces sEndpointId | String | nae examplexxxx _ | The ID of the dedicated endpoint. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateNetworkAccessEndpoint &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &NetworkAccessEndpointName=VPCEndpointForXX &VpcId=vpc-examplexxx &VpcRegionId=cn-hangzhou &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "NetworkAccessEndpointId":"nae_examplexxxx"
```

##### DeleteNetworkAccessEndpoint

Deletes a dedicated endpoint.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| NetworkA ccessEndp ointId | Strin g | Query | Yes | nae examplexxxx _ | The ID of the dedicated endpoint. You can delete only network endpoints whose NetworkEndpointType is private. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteNetworkAccessEndpoint &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &NetworkAccessEndpointId=nae_examplexxxx &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### UpdateNetworkAccessEndpointName

Changes the name of a dedicate network endpoint.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| NetworkA ccessEndp ointId | Strin g | Query | Yes | nae examplexxxx _ | The ID of the dedicated network endpoint. |
| NetworkA ccessEndp ointName | Strin g | Query | Yes | VPCEndpointForXX | The name of the dedicated network endpoint. You can change the names of only network endpoints whose NetworkEndpointType is private. VPCEndpointForXX |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateNetworkAccessEndpointName &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &NetworkAccessEndpointId=nae_examplexxxx &NetworkAccessEndpointName=VPCEndpointForXX &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### Query the regions that support network

**endpoints of IDaaS**

Queries the regions that support network endpoints of Identity as a Service (IDaaS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| Regions | Array | Array | The list of regions that are available. |

| I | DaaS |   |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -RegionId | String | cn-hangzhou | The region ID. |
| -LocalName | String | China (Hangzhou) | The region name. |

Sample requests

```
http(s)://[Endpoint]/?Action=ListNetworkAccessEndpointAvailableRegions &<Common request parameters>
```

Sample success responses

```json
 JSON format
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "Regions":[
   "RegionId":"cn-hangzhou",
   "LocalName":"China (Hangzhou)"
```

`]`

##### ListNetworkAccessEndpointAvailableZones

Queries the zones that support dedicated endpoints in the specified region of Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| NaeRegio nId | Strin g | Query | Yes | cn-hangzhou | The ID of the region that supports dedicated endpoints. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| Zones | Array | Array | The zones that support dedicated endpoints in the specified region. |
| -ZoneId | String | cn-hangzhou-j | The zone ID. |
| -LocalName | String | Hangzhou Zone J | The zone name. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListNetworkAccessEndpointAvailableZones &NaeRegionId=cn-hangzhou &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "Zones":[
   "ZoneId":"cn-hangzhou-j",
   "LocalName":"Hangzhou Zone J"
```

`]`

##### GetNetworkAccessEndpoint

Queries the information about a network endpoint.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| NetworkA ccessEndp ointId | Strin g | Query | Yes | nae-examplexxxx | The ID of the network endpoint. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| NetworkAcces sEndpoint | Struct | Struct | The information about the network endpoint. |
| -InstanceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The instance ID. |
| - NetworkAcces sEndpointId | String | nae examplexxx _ | The ID of the network endpoint. |
| - NetworkAcces sEndpointNam e | String | VPCEndpointForXX | The name of the network endpoint. |
| -VpcId | String | vpc-examplexxx | The ID of the virtual private cloud (VPC) to which the network endpoint is connected. |
| -VpcRegionId | String | cn-hangzhou | The region ID of the VPC to which the network endpoint is connected. |
| - SecurityGroupI d | String | sg-examplexxx | The ID of the security group used by the network endpoint. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Status | String | running | The status of the network endpoint. Valid values: Pending: The network endpoint is pending for initialization. creating: The network endpoint is being created. running: The network endpoint is running. deleting: The network endpoint is being deleted. |
| - NetworkAcces sEndpointType | String | private | The type of the network endpoint. Valid values: shared: shared network endpoint. private: dedicated network endpoint. |
| -CreateTime | Long | 1649830226000 | The time when the network endpoint was created. The value is a UNIX timestamp. Unit: milliseconds. |
| -UpdateTime | Long | 1649830226000 | The time when the network endpoint was updated. The value is a UNIX timestamp. Unit: milliseconds. |
| -VSwitchIds | String | vsw-examplexxx | The vSwitches that are connected to the network endpoint. |
| - EgressPublicIp Addresses | String | 8.xx.xx.xxx/27 | The outbound public CIDR block of the shared network endpoint. This value is returned only when NetworkEndpointType is set to shared. |
| - EgressPrivateI pAddresses | String | 172.168.x.x | The outbound public CIDR block of the dedicated network endpoint. This value is returned only when NetworkEndpointType is set to private. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=GetNetworkAccessEndpoint &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &NetworkAccessEndpointId=nae-examplexxxx &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "NetworkAccessEndpoint":{
  "Status":"running",
  "InstanceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
  "VSwitchIds":"",
  "SecurityGroupId":"sg-examplexxx",
  "CreateTime":1649830226000,
  "NetworkAccessEndpointId":"nae_examplexxx",
  "NetworkAccessEndpointName":"VPCEndpointForXX",
  "EgressPrivateIpAddresses":"",
  "VpcId":"vpc-examplexxx",
  "UpdateTime":1649830226000,
  "VpcRegionId":"cn-hangzhou",
  "NetworkAccessEndpointType":"private",
  "EgressPublicIpAddresses":""
```

##### ListNetworkAccessEndpoints

Queries the network endpoints of an IDaaS EIAM instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| NextToke n | Strin g | Query | No | NTxxxxxexample | The pagination token that is used in the next request to retrieve a new page of results. You must specify the token that is obtained from the previous query as the value of NextToken. No token is returned for the first query. |
| MaxResult s | Long | Query | No | 20 | The maximum number of entries per page. Maximum value: 100. |

| Developer Gui | de·API R | eference |   |   | IDaa |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| NetworkA ccessEndp ointType | Strin g | Query | No | private | The type of the network endpoint. Valid values: shared: shared network endpoint. private: dedicated network endpoint. Default value: private. |
| VpcId | Strin g | Query | No | vpc-examplexxx | The ID of the virtual private cloud (VPC) to which the network endpoint is connected. This parameter does not take effect when NetworkAccessEndpoint Type is set to shared. |
| VpcRegio nId | Strin g | Query | No | cn-hangzhou | The region of the VPC to which the network endpoint is connected. The ID of the region must be returned by the ListNetworkAccessEndp ointAvailableRegions operation. This parameter does not take effect when NetworkAccessEndpoint Type is set to shared. |
| NetworkA ccessEndp ointStatus | Strin g | Query | No | running | The status of the network endpoint. Valid values: Pending: The network endpoint is pending for initialization. creating: The network endpoint is being created. running: The network endpoint is running. deleting: The access path is being deleted. This parameter does not take effect when NetworkAccessEndpoint Type is set to shared. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Long | 100 | The total number of entries returned. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| NextToken | String | NTxxxexample | The token returned in the current call. |
| NetworkAcces sEndpoints | Array | Struct | The network endpoints. |
| -InstanceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The instance ID. |
| - NetworkAcces sEndpointId | String | nae examplexxx _ | The ID of the network endpoint. |
| - NetworkAcces sEndpointNam e | String | VPCEndpointForXX | The name of the network endpoint. |
| -VpcId | String | vpc-examplexxx | The ID of the VPC to which the network endpoint is connected. |
| -VpcRegionId | String | cn-hangzhou | The region ID of the VPC to which the network endpoint is connected. |
| - SecurityGroupI d | String | sg-examplexxx | The ID of the security group used by the network endpoint. |
| -Status | String | running | The status of the network endpoint. Valid values: Pending: The network endpoint is pending for initialization. creating: The network endpoint is being created. running: The network endpoint is running. deleting: The network endpoint is being deleted. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| - NetworkAcces sEndpointType | String | private | The type of the network endpoint. Valid values: shared: shared network endpoint. private: dedicated network endpoint. |
| -CreateTime | Long | 1649830226000 | The time when the network endpoint was created. This value is a UNIX timestamp. Unit: milliseconds. |
| -UpdateTime | Long | 1649830226000 | The time when the network endpoint was updated. This value is a UNIX timestamp. Unit: milliseconds. |
| -VSwitchIds | String | vsw-examplexxx | The vSwitches that are connected to the network endpoint. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListNetworkAccessEndpoints &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &<Common request parameters>
```

Sample responses `JSON` format

```json
 "TotalCount":100,
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "NextToken":"NTxxxexample",
 "NetworkAccessEndpoints":[
   "Status":"running",
   "VpcId":"vpc-examplexxx",
   "InstanceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
   "VSwitchIds":"",
   "SecurityGroupId":"sg-examplexxx",
   "CreateTime":1649830226000,
   "UpdateTime":1649830226000,
   "NetworkAccessEndpointId":"nae_examplexxx",
   "VpcRegionId":"cn-hangzhou",
   "NetworkAccessEndpointName":"VPCEndpointForXX",
   "NetworkAccessEndpointType":"private"
```

`]`

##### ListNetworkAccessPaths

Queries the access paths of a dedicated endpoint.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| NetworkA ccessEndp ointId | Strin g | Query | Yes | nae examplexxxx _ | The ID of the dedicated endpoint. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| NetworkAcces sPaths | Array | Struct | The list of access paths. |
| -InstanceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The instance ID. |
| - NetworkAcces sEndpointId | String | nae examplexxx _ | The ID of the dedicated endpoint. |
| - NetworkAcces sPathId | String | nap examplexxx _ | The ID of the access path. |
| - NetworkInterfa ceId | String | eni-examplexxx | The elastic network interface (ENI) ID used by the access path. |
| -VSwitchId | String | vsw-examplexxx | The ID of the vSwitch to which the ENI used by the access path belongs. |
| - PrivateIpAddre ss | String | cn-hangzhou | The private IP address of the ENI used by the access path. |

| Developer Guide·A | PI Reference |   | IDaa |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Status | String | running | The status of the access path. Valid values: Pending: The access path is pending for initialization. creating: The access path is being created. running: The access path is running. deleting: The access path is being deleted. |
| -CreateTime | Long | 1649830226000 | The time when the access path was created. The value is a UNIX timestamp. Unit: milliseconds. |
| -UpdateTime | Long | 1649830226000 | The time when the access path was updated. The value is a UNIX timestamp. Unit: milliseconds. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListNetworkAccessPaths &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &NetworkAccessEndpointId=nae_examplexxxx &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "NetworkAccessPaths":[
   "Status":"running",
   "NetworkAccessPathId":"nap_examplexxx",
   "PrivateIpAddress":"cn-hangzhou",
   "InstanceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
   "VSwitchId":"vsw-examplexxx",
   "CreateTime":1649830226000,
   "UpdateTime":1649830226000,
   "NetworkAccessEndpointId":"nae_examplexxx",
   "NetworkInterfaceId":"eni-examplexxx"
```

`]`

##### Query the VPCs within a user account

**when creating a network endpoint**

Queries the list of VPCs within a user account when creating a network endpoint.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| ResourceS etId | Strin g | Query | Yes | 12 | The ID of the resource set. |
| PageNum ber | Long | Query | No | 1 | The page number. |
| PageSize | Long | Query | No | 10 | The number of entries per page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Vpcs | Array | VPC list | The list of VPCs. |
| -Description | String | Test | The description. |
| -VpcId | String | vpc-examplexxx | The VPC ID. |
| -CidrBlock | String | 10.0.0.0/24 | The CIDR block of the vSwitch. |
| -VpcName | String | Name | The VPC name. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListVpcs &ResourceSetId=12 &<Common request parameters>
```

Sample success responses

```json
 JSON format
 "Vpcs":[
   "Description":"Test",
   "VpcId":"vpc-examplexxx",
   "CidrBlock":"10.0.0.0/24",
   "VpcName":"Name"
```

`],`

```json
 "TotalCount":100,
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### ListVSwitches

Queries a list of vSwitches in a virtual private cloud (VPC) when a network access endpoint is created.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| PageNum ber | Long | Query | No | 1 | The page number. |
| PageSize | Long | Query | No | 10 | The number of entries per page. |
| VpcId | Strin g | Query | Yes | vpc-examplexxx | The VPC ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| VSwitches | Array | A list of vSwitches | The queried vSwitches. |
| -Description | String | Use for testing | The description of the vSwithes. |
| -VpcId | String | vpc-examplexxx | The VPC ID. |
| -ZoneId | String | cn-hangzhou-h | The zone ID. |
| -VSwitchId | String | vsw-examplexxx | The vSwitch ID. |
| - AvailableIpAdd ressCount | Integer | 253 | The number of available IP addresses in the vSwitch. |
| -CidrBlock | String | 10.0.0.0/24 | The CIDR block of the vSwitch. |
| -VSwitchName | String | test | The name of the vSwitch. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListVSwitches &VpcId=vpc-examplexxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "TotalCount":100,
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "VSwitches":[
   "Description":"test",
   "VpcId":"vpc-examplexxx",
   "ZoneId":"cn-hangzhou-h",
   "VSwitchId":"vsw-examplexxx",
   "AvailableIpAddressCount":253,
   "CidrBlock":"10.0.0.0/24",
   "VSwitchName":"test"
```

`]`

##### ListNetworkInterfaces

Queries a list of elastic network interfaces (ENIs) associated with network endpoints.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| PageNum ber | Long | Query | No | 1 | The page number. |
| PageSize | Long | Query | No | 10 | The number of entries per page. |
| NetworkIn terfaceId | Array | Query | No | eni-bp67acfmxazb4p**** | The ID of the ENI. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| NetworkInterfa ceSets | Array | ENI list | The list of ENIs. |
| - SecurityGroupI ds | String | Security group ID list | The list of security group IDs. |

| I | DaaS |   |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Status | String | Available | The status of the ENI. Valid values: ● Available: The ENI is available. ● Attaching: The ENI is being attached to the network endpoint. ● InUse: The ENI is attached to the network endpoint. ● Detaching: The ENI is being detached from the network endpoint. ● Deleting: The ENI is being deleted. |
| -Type | String | Primary | The type of the ENI. Valid values: ● Primary: the primary ENI. ● Secondary: the secondary ENI. |
| - PrivateIpAddre ss | String | ENI primary private IP address | The primary private IP address of the ENI. |
| -Description | String | Test | The description of ENI. |
| -VpcId | String | vpc-examplexxx | The ID of the virtual private cloud (VPC) to which the ENI belongs. |
| -ZoneId | String | cn-hangzhou-h | The ID of the zone to which the ENI belongs. |
| -VSwitchId | String | vsw-examplexxx | The ID of the vSwitch to which the ENI belongs. |
| - NetworkInterfa ceId | String | eni-examplexxx | The ID of the ENI. |
| - AssociatedPub licIp | Struct | Public IP address | The elastic IP address (EIP) that is associated with the secondary private IP address of the ENI. |
| -- PublicIpAddres s | String | 116.62.**.** | The EIP. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListNetworkInterfaces &<Common request parameters>
```

Sample responses `JSON` format

```json
 "TotalCount":100,
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "NetworkInterfaceSets":[
   "Status":"Available",
   "AssociatedPublicIp":[
     "PublicIpAddress":"116.62.**.**"
```

`],`

```json
   "Type":"Primary",
   "PrivateIpAddress":"ENI private IP address",
   "Description":"Test",
   "VpcId":"vpc-examplexxx",
   "ZoneId":"cn-hangzhou-h",
   "VSwitchId":"vsw-examplexxx",
   "NetworkInterfaceId":"eni-examplexxx",
   "SecurityGroupIds":"Security group ID list"
```

`]`

##### ListNatGateways

Queries the outbound public IP addresses of a dedicated endpoint.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |
| PageNum ber | Long | Query | No | 1 | The page number. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageSize | Long | Query | No | 10 | The number of entries per page. |
| VpcId | Strin g | Query | Yes | vpc-examplexxx | The ID of the virtual private cloud (VPC) to which the dedicated endpoint is connected. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| NatGateways | Array | NAT gateway list | The list of NAT gateways. |
| -IpLists | Array | IP list | The list of outbound public IP addresses. |
| --UsingStatus | String | UsedByForwardTab le | The association between the elastic IP address (EIP) and the Internet NAT gateway. Valid values: UsedByForwardTable: The EIP is specified in a DNAT entry. UsedBySnatTable: The EIP is specified in an SNAT entry. UsedByForwardSnatTable: The EIP is specified in both an SNAT entry and a DNAT entry. Idle: The EIP is not specified in an SNAT entry or a DNAT entry. |
| -- PrivateIpAddre ss | String | 172.17.**.** | The private IP address of the NAT gateway. |
| --AllocationId | String | eip- 25877c70gddh**** | The ID of the EIP associated with the NAT gateway. |
| --IpAddress | String | 192.168.XX.XX | The IP address of the EIP associated with the NAT gateway. |
| -Description | String | NAT gateway description | The description of the NAT gateway. |
| -VpcId | String | vpc-examplexxx | The ID of the VPC to which the NAT gateway belongs. |
| -NetworkType | String | internet | internet: Internet NAT gateway intranet: VPC NAT gateway |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -EipBindMode | String | MULTI BINDED _ | MULTI BINDED: multi-EIP-to-ENI mode _ NAT: NAT mode. IPv4 gateways are supported. |
| -RegionId | String | cn-hangzhou | The region ID. |
| -NatType | String | Enhanced | The type of NAT gateway. The value Enhanced is returned. |
| -NatGatewayId | String | nat- 5t7nh1cfm6kxiszltt r38**** | The ID of the NAT gateway. |
| -Name | String | test | The name of the NAT gateway. |
| TotalCount | Integer | 100 | The total number of entries returned. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListNatGateways &VpcId=vpc-examplexxx &<Common request parameters>
```

Sample responses `JSON` format

```json
 "TotalCount":100,
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "NatGateways":[
   "Description":"NAT gateway description",
   "VpcId":"vpc-examplexxx",
   "NetworkType":"internet",
   "EipBindMode":"MULTI_BINDED",
   "IpLists":[
     "UsingStatus":"UsedByForwardTable",
     "PrivateIpAddress":"172.17.**.**",
     "AllocationId":"eip-25877c70gddh****",
     "IpAddress":"192.168.XX.XX"
```

`],`

```json
   "RegionId":"cn-hangzhou",
   "NatType":"Enhanced",
   "NatGatewayId":"nat-5t7nh1cfm6kxiszlttr38****",
   "Name":"test"
```

`]`

##### CheckServiceLinkedRoleExistence

Checks whether a service-linked role exists.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| Exists | Boolean | true | Indicates whether the service-linked role exists. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CheckServiceLinkedRoleExistence &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "Exists":true
```

##### CreateServiceLinkedRole

Creates a service-linked role.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateServiceLinkedRole &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

#### Brand

##### CreateBrand

Creates a brand.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| BrandNam e | Strin g | Query | Yes | Custom Brand | The brand name. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| BrandId | String | brand xxxx _ | The brand ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=CreateBrand &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &BrandName=Custom Brand &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "BrandId":"brand_xxxx"
```

##### UpdateBrand

Modifies a brand.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| BrandId | Strin g | Query | Yes | brand xxxx _ | The brand ID. |
| BrandNam e | Strin g | Query | Yes | Custom Brand | The brand name. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=UpdateBrand &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &BrandId=brand_xxxx &BrandName=Custom Brand &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

#### Network zones

##### Create a network zone

Creates a network zone.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| NetworkZ oneName | Strin g | Query | Yes | IPV4Test | The name of the network zone. |
| Descriptio n | Strin g | Query | No | Test description | The description of the network zone. |
| NetworkZ oneType | Strin g | Query | Yes | arn:alibaba:idaas:networ k:zone:classic | The type of the network zone. |
| Ipv4Cidrs | Array | Query | No | 0.0.0.0/0 | The IPv4 CIDR block of the network zone. |
| Ipv6Cidrs | Array | Query | No | ::/0 | The IPv6 CIDR block of the network zone. |
| VpcId | Strin g | Query | No | vpc xxxxx _ | The VPC ID. |
| ClientToke n | Strin g | Query | No | client-token-example | The client token that is used to ensure the idempotence of the request. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| NetworkZoneI d | String | network m6a57vre _ 4g3h7m725yrq6px xxx | The ID of the network zone. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

Sample requests

```
http(s)://[Endpoint]/?Action=CreateNetworkZone &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &NetworkZoneName=IPV4Test &NetworkZoneType=arn:alibaba:idaas:network:zone:classic &<Common request parameters>
```

Sample success responses

```json
 JSON format
 "NetworkZoneId":"network_m6a57vre4g3h7m725yrq6pxxxx",
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### DeleteNetworkZone

Deletes a network zone.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| NetworkZ oneId | Strin g | Query | Yes | network 11111 _ | The network zone ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteNetworkZone &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &NetworkZoneId=network_11111 &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### UpdateNetworkZone

Modifies a network zone.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| NetworkZ oneId | Strin g | Query | Yes | network 11111 _ | The ID of the network zone. |
| NetworkZ oneName | Strin g | Query | Yes | IPV4Test | The name of the network zone. |
| Ipv4Cidrs | Array | Query | No | 192.168.1.0/24 | The IPv4 CIDR block of the network zone. |
| Ipv6Cidrs | Array | Query | No | 2001:db8::/32 | The IPv6 CIDR block of the network zone. |

| Developer Gui | de·API R | eference |   |   | IDaa |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| VpcId | Strin g | Query | No | vpc xxxxx _ | The ID of the virtual private cloud (VPC). |
| ClientToke n | Strin g | Query | No | client-token- examplexxxx | The client token that is used to ensure the idempotence of the request. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=UpdateNetworkZone &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &NetworkZoneId=network_11111 &NetworkZoneName=IPV4Test &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### Update the description of a network zone

**object**

Updates the description of a network zone object.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| NetworkZ oneId | Strin g | Query | Yes | network m5wsaclfvfrf56 _ 23xnirgxxxxx | The ID of the network zone. |
| Descriptio n | Strin g | Query | Yes | Test description | The description of the network zone. |
| ClientToke n | Strin g | Query | No | client-token- examplexxxx | The client token that is used to ensure the idempotence of the request. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=UpdateNetworkZoneDescription &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &NetworkZoneId=network_m5wsaclfvfrf5623xnirgxxxxx &Description=Test description &<Common request parameters>
```

Sample success responses

```json
 JSON format
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### ListNetworkZones

Queries a list of network zones.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| NextToke n | Strin g | Query | No | NTxxxxxexample | The pagination token that is used in the request to retrieve a new page of results. |
| MaxResult s | Long | Query | No | 20 | The maximum number of entries per page. |
| PreviousT oken | Strin g | Query | No | PTxxxxxexample | The token that was returned in the last call made to the API operation. |
| NetworkZ oneIds | Array | Query | No | ["zone1", "zone2"] | The list of network zone IDs. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| NetworkZones | Array | Struct | The list of network zones. |
| -InstanceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The instance ID. |
| - NetworkZoneI d | String | network m223wbv _ c3sn3uakfnxvhbxx xxx | The ID of the network zone. |
| - NetworkZoneN ame | String | test name _ | The name of the network zone. |
| -Description | String | test | The description of the network zone. |
| - NetworkZoneT ype | String | arn:alibaba:idaas:n etwork:zone:classic | The type of the network zone. |

| DaaS |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -VpcId | String | vpc- bp1usdmfqcgoy5e bxxxxx | The virtual private cloud (VPC) ID. |
| -Ipv4Cidrs | String | 192.168.1.0/24 | The IPv4 CIDR block of the network zone. |
| -Ipv6Cidrs | String | 2001:db8::/32 | The IPv6 CIDR block of the network zone. |
| TotalCount | Long | 100 | The total number of entries returned. |
| PreviousToken | String | PTxxxxxexample | The token that was returned in the last call made to the API operation. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| NextToken | String | NTxxxexample | The token returned in the current call. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ListNetworkZones &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &<Common request parameters>
```

Sample responses `JSON` format

```json
 "NetworkZones":[
   "NetworkZoneId":"network_m223wbvc3sn3uakfnxvhbxxxxx",
   "Description":"test",
   "VpcId":"vpc-bp1usdmfqcgoy5ebxxxxx",
   "InstanceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
   "Ipv6Cidrs":"",
   "NetworkZoneName":"test_name",
   "NetworkZoneType":"arn:alibaba:idaas:network:zone:classic",
   "Ipv4Cidrs":""
```

`],`

```json
 "TotalCount":100,
 "PreviousToken":"PTxxxxxexample",
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "NextToken":"NTxxxexample"
```

##### GetNetworkZone

Queries a network zone.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| NetworkZ oneId | Strin g | Query | Yes | network 11111 _ | The Network zone ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| NetworkZone | Struct | object | The network zone. |
| -InstanceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The instance ID. |
| - NetworkZoneI d | String | network m6fbr2bc _ bcadu3bcdpgzcxxx xx | The Network zone ID. |
| - NetworkZoneN ame | String | test4 name _ | The name of the network zone. |
| -Description | String | test description _ | The description of the network zone. |
| - NetworkZoneT ype | String | arn:alibaba:idaas:n etwork:zone:classic | The type of the network zone. |
| -VpcId | String | vpc-25w8wxxxx | The virtual private cloud (VPC) ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Ipv4Cidrs | String | 192.168.1.0/24 | The IPv4 CIDR block of the network zone. |
| -Ipv6Cidrs | String | 2001:db8::/32 | The IPv6 CIDR block of the network zone. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=GetNetworkZone &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &NetworkZoneId=network_11111 &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "NetworkZone":{
  "NetworkZoneId":"network_m6fbr2bcbcadu3bcdpgzcxxxxx",
  "Description":"test_description",
  "VpcId":"vpc-25w8wxxxx",
  "InstanceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
  "Ipv6Cidrs":"",
  "NetworkZoneName":"test4_name",
  "NetworkZoneType":"arn:alibaba:idaas:network:zone:classic",
  "Ipv4Cidrs":""
```

#### Others

##### DisableIdentityProviderAuthn

Disables the identity provider authentication feature.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | eiam-111ccc1111 | The instance ID. |
| IdentityPr oviderId | Strin g | Query | Yes | idp 11111 _ | The ID of the Identity Provider (IdP). |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DisableIdentityProviderAuthn &InstanceId=eiam-111ccc1111 &IdentityProviderId=idp_11111 &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### EnableIdentityProviderAuthn

Enables authentication.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | eiam-111ccc1111 | The instance ID. |

| DaaS |   |   |   | Dev | eloper Guide·API Referenc |
|---|---|---|---|---|---|
| Parame ter | Typ e | Positi on | Require d | Example | Description |
| IdentityPr oviderId | Strin g | Query | Yes | idp 11111 _ | The identity provider (IdP) ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=EnableIdentityProviderAuthn &InstanceId=eiam-111ccc1111 &IdentityProviderId=idp_11111 &<Common request parameters>
```

Sample responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

**1.4.12.3.**

##### ListApplicationSupportedProvisionProtocolTypes

Queries a list of synchronization protocol types that are supported by an application.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |

| Developer Gui | de·API R | eference |   |   | IDaa |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Applicatio nId | Strin g | Query | Yes | app mkv7rgt4d7i4u7zqt _ zev2mxxxx | The application ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ApplicationSup portedProvisio nProtocolType | Struct | object | The synchronization protocol types that are supported by the application. |
| - ProvisionProto colType | String | The synchronization protocol type of the application account. Valid values: idaas callback: _ event callback protocol of Identity as a Service (IDaaS). scim2: System for Cross- domain Identity Management (SCIM) protocol. | Type |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=ListApplicationSupportedProvisionProtocolTypes &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &ApplicationId=app_mkv7rgt4d7i4u7zqtzev2mxxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "ApplicationSupportedProvisionProtocolType":{
  "ProvisionProtocolType":""
```

`},`

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### Delete a brand

Deletes a brand.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| BrandId | Strin g | Query | Yes | brand xxxx _ | The brand ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DeleteBrand &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &BrandId=brand_xxxx &<Common request parameters>
```

Sample success responses

```json
 JSON format
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### Disables a brand

Disables a brand.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| BrandId | Strin g | Query | Yes | brand xxxx _ | The brand ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=DisableBrand &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &BrandId=brand_xxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### EnableBrand

Enables a brand.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| BrandId | Strin g | Query | Yes | brand xxxx _ | The brand ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=EnableBrand &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &BrandId=brand_xxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### GetBrand

Queries the detailed information about a brand.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |

|   | Developer Gui | de·API R | eference |   |   | IDaa | S |
|---|---|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| BrandId | Strin g | Query | Yes | brand xxxx _ | The brand ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Brand | Struct | object | The brand. |
| -InstanceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The instance ID. |
| -BrandId | String | brand xxxx _ | The brand ID. |
| -BrandName | String | Custom Brand | The brand name. |
| -BrandType | String | user custom _ | The brand type. |
| -Status | String | enabled | The brand status. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=GetBrand &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &BrandId=brand_xxxx &<Common request parameters>
```

Sample responses `JSON` format

```json
 "Brand":{
  "BrandName":"Custom Brand",
  "Status":"enabled",
  "BrandType":"user_custom",
  "InstanceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
  "BrandId":"brand_xxxx"
```

`},`

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### GetLoginRedirectApplicationForBrand

Configures redirection to an application after Single Sign-On (SSO) for a brand.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| BrandId | Strin g | Query | Yes | brand xxxx _ | The brand ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| BrandLoginRe directApplicati on | Struct | object | The information about the application to which users are redirected. |
| -InstanceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The instance ID. |
| -BrandId | String | brand xxxx _ | The brand ID. |
| -ApplicationId | String | app xxxx _ | The application ID. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=GetLoginRedirectApplicationForBrand &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &BrandId=brand_xxxx &<Common request parameters>
```

Sample responses `JSON` format

```json
 "BrandLoginRedirectApplication":{
  "InstanceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
  "BrandId":"brand_xxxx",
  "ApplicationId":"app_xxxx"
```

`},`

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### Query a list of brands

Queries a list of brands

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| NextToke n | Strin g | Query | No | NTxxxxxexample | The pagination token that is used in the request to retrieve a new page of results. |
| PreviousT oken | Strin g | Query | No | PTxxxxxexample | The token that was returned in the last call made to the API operation. |
| MaxResult s | Long | Query | No | 20 | The maximum number of entries per page. |

| DaaS |   |   |   | Dev | eloper Guide·API Referenc |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Long | 100 | The total number of entries returned. |
| PreviousToken | String | PTxxxexample | A pagination token. |
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |
| NextToken | String | NTxxxexample | A pagination token. It can be used in the next request to retrieve a new page of results. |
| MaxResults | Long | 20 | The maximum number of entries per page. |
| Brands | Array | array | A list of brands. |
| -InstanceId | String | idaas ue2jvisn35e _ a5lmthk267xxxxx | The instance ID. |
| -BrandId | String | brand xxxx _ | The brand ID. |
| -BrandName | String | Custom Brand | The brand name. |
| -BrandType | String | user custom _ | The brand type. |
| -Status | String | enabled | The brand status. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=ListBrands &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &<Common request parameters>
```

Sample success responses

```json
 JSON format
 "TotalCount":100,
 "PreviousToken":"PTxxxexample",
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A",
 "NextToken":"NTxxxexample",
 "MaxResults":20,
 "Brands":[
   "BrandName":"Custom Brand",
   "Status":"enabled",
   "BrandType":"user_custom",
   "InstanceId":"idaas_ue2jvisn35ea5lmthk267xxxxx",
   "BrandId":"brand_xxxx"
```

`]`

##### SetLoginRedirectApplicationForBrand

Configures the application to which users are redirected after login for a brand.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| BrandId | Strin g | Query | Yes | brand xxxx _ | The brand ID. |
| Applicatio nId | Strin g | Query | Yes | app xxxx _ | The application ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=SetLoginRedirectApplicationForBrand &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &BrandId=brand_xxxx &ApplicationId=app_xxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

##### Changes the brand associated with a

**domain name**

Changes the brand associated with a domain name.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the Common parameters topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | idaas ue2jvisn35ea5lmt _ hk267xxxxx | The instance ID. |
| DomainId | Strin g | Query | Yes | dm examplexxxxx _ | The domain ID. |
| BrandId | Strin g | Query | Yes | brand xxxx _ | The brand ID. |
| RegionId | Strin g | Host | No | cn-hangzhou | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0441BD79-92F3- 53AA-8657- F8CE4A2B912A | The request ID. |

**Examples**

Sample requests

```
https://[Endpoint]/?Action=UpdateDomainBrand &InstanceId=idaas_ue2jvisn35ea5lmthk267xxxxx &DomainId=dm_examplexxxxx &BrandId=brand_xxxx &<Common request parameters>
```

Sample success responses `JSON` format

```json
 "RequestId":"0441BD79-92F3-53AA-8657-F8CE4A2B912A"
```

### Release notes

**Update date: October 23, 2025**

Release description: The first time Identity as a Service (IDaaS) released on Apsara Stack. All API operations of IDaaS are available.
1. List of operations by function

**1.1. Instances**

| No. | API | Title | Description |
|---|---|---|---|
| 1 | CreateApsaraEiamInstance | CreateApsaraEiamInstance | Creates an instance to use all capabilities of IDaaS Enterprise Identity Access Management (EIAM). |
| 2 | DeleteApsaraEiamInstance | DeleteApsaraEiamInstance | Deletes an IDaaS EIAM instance. |
| 3 | UpdateApsaraEiamInstance Description | UpdateApsaraEiamInstance Description | Modifies the description of an IDaaS EIAM instance. |
| 4 | ListApsaraEiamInstances | ListApsaraEiamInstances | Queries the information about one or more IDaaS EIAM instances. |
| 5 | UpdateApsaraEiamInstance Quota | UpdateApsaraEiamInstance Quota | Queries the detailed information about an IDaaS EIAM instance. |

| 6 | GetInstanceLicense | GetInstanceLicense | Queries the valid license of an IDaaS EIAM instance. |
|---|---|---|---|

**1.2. Applications**

| No. | API | Title | Description |
|---|---|---|---|
| ç | Application basics | Application basics |   |
| 1 | CreateApplication | CreateApplication | Creates an application on an EIAM instance of IDaaS. |
| 2 | DeleteApplication | DeleteApplication | Deletes an EIAM application. |
| 3 | UpdateApplicationDescriptio n | UpdateApplicationDescription | Modifies the description of an EIAM application. |
| 4 | EnableApplication | EnableApplication | Enables an EIAM application. |
| 5 | DisableApplication | DisableApplication | Disables an EIAM application. All features of the EIAM application become unavailable. |
| 6 | GetApplication | GetApplication | Queries the detailed information about an EIAM application. |
| 7 | ListApplications | ListApplications | Queries the information about one or more EIAM applications by page. |
| 8 | GetApplicationTemplate | GetApplicationTemplate | Queries the information about an application template in IDaaS EIAM. |
| 9 | UpdateApplicationInfo | UpdateApplicationInfo | Updates the basic information of an EIAM application. |
| 10 | ListApplicationsForNetworkA ccessEndpoint | ListApplicationsForNetworkAc cessEndpoint | Queries a list of applications associated with a network endpoint. |

| 11 | ListApplicationsForNetworkZ one | ListApplicationsForNetworkZo ne | Queries a list of applications associated with a network zone. |
|---|---|---|---|
| 12 | ListApplicationsForGroup | ListApplicationsForGroup | Queries a list of applications that an account group in IDaaS EIAM can access. |
| - | Application Single Sign-On (SSO) | Application SSO |   |
| 1 | EnableApplicationSso | EnableApplicationSso | Enables the SSO feature for an EIAM application. |
| 2 | DisableApplicationSso | DisableApplicationSso | Disables the SSO feature for an EIAM application. This way, users cannot log in to the application through SSO. |
| 3 | SetApplicationSsoConfig | SetApplicationSsoConfig | Configures the SSO attributes of an EIAM application. |
| 4 | GetApplicationSsoConfig | GetApplicationSsoConfig | Queries the SSO attributes of an EIAM application. |
| - | Application authorization | Application authorization |   |
| 1 | AuthorizeApplicationToUsers | AuthorizeApplicationToUsers | Grants the access permissions on an application to multiple EIAM accounts at a time. |
| 2 | AuthorizeApplicationToOrga nizationalUnits | AuthorizeApplicationToOrgani zationalUnits | Grants the access permissions on an application to multiple EIAM organizations at a time. |
| 3 | AuthorizeApplicationToGrou ps | AuthorizeApplicationToGroup s | Grants the access permissions on an application to multiple EIAM account groups at a time. |
| 4 | RevokeApplicationFromUser s | RevokeApplicationFromUsers | Revokes the access permissions on an application from multiple EIAM accounts at a time. |

| 5 | RevokeApplicationFromOrga nizationalUnits | RevokeApplicationFromOrgan izationalUnits | Revokes the access permissions on an application from multiple EIAM organizations at a time. |
|---|---|---|---|
| 6 | RevokeApplicationFromGrou ps | RevokeApplicationFromGroup s | Revokes the access permissions on an application from multiple EIAM account groups at a time. |
| 7 | UpdateApplicationAuthorizat ionType | UpdateApplicationAuthorizati onType | Modifies the authorization type of an EIAM application. |
| 8 | ListUsersForApplication | ListUsersForApplication | Queries the accounts that are allowed to access an EIAM application. The return results include the IDs of the accounts. If you need to obtain the details of the accounts, call the GetUser operation. |
| 9 | ListOrganizationalUnitsForA pplication | ListOrganizationalUnitsForAp plication | Queries the organizations that are allowed to access an EIAM application by page. The return result includes the IDs of the organizations. If you want to obtain the details of the organizations, call the GetOrganizationalUnit operation. |
| 10 | ListGroupsForApplication | ListGroupsForApplication | Queries the account groups that are granted permissions to access an application and displays the results by page. The IDs of the account groups are returned. To query the detailed information about the account groups, call the GetGroup operation. |

| 11 | ListApplicationsForUser | ListApplicationsForUser | Queries a list of applications that an EIAM account can access by page. The IDs of the applications are returned. To query the detailed information about the applications, call the GetApplication operation. |
|---|---|---|---|
| 12 | ListApplicationsForOrganizat ionalUnit | ListApplicationsForOrganizati onalUnit | Queries the applications that an EIAM organization can access. The return result includes the IDs of the applications. To query the detailed information about the applications, call the GetApplication operation. |
| - | Application federated credential management | Application federated credential management |   |
| 1 | UpdateApplicationFederated CredentialDescription | UpdateApplicationFederatedC redentialDescription | Modifies the description of an application federated credential. |
| 2 | UpdateApplicationFederated Credential | UpdateApplicationFederatedC redential | Renews an application federated credential. |
| 3 | ListApplicationFederatedCre dentials | ListApplicationFederatedCred entials | Queries a list of application federated credentials. |
| 4 | GetApplicationFederatedCre dential | GetApplicationFederatedCred ential | Queries an application federated credential. |
| 5 | EnableApplicationFederated Credential | EnableApplicationFederatedC redential | Enables an application federated credential. |
| 6 | DisableApplicationFederated Credential | DisableApplicationFederated Credential | Disables an application federated credential. |
| 7 | DeleteApplicationFederated Credential | DeleteApplicationFederatedC redential | Deletes an application federated credential. |
| 8 | CreateApplicationFederated Credential | CreateApplicationFederatedC redential | Creates an application federated credential. |
| - | Application client keys | Application client keys |   |

| 1 | CreateApplicationClientSecr et | CreateApplicationClientSecret | Creates a client key for an EIAM application. An EIAM application can have at most two client keys. |
|---|---|---|---|
| 2 | DeleteApplicationClientSecr et | DeleteApplicationClientSecret | Deletes a client key for an EIAM application. |
| 3 | DisableApplicationClientSecr et | DisableApplicationClientSecre t | Disables a client key of an EIAM application. |
| 4 | EnableApplicationClientSecr et | EnableApplicationClientSecre t | Enables a client key for an EIAM application. |
| 5 | ListApplicationClientSecrets | ListApplicationClientSecrets | Queries the client keys of an EIAM application. The returned keys are masked. To query unmasked keys, call the ObtainApplicationClientSecre t operation. |
| 6 | ObtainApplicationClientSecr et | ObtainApplicationClientSecret | Queries a client key of an EIAM application. The returned key is masked. To query the unmasked key, call the ListApplicationClientSecrets operation. |
| 7 | UpdateApplicationClientSecr etExpirationTime | UpdateApplicationClientSecre tExpirationTime | Updates the expiration time of a client key for an EIAM application. |
| - | Application tokens | Application tokens |   |
| 1 | CreateApplicationToken | CreateApplicationToken | Creates an application token. |
| 2 | EnableApplicationToken | EnableApplicationToken | Enables an application token. |
| 3 | DisableApplicationToken | DisableApplicationToken | Disables an application token. |
| 4 | UpdateApplicationTokenExpi rationTime | UpdateApplicationTokenExpir ationTime | Updates the expiration time of an application token. |

| 5 | ListApplicationTokens | ListApplicationTokens | Queries a list of application tokens. |
|---|---|---|---|
| 6 | ObtainApplicationToken | ObtainApplicationToken | Queries an application token. |
| 7 | DeleteApplicationToken | DeleteApplicationToken | Deletes an application token. |
| - | Application accounts | Application accounts |   |
| 1 | AddApplicationAccountToUs er | AddApplicationAccountToUse r | Adds an application account for an EIAM application. |
| 2 | ListApplicationAccounts | ListApplicationAccounts | Queries a list of application accounts that belong to an EIAM application by page. |
| 3 | ListApplicationAccountsForU ser | ListApplicationAccountsForUs er | Queries all application accounts of a user for an EIAM application. |
| 4 | RemoveApplicationAccountF romUser | RemoveApplicationAccountFr omUser | Deletes the application account of an employee from an EIAM application. |
| - | Open API operations | Open API operations |   |
| 1 | EnableApplicationApiInvoke | EnableApplicationApiInvoke | Enables the Developer API feature for an EIAM application. |
| 2 | DisableApplicationApiInvoke | DisableApplicationApiInvoke | Disables the Developer API feature for an EIAM application. |
| 3 | SetApplicationGrantScope | SetApplicationGrantScope | Configures the permissions of Developer API for an EIAM application. |
| 4 | GetApplicationGrantScope | GetApplicationGrantScope | Queries the permissions of Developer API for an EIAM application. |
| - | Application account synchronization | Application account synchronization |   |

| 1 | DisableApplicationProvisioni ng | DisableApplicationProvisionin g | Disables the account synchronization feature for an EIAM application. |
|---|---|---|---|
| 2 | EnableApplicationProvisionin g | EnableApplicationProvisionin g | Enables the account synchronization feature for an EIAM application. |
| 3 | SetApplicationProvisioningC onfig | SetApplicationProvisioningCo nfig | Configures the account synchronization feature for an EIAM application. |
| 4 | SetApplicationProvisioningS cope | SetApplicationProvisioningSc ope | Sets the account synchronization scope of an EIAM application. This scope also specifies the accounts that the Developer API can query and manage. |
| 5 | GetApplicationProvisioningC onfig | GetApplicationProvisioningCo nfig | Queries the configuration of the account synchronization feature for an EIAM application. |
| 6 | GetApplicationProvisioningS cope | GetApplicationProvisioningSc ope | Queries the account synchronization scope of an EIAM application. This scope also specifies the accounts that the Developer API can query and manage. |

**1.3. Accounts**

| No. | API | Title | Description |
|---|---|---|---|
| 1 | CreateUser | CreateUser | Creates an EIAM account for an IDaaS EIAM instance. |
| 2 | AddUserToOrganizationalUnit s | AddUserToOrganizationalUnit s | Adds an EIAM account to multiple IDaaS EIAM organizations. If the account already exists in an organization, a success response is returned. |
| 3 | DeleteUser | DeleteUser | Deletes an EIAM account. If you delete an EIAM account, the information related to the account is cleared. |

| 4 | RemoveUserFromOrganizatio nalUnts | RemoveUserFromOrganizatio nalUnits | Removes an EIAM account from multiple IDaaS EIAM organizations. You cannot remove an account from a primary organization. |
|---|---|---|---|
| 5 | UpdateUser | UpdateUser | Updates the basic information of an EIAM account. |
| 6 | UpdateUserPassword | UpdateUserPassword | Changes the password of an EIAM account. The password must meet the complexity rules in the IDaaS console. |
| 7 | UpdateUserDescription | UpdateUserDescription | Modifies the description of an EIAM account. |
| 8 | DisableUser | DisableUser | Disables an EIAM account. If the account is already disabled, a success response is returned. |
| 9 | EnableUser | EnableUser | Enables an EIAM account. |
| 10 | UnlockUser | UnlockUser | Unlocks an EIAM account. |
| 11 | SetUserPrimaryOrganizationa lUnit | SetUserPrimaryOrganizationa lUnit | Configures the primary organization to which an EIAM account belongs. The account is removed from its original primary organization and added to the new primary organization. |
| 12 | GetUser | GetUser | Queries the detailed information about an EIAM account. |
| 13 | ListUsers | ListUsers | Queries the detailed information about EIAM accounts by page. |

**1.4. Organizations**

| No . | API | Title | Description |
|---|---|---|---|

| DaaS |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| 1 | CreateOrganizationalUnit | CreateOrganizationalUnit | Creates an organization in IDaaS EIAM within a specific organization. |
|---|---|---|---|
| 2 | DeleteOrganizationalUnit | DeleteOrganizationalUnit | Deletes an organization in IDaaS EIAM. If the organization has EIAM accounts or subordinate organizations, the delete operation fails. |
| 3 | DeleteOrganizationalUnitChil dren | DeleteOrganizationalUnitChil dren | Deletes all data of an organization in IDaaS EIAM. You can forcefully delete all accounts and subordinate organizations of the specified organization. |
| 4 | UpdateOrganizationalUnit | UpdateOrganizationalUnit | Modifies the basic information about an organization in IDaaS EIAM. By default, if you do not specify the request parameters, the organization is not modified. |
| 5 | UpdateOrganizationalUnitDes cription | UpdateOrganizationalUnitDes cription | Modifies the description of an organization in IDaaS EIAM. |
| 6 | UpdateOrganizationalUnitPar entId | UpdateOrganizationalUnitPar entId | Changes the parent organization ID of an organization in IDaaS EIAM. In this case, the organization is moved to another parent node. |
| 7 | GetRootOrganizationalUnit | GetRootOrganizationalUnit | Queries the information about a root organization in IDaaS EIAM. |
| 8 | GetOrganizationalUnit | GetOrganizationalUnit | Queries the information about an organization in IDaaS EIAM. |
| 9 | ListOrganizationalUnits | ListOrganizationalUnits | Queries a list of organizations in IDaaS EIAM by page. |

| 10 | ListOrganizationalUnitParents | ListOrganizationalUnitParents | Queries a list of parent organizations of an organization in IDaaS EIAM. The results are sorted in descending order of the levels of the parent organizations. |
|---|---|---|---|

**1.5. Account groups**

| No. | API | Title | Description |
|---|---|---|---|
| 1 | CreateGroup | CreateGroup | Creates an EIAM account group. |
| 2 | AddUsersToGroup | AddUsersToGroup | Adds multiple EIAM accounts to an EIAM account group. |
| 3 | DeleteGroup | DeleteGroup | Deletes an EIAM account group. |
| 4 | RemoveUsersFromGro up | RemoveUsersFromGroup | Removes multiple accounts from an EIAM account group. |
| 5 | UpdateGroup | UpdateGroup | Modifies an EIAM account group. If no information is specified, the account group is not modified. |
| 6 | UpdateGroupDescripti on | UpdateGroupDescription | Modifies the description of an EIAM account group. |
| 7 | GetGroup | GetGroup | Queries the detailed information about an EIAM account group. |
| 8 | ListGroups | ListGroups | Queries a list of EIAM account groups. |
| 9 | ListUsersForGroup | ListUsersForGroup | Queries a list of accounts that belong to an EIAM account group. |
| 10 | ListGroupsForUser | ListGroupsForUser | Queries a list of EIAM account groups to which an account belongs. |

**1.6 Identity providers (IdPs)**

| No. | API | Title | Description |
|---|---|---|---|
| 1 | CreateIdentityProvider | CreateIdentityProvider | Creates an IdP. |
| 2 | DeleteIdentityProvider | DeleteIdentityProvider | Deletes an IdP. |
| 3 | UpdateIdentityProvider | UpdateIdentityProvider | Modifies the basic configuration of an IdP. |
| 4 | GetIdentityProvider | GetIdentityProvider | Queries an IdP. |
| 5 | ListIdentityProviders | ListIdentityProviders | Queries a list of IdPs. |
| 6 | EnableIdentityProviderUdPull | EnableIdentityProviderUdPull | Enables the IdP pulling feature. |
| 7 | DisableIdentityProviderUdPull | DisableIdentityProviderUdPull | Disables the IdP pulling feature. |
| 8 | SetIdentityProviderUdPullCon figuration | SetIdentityProviderUdPullCon figuration | Modifies the IdP pulling configuration. |
| 9 | GetIdentityProviderUdPullCon figuration | GetIdentityProviderUdPullCon figuration | Queries the IdP pulling configuration. |

**1.7. Password policies**

| No. | API | Title | Description |
|---|---|---|---|
| 1 | SetForgetPasswordConfigurati on | SetForgetPasswordCon figuration | Configures a forgot password policy for an IDaaS EIAM instance. |
| 2 | SetPasswordInitializationConfi guration | SetPasswordInitializati onConfiguration | Configures a password initialization policy for an IDaaS EIAM instance. |
| 3 | SetPasswordHistoryConfigurati on | SetPasswordHistoryCo nfiguration | Configures a password history policy for an IDaaS EIAM instance. |
| 4 | SetPasswordExpirationConfigu ration | SetPasswordExpiration Configuration | Configures a password expiration policy for an IDaaS EIAM instance. |

| 5 | SetPasswordComplexityConfig uration | SetPasswordComplexit yConfiguration | Configures a password complexity rule for an IDaaS EIAM instance. |
|---|---|---|---|
| 6 | GetForgetPasswordConfigurati on | GetForgetPasswordCo nfiguration | Queries the forgot password policy of an IDaaS EIAM instance. |
| 7 | GetPasswordInitializationConfi guration | GetPasswordInitializati onConfiguration | Queries the password initialization policy of an IDaaS EIAM instance. |
| 8 | GetPasswordHistoryConfigurat ion | GetPasswordHistoryCo nfiguration | Queries the password history policy of an IDaaS EIAM instance. |
| 9 | GetPasswordExpirationConfigu ration | GetPasswordExpiration Configuration | Queries the password expiration policy of an IDaaS EIAM instance. |
| 10 | GetPasswordComplexityConfig uration | GetPasswordComplexit yConfiguration | Queries the password complexity rule of an IDaaS EIAM instance. |

**1.8. Synchronization**

| No. | API | Title | Description |
|---|---|---|---|
| 1 | ListSynchronizationJobs | ListSynchronizationJobs | Queries a list of synchronization jobs. |
| 2 | RunSynchronizationJob | RunSynchronizationJob | Creates a synchronization job and immediately runs the job. |
| 3 | GetSynchronizationJob | GetSynchronizationJob | Queries the detailed information about a synchronization job. |

**1.9. Brands**

| No. | API | Title | Description |
|---|---|---|---|
| 1 | CreateBrand | CreateBrand | Creates a brand. |
| 2 | UpdateBrand | UpdateBrand | Modifies a brand. |

**1.10 Network endpoints**

| No. | API | Title | Description |
|---|---|---|---|
| 1 | CreateNetworkAccessEn dpoint | CreateNetworkAccessEndpoint | Creates a dedicated network endpoint. |
| 2 | DeleteNetworkAccessEnd point | DeleteNetworkAccessEndpoint | Deletes a dedicated network endpoint. |
| 3 | UpdateNetworkAccessEn dpointName | UpdateNetworkAccessEndpoin tName | Changes the name of a dedicated network endpoint. |
| 4 | ListNetworkAccessEndpoi ntAvailableRegions | ListNetworkAccessEndpointAv ailableRegions | Queries a list of regions in which network endpoints can be created. |
| 5 | ListNetworkAccessEndpoi ntAvailableZones | ListNetworkAccessEndpointAv ailableZones | Queries a list of zones within a region in which network endpoints can be created. |
| 6 | GetNetworkAccessEndpoi nt | GetNetworkAccessEndpoint | Queries the information about a network endpoint. |
| 7 | ListNetworkAccessEndpoi nts | ListNetworkAccessEndpoints | Queries a list of network endpoints of an IDaaS EIAM instance. |
| 8 | ListNetworkAccessPaths | ListNetworkAccessPaths | Queries a list of access paths for a network endpoint. |
| 9 | ListNetworkInterfaces | ListNetworkInterfaces | Queries a list of elastic network interfaces (ENIs) associated with a network point. |
| 10 | CheckServiceLinkedRole Existence | CheckServiceLinkedRoleExiste nce | Checks whether a service- linked role exists. |
| 11 | ListNatGateways | ListNatGateways | Queries the outbound public IP addresses of a network endpoint. |
| 12 | CreateServiceLinkedRole | CreateServiceLinkedRole | Creates a service-linked role. |
| 13 | ListVSwitches | ListVSwitches | Queries a list of vSwitches in the virtual private cloud (VPC) of a network endpoint. |

| 14 | ListVpcs | ListVpcs | Queries a list of VPCs available for an account when a network endpoint is created. |
|---|---|---|---|

**1.11 Network zones**

| No. | API | Title | Description |
|---|---|---|---|
| 1 | CreateNetworkZone | CreateNetworkZone | Creates a network zone. |
| 2 | DeleteNetworkZone | DeleteNetworkZone | Deletes a network zone. |
| 3 | UpdateNetworkZone | UpdateNetworkZone | Modifies a network zone. |
| 4 | UpdateNetworkZoneDescri ption | UpdateNetworkZoneDescription | Modifies the description of a network zone. |
| 5 | ListNetworkZones | ListNetworkZones | Queries a list of network zones. |
| 6 | GetNetworkZone | GetNetworkZone | Queries a network zone. |

**1.12. Others**

| No. | API | Title | Description |
|---|---|---|---|
| 1 | DisableIdentityProviderAuth n | DisableIdentityProviderAut hn | Disables the IdP authentication feature. |
| 2 | EnableIdentityProviderAuthn | EnableIdentityProviderAuth n | Enables the IdP authentication feature. |
| 3 | ListApplicationSupportedPro visionProtocolTypes | ListApplicationSupportedPr ovisionProtocolTypes | Queries a list of synchronization protocol types that are supported by an application. |
| 4 | DeleteBrand | DeleteBrand | Deletes a brand. |
| 5 | DisableBrand | DisableBrand | Disables a brand. |
| 6 | EnableBrand | EnableBrand | Enables a brand. |

| 7 | GetBrand | GetBrand | Queries the detailed information about a brand. |
|---|---|---|---|
| 8 | GetLoginRedirectApplication ForBrand | GetLoginRedirectApplicatio nForBrand | Queries the application to which users are redirected after login for a brand. |
| 9 | ListBrands | ListBrands | Queries a list of brands. |
| 10 | SetLoginRedirectApplication ForBrand | SetLoginRedirectApplicatio nForBrand | Configures the application to which users are redirected after login for a brand. |
| 11 | UpdateDomainBrand | UpdateDomainBrand | Modifies the brand associated with a domain name. |

## API Reference

### List of operations by function

The API operations of this product ( `EIAM DeveloperAPI/2022-02-25` ) use the resourceoriented architecture (ROA) style signature. For more information about signature details, see Request syntax and signature method. We offer SDKs in various popular programming languages, so that developers can call API operations in a plug-and-play manner, without delving into the technical details. If the SDKs provided cannot fully meet your requirements, you have the option to build your own SDK that is adapted to the signature mechanism. The process of creating custom signatures is complicated and may take approximately five days to complete. We recommend that you join the DingTalk group (ID: 78410016550) for assistance. Before you call an API operation, you must make sure that an Alibaba Cloud account is created and an AccessKey pair is created for the account. This way, you can call the API operation by using client tools such as SDKs and the CLI. For more information, see Obtain an AccessKey pair.

**OpenID Connect (OIDC) API operations**

| API operation | Title | Description |
|---|---|---|
| GenerateToken | GenerateToken | Generates an access token for an application in a specified Identity- as-a-Service Enterprise Identity Access Management (IDaaS EIAM) instance. |
| GenerateDeviceCode | GenerateDeviceCode | Generates a device code. |
| GetUserInfo | GetUserInfo | Queries the information of a user by using the user token. |
| RevokeToken | RevokeToken | Revokes an access token or refresh token. |

**API operations related to authorization scope**

| API operation | Title | Description |
|---|---|---|
| GetApplicationProvisioningSc ope | GetApplicationProvisioningSco pe | Queries the provisioning scope of an application in an instance. |

**API operations related to organization management**

| API operation | Title | Description |
|---|---|---|
| CreateOrganizationalUnit | CreateOrganizationalUnit | Creates an organizational unit. |
| PatchOrganizationalUnit | PatchOrganizationalUnit | Modifies an EIAM organizational unit. |
| GetOrganizationalUnit | GetOrganizationalUnit | Queries the information of an organizational unit. |
| DeleteOrganizationalUnit | GetOrganizationalUnit | Deletes an organizational unit. |

| API operation | Title | Description |
|---|---|---|
| ListOrganizationalUnits | ListOrganizationalUnits | Queries a list of EIAM organizations by page. |
| ListOrganizationalUnitParentI ds | ListOrganizationalUnitParentId s | Queries the information of all the parent organizational units of an organizational unit. |
| GetOrganizationalUnitIdByExt ernalId | GetOrganizationalUnitIdByExt ernalId | Obtains the ID of an organizational unit based on the external ID. |

**API operations related to account management**

| API operation | Title | Description |
|---|---|---|
| CreateUser | CreateUser | Creates an EIAM account in an organizational unit. |
| PatchUser | PatchUser | Modifies an EIAM account. |
| GetUser | GetUser | Queries the details of an EIAM account. |
| UpdateUserPassword | UpdateUserPassword | Updates the password of an EIAM account. |
| DeleteUser | DeleteUser | Deletes an EIAM account. |
| ListUsers | ListUsers | Queries the information of EIAM accounts by page. |
| EnableUser | EnableUser | Enables an EIAM account. |
| DisableUser | DisableUser | Disables an EIAM account. |
| GetUserIdByEmail | GetUserIdByEmail | Queries the ID of an EIAM account based on the email address. |
| GetUserIdByPhoneNumber | GetUserIdByPhoneNumber | Queries the ID of an EIAM account based on the mobile number. |
| GetUserIdByUserExternalId | GetUserIdByUserExternalId | Queries the ID of an EIAM account based on the external ID. |
| GetUserIdByUsername | GetUserIdByUsername | Queries the ID of an EIAM account based on the username. |
| SetUserPrimaryOrganizationa lUnit | SetUserPrimaryOrganizational Unit | Sets the primary organization to which an EIAM account belongs. The account is removed from the original primary organization and added to the new organization. |

| API operation | Title | Description |
|---|---|---|
| AddUserToOrganizationalUnit s | AddUserToOrganizationalUnits | Adds an EIAM account to multiple EIAM organizations. These organizations serve as subordinate organizations of the account. If the account already belongs to the specified organizations, no update is performed. |
| RemoveUserFromOrganizatio nalUnits | RemoveUserFromOrganization alUnits | Removes an EIAM account from multiple EIAM organizations. If the account no longer belongs to these organizations, the removal succeeds by default. |
| ListGroupsForUser | ListGroupsForUser | Queries a list of groups to which an EIAM account belongs. |

**API operations related to account group management**

| API operation | Title | Description |
|---|---|---|
| GetGroup | GetGroup | Queries the details of a group. |
| CreateGroup | CreateGroup | Creates a group. |
| PatchGroup | PatchGroup | Modifies the information of an EIAM group. |
| DeleteGroup | DeleteGroup | Deletes a group. |
| ListGroups | ListGroups | Queries the information of EIAM groups by page. |
| AddUsersToGroup | AddUsersToGroup | Adds multiple EIAM accounts to an EIAM group. If the accounts already belong to the specified group, no update is performed. |
| RemoveUsersFromGroup | RemoveUsersFromGroup | Removes multiple EIAM accounts from an EIAM group. If the accounts no longer belong to the group, the removal succeeds by default. |
| ListUsersForGroup | ListUsersForGroup | Queries a list of accounts in an EIAM group. |

### Endpoints

IDentity as a Service (IDaaS) provides developer API operations and allows network connectivity between a user virtual private cloud (VPC) and IDaaS. IDaaS endpoints are in the following format: developerapi-idaas-${global_region}.${internet_domain} To obtain the value of global_region and internet_domain, log in to the Apsara Uni-manager Management Console. In the top navigation bar, choose **Security > Identity and O&M**
**Security > IDaaS**. On the IDaaS page, find the required instance and click Console in the
Actions column. On the Quick Start page, view the **URL** in the upper-right corner. In the following example: The value of global_region is cn-ece-entity121-d01. The value of internet_domain is cloud.ece-group-121.com.

### API operations

#### OIDC API

##### GenerateToken

Generates an access token for an application in a specific IDentity as a Service Enterprise Identity Access Management (IDaaS EIAM) instance.

**Request syntax**

```
POST /v2/{instanceId}/{applicationId}/oauth2/token HTTP/1.1
```

**Request parameters**

| Parameter | Type | Requir ed | Description | Example |
|---|---|---|---|---|
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| client id _ | string | No | The client ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| client secret _ | string | No | The client key. This parameter must be specified when grant type is _ set to client credentials and _ client secret post is _ _ specified. | CSEHDcHcrUKHw1Cu xkJEHPveWRXBGqVq Rsxxxx |
| grant type _ | string | Yes | The authorization type. Valid values: client credentials: If you _ select this authorization type, you must specify client id and client secret. _ _ refresh token _ authorization code _ urn:ietf:params:oauth:gra nt-type:device code _ password | client credentials _ |
| code | string | No | The authorization code. This parameter must be specified when grant type is _ set to authorization code. _ | xxxx |
| username | string | No | The username. In password mode, this parameter must be specified. | uesrname 001 _ |
| password | string | No | The password. In password mode, this parameter must be specified. | xxxxxx |

| device code _ | string | No | The device code. This parameter must be specified when grant type is _ set to urn:ietf:params:oauth:grant- type:device code. _ | xxxx |
|---|---|---|---|---|
| redirect uri _ | string | No | The redirect URI. This parameter must be specified when grant type is _ set to authorization code. _ The value of this parameter must be the same as the redirect URI in the request to obtain the authorization code. | xxx |
| refresh token _ | string | No | The refresh token. This parameter must be specified when grant type is _ set to refresh token. _ | ATxxx |
| code verifier _ | string | No | The verification code when Proof Key for Code Exchange (PKCE) is enabled in authorization code mode. | xxx |
| exclusive tag _ | string | No | The excluded tags. | ATxxx |
| scope | string | No | The scope of related parameters. You can specify multiple values. Separate the values with spaces. Valid values: openid email phone profile | xxxx |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|
|   | object | Schema of Response |   |

| token type _ | string | The type of the token. Valid values: Basic Bearer Valid values of the two token types: Basic : Basic Bearer : Bearer | Bearer |
|---|---|---|---|
| access token _ | string | The access token. | ATxxx |
| refresh token _ | string | The refresh token. | RTxxx |
| expires in _ | integer | The validity period of the token. Unit: seconds. | 1200 |
| expires at _ | integer | The time when the token expires. This value is a UNIX timestamp. Unit: seconds. | 1653288641 |
| id token _ | string | The ID token. | xxxxx |

**Examples**

Sample success responses `JSON` format

```json
  "token_type": "Bearer",
  "access_token": "ATxxx",
  "refresh_token": "RTxxx",
  "expires_in": 1200,
  "expires_at": 1653288641,
  "id_token": "xxxxx"
```

##### GetUserInfo

Queries the information of a user based on the user token. Debug

**Debugging**

You can run this interface directly in OpenAPI Explorer, saving you the trouble of calculating signatures. After running successfully, OpenAPI Explorer dynamically generates SDK code samples for different programming languages.

**Request syntax**

GET /v2/{instanceId}/{applicationId}/oauth2/userinfo HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| Authorization | string | Yes | The authentication information. The value is in the Bearer ${access token} _ format. Example: Bearer ATxxxx. | Bearer xxxx |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|
|   | object | The response data. |   |
|   | any | The user information. | None |

**Examples**

Sample responses `JSON` format

```json
  "key": "None"
```

**Error codes**

For a list of error codes, see Service error codes.

**Change history**

| Updated at | Description | Operation |
|---|---|---|
| 2023-10-24 | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details |

**Error codes**

| HttpCode | Error Code | Error message | Description |
|---|---|---|---|
| 400 | invalid request _ | Application is not OIDC application | The application is not an OIDC application. |
| 400 | invalid token _ | Invalid token | The token is invalid. |
| 404 | application not found _ _ | Application id not found: app mkv7rgt4d7i4u7z _ qtzev2mxxxx | The application is not found. |
| 500 | Internal Server Error | Internal Server Error | An internal server error occurred. |

##### RevokeToken

Revokes an access token or refresh token. Debug

**Debugging**

You can run this interface directly in OpenAPI Explorer, saving you the trouble of calculating signatures. After running successfully, OpenAPI Explorer dynamically generates SDK code samples for different programming languages.

**Request syntax**

POST /v2/{instanceId}/{applicationId}/oauth2/revoke HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| client id _ | string | No | The client ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| client secret _ | string | No | The client secret. | CSEHDcHcrUKHw1Cu xkJEHPveWRXBGqVq Rsxxxx |
| token | string | Yes | The token to be revoked. | ATxxxx |
| token type hint _ _ | string | No | The type of the token. access token refresh token _ _ Valid values: access token: access _ token refresh token: refresh _ token | access token _ |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|
|   | object | The response data. |   |

**Examples**

Sample responses `JSON` format

```json
  "test": "test",
  "test2": 1
```

**Error codes**

For a list of error codes, see Service error codes.

**Change history**

| Updated at | Description | Operation |
|---|---|---|
| 2023-10-24 | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details |

#### API operations related to authorization

**scope**

##### GetApplicationProvisioningScope

Queries the synchronization scope of an application in an instance.

**Usage notes**

**Note**

You can go to the Applications page in the IDaaS console to set the synchronization scope. After an application is created, the application has the permission to call this operation by default. Debug

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request syntax**

GET /v2/{instanceId}/{applicationId}/provisioningScope HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The authentication information. The value is in the Bearer ${access token} _ format. Example: Bearer ATxxxx. | Bearer AT8csE2seYxxxxxij |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|
|   | object | The response data. |   |
| organizationalUnitIds | array | The organization IDs. |   |
| organizationalUnitId | string | The organization ID. | ou wovwffm62xifdzie _ m7an7xxxxx |
| groupIds | array | The group IDs. |   |
| groupIds | string | The group ID. | group wovwffm62xifd _ ziem7an7xxxxx |

**Examples**

Sample success responses `JSON` format

```json
  "organizationalUnitIds": [
    "ou_wovwffm62xifdziem7an7xxxxx"
```

`],`

```json
  "groupIds": [
    "group_wovwffm62xifdziem7an7xxxxx"
```

`]`

**Error codes**

For a list of error codes, see Service error codes.

**Change history**

| Change time | Summary of changes | Action |
|---|---|---|
| 2023-10-24 | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details |

**Error codes**

| HttpCode | Error Code | Error message | Description |
|---|---|---|---|
| 400 | invalid token _ | Access token is not valid | The token is invalid. |
| 404 | application not found _ _ | Application id not found: app 001 _ | The application is not found. |

| HttpCode | Error Code | Error message | Description |
|---|---|---|---|
| 403 | application disabled _ | Application is disabled | The application is disabled. |
| 403 | application api disable _ _ d | Application api invoke disabled | The application API is not available. |
| 403 | permission denied _ | Require scopes: [urn:alibaba:idaas:sco pe:user:read all] _ | The API authorization information is required. |
| 500 | Internal Server Error | Internal Server Error | An internal server error occurred. |

#### Organization management

##### CreateOrganizationalUnit

Creates an organization. Debug

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request syntax**

POST /v2/{instanceId}/{applicationId}/organizationalUnits HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The credential. The value is in the Bearer ${access token} format. _ Example: Bearer ATxxxx. | Bearer AT8csE2seYxxxxxij |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| body | object | No | The request body. |   |

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| organizational UnitName | string | Yes | The organization name. The name can be up to 64 characters in length. | name001 |
| parentId | string | Yes | The ID of the parent organization. | ou wovwffm62xifdzie _ m7an7xxxxx |
| organizational UnitExternalI d | string | No | The external ID of the organization. The external ID can be used to map external data to the data of the organization in Identity as a Service (IDaaS). By default, the external ID is the organization ID. The ID can be up to 64 characters in length. | ou wovwffm62xifdzie _ m7an7xxxxx |
| description | string | No | The organization description. The description can be up to 128 characters in length. | Test organization |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|
|   | object | The response parameters. |   |
| organizationalUnitId | string | The organization ID. | ou wovwffm62xifdziem _ 7an7xxxxx |

**Examples**

Sample success responses `JSON` format

```json
  "organizationalUnitId": "ou_wovwffm62xifdziem7an7xxxxx"
```

**Error codes**

For a list of error codes, see Service error codes.

**Change history**

| Time | Description | Operation |
|---|---|---|
| 2023-10-24 | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details |

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | invalid token _ | Access token is not valid | The token is invalid. |
| 400 | OrganizationUnitIdNotI nScopes | organizationUnitId : ou wovwffm62xifdzie _ m7an7xxxxx not in provisioning scope! | The organization is not synchronized. |
| 400 | MissingParameter.Org anizationalUnitName | The specified parameter:Organizatio nalUnitName is required! | organizationalUnitNam e is not specified. |
| 404 | application not found _ _ | Application id not found: app mkv7rgt4d7i4u7z _ qtzev2mxxxx | The application is not found. |
| 403 | application disabled _ | Application is disabled | The application is disabled. |
| 403 | application api disable _ _ d | Application api invoke disabled | The application API is not available. |
| 403 | permission denied _ | Require scopes: [urn:alibaba:idaas:sco pe:organizational unit: _ manage all] _ | The API authorization information is not specified. |
| 500 | Internal Server Error | Internal Server Error | An internal server error occurred. |

##### PatchOrganizationalUnit

Updates the information about an organization in Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM).

**Usage notes**

The operation conforms to the HTTP PATCH request method. The value of a parameter is modified only if the parameter is specified in the request. Debug

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request syntax**

PATCH /v2/{instanceId}/{applicationId}/organizationalUnits/{organizationalUnitId} HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The authentication information. The value is in the Bearer ${access token} _ format. Example: Bearer ATxxxx. | Bearer AT8csE2seYxxxxxij |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| organizationalUni tId | string | Yes | The organization ID. | ou wovwffm62xifdzie _ m7an7xxxxx |
| body | object | No | The request body. |   |
| organizational UnitName | string | No | The organization name. The name can be up to 64 characters in length. | name001 |
| description | string | No | The description of the organization. The description can be up to 128 characters in length. | Test organization |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|

This operation does not return any operation-specific parameters.

**Note**

If the request was successful, the HTTP status code 200 is returned by default.

**Examples**

Sample success responses `JSON` format `{}`

**Error codes**

For a list of error codes, see Service error codes.

**Change history**

| Change time | Summary of changes | Action |
|---|---|---|
| 2023-10-24 | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details |

**Error codes**

| HttpCode | Error Code | Error message | Description |
|---|---|---|---|
| 400 | invalid token _ | Access token is not valid | The token is invalid. |
| 400 | OrganizationUnitIdNotI nScopes | organizationUnitId : ou wovwffm62xifdzie _ m7an7xxxxx not in provisioning scope! | The organization is not synchronized. |
| 400 | ResourceDuplicated.Or ganizationalUnitName | The specified OrganizationalUnitNa me resource: xxx already exist! | The organization name already exists. |
| 404 | application not found _ _ | Application id not found: app mkv7rgt4d7i4u7z _ qtzev2mxxxx | The application is not found. |
| 403 | application disabled _ | Application is disabled | The application is disabled. |
| 403 | application api disable _ _ d | Application api invoke disabled | The application API is not available. |
| 403 | permission denied _ | Require scopes: [urn:alibaba:idaas:sco pe:organizational unit: _ manage all] _ | The API authorization information is required. |
| 500 | Internal Server Error | Internal Server Error | An internal server error occurred. |

##### GetOrganizationalUnit

Queries the information about an organization. Debug

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request syntax**

GET /v2/{instanceId}/{applicationId}/organizationalUnits/{organizationalUnitId} HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The credential. The value is in the Bearer ${access token} format. _ Example: Bearer ATxxxx. | Bearer AT8csE2seYxxxxxij |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| organizationalUni tId | string | Yes | The organization ID. | ou wovwffm62xifdzie _ m7an7xxxxx |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|
|   | object | The response parameters. |   |
| instanceId | string | The instance ID. | idaas ue2jvisn35ea _ 5lmthk267xxxxx |
| organizationalUnitId | string | The organization ID. | ou wovwffm62xifdz _ iem7an7xxxxx |
| organizationalUnitName | string | The organization name. | name001 |
| parentId | string | The ID of the parent organization. | ou wovwffm62xifdz _ iem7an7xxxxx |
| organizationalUnitExternalId | string | The external ID. | id wovwffm62xifdzi _ em7an7xxxxx |
|   |   | The source type of the organization. Valid values: build in: The _ organization was |   |

| Developer Guide·API Reference |   |   | IDaa |
|---|---|---|---|
| Parameter | Type | created in Identity as a DeSsecrvriicpet (iIoDnaaS). | Example |
| organizationalUnitSourceType | string | ding talk: The _ organization was imported from DingTalk. ad: The organization was imported from Microsoft Active Directory (AD). ldap: The organization was imported from a Lightweight Directory Access Protocol (LDAP) service. | build in _ |
| organizationalUnitSourceId | string | The source ID of the organization. | id wovwffm62xifdzi _ em7an7xxxxx |
| createTime | long | The time when the organization was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. | 1652083425923 |
| updateTime | long | The last time when the organization was updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. | 1652083425923 |
| description | string | The description. | xxxxx |

**Examples**

Sample success responses `JSON` format

```json
  "instanceId": "idaas_ue2jvisn35ea5lmthk267xxxxx",
  "organizationalUnitId": "ou_wovwffm62xifdziem7an7xxxxx",
  "organizationalUnitName": "name001",
  "parentId": "ou_wovwffm62xifdziem7an7xxxxx",
  "organizationalUnitExternalId": "id_wovwffm62xifdziem7an7xxxxx",
  "organizationalUnitSourceType": "build_in",
  "organizationalUnitSourceId": "id_wovwffm62xifdziem7an7xxxxx",
  "createTime": 1652083425923,
  "updateTime": 1652083425923,
  "description": "xxxxx"
```

**Error codes**

For a list of error codes, see Service error codes.

**Change history**

| Time | Description | Operation |
|---|---|---|
| 2023-10-24 | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details |

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | invalid token _ | Access token is not valid | The token is invalid. |
| 400 | OrganizationUnitIdNotI nScopes | organizationUnitId : ou wovwffm62xifdzie _ m7an7xxxxx not in provisioning scope! | The organization is not synchronized. |
| 404 | application not found _ _ | Application id not found: app mkv7rgt4d7i4u7z _ qtzev2mxxxx | The application is not found. |
| 403 | application disabled _ | Application is disabled | The application is disabled. |
| 403 | application api disable _ _ d | Application api invoke disabled | The application API is not available. |
| 403 | permission denied _ | Require scopes: [urn:alibaba:idaas:sco pe:organizational unit: _ read all] _ | The API authorization information is not specified. |
| 500 | Internal Server Error | Internal Server Error | An internal server error occurred. |

##### DeleteOrganizationalUnit

Deletes an organization. Debug

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request syntax**

DELETE /v2/{instanceId}/{applicationId}/organizationalUnits/{organizationalUnitId} HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The credential. The value is in the Bearer ${access token} format. _ Example: Bearer ATxxxx. | Bearer AT8csE2seYxxxxxij |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| organizationalUni tId | string | Yes | The organization ID. | ou wovwffm62xifdzie _ m7an7xxxxx |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|

This operation does not return any operation-specific parameters.

**Examples**

Sample success responses `JSON` format `{}`

**Error codes**

For a list of error codes, see Service error codes.

**Change history**

| Time | Description | Operation |
|---|---|---|
| 2023-10-24 | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details |

**Error codes**

| HttpCode | Error Code | Error message | Description |
|---|---|---|---|
| 400 | invalid token _ | Access token is not valid | The token is invalid. |
| 400 | OrganizationUnitIdNotI nScopes | organizationUnitId : ou wovwffm62xifdzie _ m7an7xxxxx not in provisioning scope! | The organization is not synchronized or not found. |
| 404 | application not found _ _ | Application id not found: app mkv7rgt4d7i4u7z _ qtzev2mxxxx | The application is not found. |
| 403 | application disabled _ | Application is disabled | The application is disabled. |
| 403 | application api disable _ _ d | Application api invoke disabled | The application API is not available. |
| 403 | permission denied _ | Require scopes: [urn:alibaba:idaas:sco pe:organizational unit: _ manage all] _ | The API authorization information is not specified. |
| 500 | Internal Server Error | Internal Server Error | An internal server error occurred. |

##### ListOrganizationalUnits

Queries a list of organizations in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM) by page.

**Usage notes**

If you need to query child organizations in a root organization, set the following request parameter: "parentOrganizationalUnitId": "ou_root"

| Debug Debugging | Debug |
|---|---|
| > Document Version: 20260831 41 |   |

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request syntax**

GET /v2/{instanceId}/{applicationId}/organizationalUnits HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The credential. The value is in the Bearer ${access token} format. _ Example: Bearer ATxxxx. | Bearer AT8csE2seYxxxxxij |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| parentId | string | Yes | The ID of the parent organization. | ou wovwffm62xifdzie _ m7an7xxxxx |
| pageNumber | integer | No | The page number. Default value: 1. | 1 |
| pageSize | integer | No | The number of entries per page. Default value: 20. Valid values: 1 to 100. | 20 |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|
|   | object | The response parameters. |   |
| totalCount | long | The total number of entries returned. | 1000 |
| data | array<object> | The data objects returned. |   |
| data | object | The data object returned. |   |

| DaaS |   | Developer G | uide·API Referenc |
|---|---|---|---|
| Parameter | Type | Description | Example idaas ue2jvisn _ |
| instanceId | string | The instance ID. | 35ea5lmthk26 7xxxxx |
| organizationalUnitId | string | The organization ID. | ou wovwffm62 _ xifdziem7an7x xxxx |
| organizationalUnitName | string | The organization name. | name001 |
| parentId | string | The ID of the parent organization. | ou wovwffm62 _ xifdziem7an7x xxxx |
| organizationalUnitExternalId | string | The external ID of the organization. The external ID can be used to map external data to the data of the organization in Identity as a Service (IDaaS). By default, the external ID is the organization ID. Note: For organizations with the same source type and source ID, each organization has a unique external ID. | ou wovwffm62 _ xifdziem7an7x xxxx |
| organizationalUnitSourceType | string | The source type of the organization. Valid values: build in: The _ organization was created in IDaaS. ding talk: The _ organization was imported from DingTalk. ad: The organization was imported from Microsoft Active Directory (AD). ldap: The organization was imported from a Lightweight Directory Access Protocol (LDAP) service. | build in _ |

|   | Parameter | Type | The source ID of the Description organization. | Example |   |
|---|---|---|---|---|---|
|   | organizationalUnitSourceId | string | If the organization was created in IDaaS, its source ID is the ID of the IDaaS instance. If the organization was imported, its source ID is the enterprise ID in the source. For example, if the organization was imported from DingTalk, its source ID is the corpId value of the enterprise in DingTalk. | idaas ue2jvisn _ 35ea5lmthk26 7xxxxx |   |
|   | createTime | long | The time when the organization was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. | 165208342592 3 |   |
|   | updateTime | long | The last time when the organization was updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. | 165208342592 3 |   |
|   | description | string | The organization description. | Test organization |   |

**Examples**

Sample success responses `JSON` format

```json
  "totalCount": 1000,
  "data": [
      "instanceId": "idaas_ue2jvisn35ea5lmthk267xxxxx",
      "organizationalUnitId": "ou_wovwffm62xifdziem7an7xxxxx",
      "organizationalUnitName": "name001",
      "parentId": "ou_wovwffm62xifdziem7an7xxxxx",
      "organizationalUnitExternalId": "ou_wovwffm62xifdziem7an7xxxxx",
      "organizationalUnitSourceType": "build_in",
      "organizationalUnitSourceId": "idaas_ue2jvisn35ea5lmthk267xxxxx",
      "createTime": 1652083425923,
      "updateTime": 1652083425923,
      "description": "Test organization"
```

`]`

**Error codes**

For a list of error codes, see Service error codes.

**Change history**

| Time | Description | Operation |
|---|---|---|
| 2023-10-24 | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details |

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | invalid token _ | Access token is not valid | The token is invalid. |
| 400 | OrganizationUnitIdNotI nScopes | organizationUnitId : ou wovwffm62xifdzie _ m7an7xxxxx not in provisioning scope! | The organization is not synchronized. |
| 404 | application not found _ _ | Application id not found: app mkv7rgt4d7i4u7z _ qtzev2mxxxx | The application is not found. |
| 403 | application disabled _ | Application is disabled | The application is disabled. |
| 403 | application api disable _ _ d | Application api invoke disabled | The application API is not available. |
| 403 | permission denied _ | Require scopes: [urn:alibaba:idaas:sco pe:organizational unit: _ read all] _ | The API authorization information is not specified. |

| Developer Guide·API Refe | rence |   | IDaa |
|---|---|---|---|
| HTTP status code | Error code | Error message | Description |

| 500 | Internal Server Error | Internal Server Error | An internal server error occurred. |
|---|---|---|---|

##### ListOrganizationalUnitParentIds

Queries the information of all the parent organizational units of an organizational unit. Debug

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request syntax**

GET /v2/{instanceId}/{applicationId}/organizationalUnits/{organizationalUnitId}/parentIds HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The authentication information. The value is in the Bearer ${access token} _ format. Example: Bearer ATxxxx. | Bearer AT8csE2seYxxxxxij |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| organizationalUni tId | string | Yes | The organization ID. | ou wovwffm62xifdzie _ m7an7xxxxx |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|
|   | object | The response parameters. |   |
| parentIds | array | The IDs of the parent organizational units. The IDs of the organizational units are ordered based on their levels from high to low. Only the IDs of the organizational units within the authorization scope are displayed. |   |
| parentId | string | The organization ID. | ou wovwffm62xifdziem7 _ an7xxxxx |

**Examples**

Sample success responses `JSON` format

```json
  "parentIds": [
    "ou_wovwffm62xifdziem7an7xxxxx"
```

`]`

**Error codes**

For a list of error codes, see Service error codes.

**Change history**

| Updated at | Description | Operation |
|---|---|---|
| 2023-10-24 | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details |

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | invalid token _ | Access token is not valid | The token is invalid. |
| 400 | OrganizationUnitIdNotI nScopes | organizationUnitId : ou wovwffm62xifdzie _ m7an7xxxxx not in provisioning scope! | The organizational unit is not in the provisioning scope. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | application not found _ _ | Application id not found: app mkv7rgt4d7i4u7z _ qtzev2mxxxx | The application is not found. |
| 403 | application disabled _ | Application is disabled | The application is disabled. |
| 403 | application api disable _ _ d | Application api invoke disabled | The application API is not available. |
| 403 | permission denied _ | Require scopes: [urn:alibaba:idaas:sco pe:organizational unit: _ read all] _ | The API authorization information is required. |
| 500 | Internal Server Error | Internal Server Error | An internal server error occurred. |

##### GetOrganizationalUnitIdByExternalId

Obtains the ID of an organization based on the external ID. Debug

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request syntax**

POST /v2/{instanceId}/{applicationId}/organizationalUnits/_/actions/getOrganizationalUnitIdByExternalI d HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The authentication information. The value is in the Bearer ${access token} _ format. Example: Bearer ATxxxx. | Bearer AT8csE2seYxxxxxij |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |

| DaaS |   |   | Develo | per Guide·API Referenc |
|---|---|---|---|---|

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| body | object | No | The request body. |   |
| organizational UnitExternalI d | string | Yes | The external ID of the organization. The external ID can be used to map external data to the data of the organization in Identity-as-a- Service Enterprise Identity Access Management (IDaaS EIAM). By default, the external ID is the organization ID. Note: For organizations with the same source type and source ID, each organization has a unique external ID. | ou wovwffm62xifdzie _ m7an7xxxxx |
| organizational UnitSourceTyp e | string | Yes | The source type of the organization. Valid values: build in: The organization _ was created in IDaaS EIAM. ding talk: The _ organization was imported from DingTalk. ad: The organization was imported from Microsoft Active Directory (AD). ldap: The organization was imported from a Lightweight Directory Access Protocol (LDAP) service. | build in _ |
| organizational UnitSourceId | string | Yes | The source ID of the organization. If the organization was created in IDaaS EIAM, its source ID is the ID of the IDaaS EIAM instance. If the organization was imported, its source ID is the enterprise ID in the source. For example, if the organization was imported from DingTalk, its source ID is the corpId value of the enterprise in DingTalk. | idaas ue2jvisn35ea5l _ mthk267xxxxx |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|
|   | object | OrganizationalUnitIdObject |   |
| organizationalUnitId | string | The organization ID. | ou wovwffm62xifdziem _ 7an7xxxxx |

**Examples**

Sample success responses `JSON` format

```json
  "organizationalUnitId": "ou_wovwffm62xifdziem7an7xxxxx"
```

**Error codes**

For a list of error codes, see Service error codes.

**Change history**

| Change time | Summary of changes | Action |
|---|---|---|
| 2023-10-24 | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details |

#### Account management

##### CreateUser

Creates an Employee Identity and Access Management (EIAM) account in an organization. Debug

**Debugging**

You can run this interface directly in OpenAPI Explorer, saving you the trouble of calculating signatures. After running successfully, OpenAPI Explorer dynamically generates SDK code samples for different programming languages.

**Request syntax**

POST /v2/{instanceId}/{applicationId}/users HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The authentication information. The value is in the Bearer ${access token} _ format. Example: Bearer ATxxxx. | Bearer AT8csE2seYxxxxxij |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| body | object | No | The request body. |   |
| username | string | Yes | The name of the account. The name can be up to 64 characters in length and can contain letters, digits, underscores ( ), periods (.), _ at signs (@), and hyphens (- ). | name001 |
| displayName | string | No | The display name of the account. The display name can be up to 64 characters in length. | display name001 _ |
| password | string | No | The password of the account. For information about the password rules, go to the Create User panel in the Identity as a Service (IDaaS) console. | xxxxx |
| phoneRegion | string | No | The country code of the mobile number. For example, the country code of China is 86 without 00 or +. This parameter is required if a mobile number is specified. | 86 |
| phoneNumbe r | string | No | The mobile phone number of the account. The value must be 6 to 15 digits. | 156xxxxxxx |

| Developer Guide·API Re | ference |   |   | IDaa |
|---|---|---|---|---|

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| phoneNumber Verified | boolean | No | Specifies whether the mobile number is verified. This field is required if a mobile number is specified. If you have no special requirement, set this parameter to true. | true |
| email | string | No | The email address. The prefix of the email address can contain letters, digits, periods (.), underscores ( ), _ and hyphens (-). The email address can be up to 64 characters in length. | example@example.c om |
| emailVerified | boolean | No | Specifies whether the email address is verified. This field is required if an email address is specified. If you have no special requirement, set this parameter to true. | true |
| userExternalI d | string | No | The external ID of the account, which can be used to associate with an external system. The external ID can be up to 64 characters in length. If you do not specify this parameter, the external ID is the account ID. | user d6sbsuumeta4h _ 66ec3il7yxxxx |
| primaryOrgani zationalUnitId | string | Yes | The ID of the primary organization. | ou wovwffm62xifdzie _ m7an7xxxxx |
| description | string | No | The description of the account. The description can be up to 256 characters in length. | Test account |
| passwordInitial izationConfig | object | No | The configuration for password initialization. |   |

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| passwordIni tializationPo licyPriority | string | No | The priority of the password initialization policy. By default, the password initialization feature is disabled and no password initialization policy is used. Valid values: global: The instance-level password initialization policy is used, which means that the password initialization policy that you configured does not take effect. custom: The password initialization policy that you configured is used, including whether to force users to change the password, the password initialization method, and the notification method. | global |
| passwordFo rcedUpdate Status | string | No | Specifies whether to force users to change the password. Default value: disabled. Valid values: enabled: force users to change the password. disabled: do not force users to change the password. | enabled |
| userNotifica tionChannel s | array | No | The password notification methods. Valid values: email sms |   |
| userNotif icationCh annel | string | No | The password notification method. | email |
| passwordIni tializationTy pe | string | No | The password initialization method. Set the value to random. | random |
| customFields | array<ob ject> | No | The extended fields of the account. |   |

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| customFiel d | object | No | The key and value of the extended field. |   |
| fieldNam e | string | No | The key of the extended field. For more information about the type and valid values of the extended field, see the description of the extended field in the IDaaS console. | age |
| fieldValu e | string | No | The value of the extended field. | fieldValue 001 _ |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|
|   | object | The response data. |   |
| userId | string | The account ID. | user d6sbsuumeta4h66 _ ec3il7yxxxx |

**Examples**

Sample responses `JSON` format

```json
  "userId": "user_d6sbsuumeta4h66ec3il7yxxxx"
```

**Error codes**

For a list of error codes, see Service error codes.

**Change history**

| Updated at | Description | Operation |
|---|---|---|
| 2023-10-24 | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details |

**Error codes**

| HttpCode | Error Code | Error message | Description |
|---|---|---|---|
| 400 | invalid token _ | Access token is not valid | The token is invalid. |
| 400 | invalid request _ | Access token application id not match | The request is invalid because the token does not match the application ID. |
| 400 | OrganizationUnitIdNotI nScopes | organizationUnitId : ou wovwffm62xifdzie _ m7an7xxxxx not in provisioning scope! | The organization is not found or is not within the synchronization scope. |
| 404 | instance not found _ _ | Instance id not found: idaas ue2jvisn35ea5l _ mthk267xxxxx | The instance is not found. |
| 404 | application not found _ _ | Application id not found: app mkv7rgt4d7i4u7z _ qtzev2mxxxx | The application is not found. |
| 403 | application disabled _ | Application is disabled | The application is disabled. |
| 403 | application api disable _ _ d | Application api invoke disabled | The application API is not available. |
| 403 | permission denied _ | Require scopes: [urn:alibaba:idaas:sco pe:user:manager all] _ | The API authorization information is required. |
| 400 | MissingParameter.User name | The specified parameter:Username is required! | The username is required. |
| 400 | MissingParameter.Pho neRegion | The specified parameter:PhoneRegio n is required! | phoneRegion is required if a mobile number is specified. |
| 400 | MissingParameter.Pho neNumberVerified | The specified parameter:PhoneRegio n is required! | phoneNumberVerified is required if a mobile number is specified. |
| 400 | MissingParameter.Ema il | The specified parameter:Email is required! | emailVerified is required if an email address is specified. |
| 400 | MissingParameter.User name | The specified parameter:Username is required! | The username is required. |
| 400 | MissingParameter.Prim aryOrganizationalUnitI d | The specified parameter:PrimaryOrg anizationalUnitId is required! | The primary organization is required. |
| 400 | InvalidParameter.Phon eNumber | The specified parameter:PhoneNum ber is invalid. | Invalid mobile number. |

| Developer Guide·API Refe | rence |   | IDaa |
|---|---|---|---|
| HttpCode | Error Code | Error message | Description |
| 400 | InvalidParameter.Phon eRegion | The specified parameter:PhoneRegio n is invalid. | Invalid country code of the mobile number. |
| 400 | InvalidParameter.Pass word | The specified parameter:Password is invalid. | Invalid password. For information about the password rules, go to the Create User panel in the IDaaS console. |
| 400 | InvalidParameter.Emai l | The specified parameter:Email is invalid. | Invalid email address. |
| 400 | InvalidParameter.Displ ayName | The specified parameter:DisplayNa me is invalid. | The display name of the account has exceeded the maximum length. |
| 400 | InvalidParameter.Desc ription | The specified parameter:Description is invalid. | The description of the account has exceeded the maximum length. |
| 500 | Internal Server Error | Internal Server Error | An internal server error occurred. |

##### PatchUser

Modifies an Employee Identity and Access Management (EIAM) account.

**Usage notes**

The operation conforms to the HTTP PATCH request method. The value of a parameter is modified only if the parameter is specified in the request. Debug

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request syntax**

PATCH /v2/{instanceId}/{applicationId}/users/{userId} HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The credential. The value is in the Bearer ${access token} format. _ Example: Bearer ATxxxx. | Bearer AT8csE2seYxxxxxij |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| userId | string | Yes | The account ID. | user d6sbsuumeta4h _ 66ec3il7yxxxx |
| body | object | No | The request body. |   |
| username | string | No | The account name. | name001 |
| displayName | string | No | The display name of the account. | display name001 _ |
| phoneRegion | string | No | The country code of the mobile number. For example, the country code of China is 86 without 00 or +. This parameter is required if a mobile number is specified. | 86 |
| phoneNumbe r | string | No | The mobile number of the account owner. | 156xxxxxxx |
| phoneNumber Verified | boolean | No | Specifies whether the mobile number is verified. This field is required if a mobile number is specified. If you have no special requirement, set this parameter to true. | true |
| email | string | No | The email address of the account owner. | example@example.c om |

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| emailVerified | boolean | No | Specifies whether the email address is verified. This field is required if an email address is specified. If you have no special requirement, set this parameter to true. | true |
| customFields | array<ob ject> | No | The extended fields of the account. |   |
| customFiel d | object | No | The extended field. |   |
| operato r depre cated | string | No | The type of the operation. This parameter is deprecated. Replace it with operation. | replace |
| fieldNam e | string | No | The name of the extended field. For more information about the type and valid values of the extended field, see the detailed description of the extended field in the IDaaS console. | age |
| fieldValu e | string | No | The value of the extended field. | test value _ |
| operatio n | string | No | The operation to be performed on the field. Valid values: add replace If you leave the value of the extended field empty, the replace operation is converted to an add operation. remove | replace |

| depre |   | strin |
|---|---|---|

|   | cated |
|---|---|

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|

This operation does not return any operation-specific parameters.

**Examples**

Sample success responses `JSON` format `{}`

**Error codes**

For a list of error codes, see Service error codes.

**Change history**

| Time | Description | Operation |
|---|---|---|
| 2023-10-24 | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details |
| 2023-04-16 | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details |

**Error codes**

| HttpCode | Error Code | Error message | Description |
|---|---|---|---|
| 400 | invalid token _ | Access token is not valid | The token is invalid. |
| 400 | MissingParameter.xxx x | The specified parameter:xxx is required! | The xxxx parameter is not specified. |
| 400 | InvalidParameter.xxxx | The specified parameter:xxxx is required! | The value of the xxxx parameter is invalid. |
| 404 | ResourceNotFound.Us er | The specified User resource: user d6sbsuumeta4h6 _ 6ec3il7yxxxx not found. | The account is not found. |
| 404 | application not found _ _ | Application id not found: app mkv7rgt4d7i4u7z _ qtzev2mxxxx | The application is not found. |
| 403 | application disabled _ | Application is disabled | The application is disabled. |
| 403 | application api disable _ _ d | Application api invoke disabled | The application API is not available. |
| 403 | permission denied _ | Require scopes: [urn:alibaba:idaas:sco pe:user:manager all] _ | The API authorization information is not specified. |
| 500 | Internal Server Error | Internal Server Error | An internal server error occurred. |

##### GetUser

Queries the details of an Employee Identity and Access Management (EIAM) account. Debug

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request syntax**

GET /v2/{instanceId}/{applicationId}/users/{userId} HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The credential. The value is in the Bearer ${access token} format. _ Example: Bearer ATxxxx. | Bearer AT8csE2seYxxxxxij |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| userId | string | Yes | The account ID. | user d6sbsuumeta4h _ 66ec3il7yxxxx |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|
|   | object | The response parameters. |   |
| instanceId | string | The instance ID. | idaas ue2jvisn35 _ ea5lmthk267xxx xx |
| organizationalUnits | array<object> | The organizations to which the account belongs. |   |
| organizationalUnit | object | The organization. |   |
|   |   |   | ou wovwffm62xif |

|   | organizationalUnitId Parameter | string Type | The organization ID. Description | ou wovwffm62xif _ dEzxieamm7panle7xxxxx |   |
|---|---|---|---|---|---|
|   | organizationalUnitName | string | The organization name. | name001 |   |
|   | primary | boolean | Indicates whether the organization is the primary organization. | true |   |
|   | primaryOrganizationalUnitId | string | The ID of the primary organization of the account. | ou wovwffm62xif _ dziem7an7xxxxx |   |
|   | customFields | array<object> | The extended fields of the account. |   |   |
|   | customField | object | The extended field. |   |   |
|   | fieldName | string | The name of the extended field. | xxxx |   |
|   | fieldValue | string | The value of the extended field. Field values are returned as strings regardless of the data types of the fields. For example, true or false is returned for a Boolean field. | Field value |   |
|   | userId | string | The account ID. | user d6sbsuumet _ a4h66ec3il7yxxx x |   |
|   | username | string | The account name. | name001 |   |
|   | displayName | string | The display name of the account. | display name001 _ |   |
|   | passwordSet | boolean | Indicates whether a password is set. | true |   |
|   | phoneRegion | string | The country code of the mobile number. For example, the country code of China is 86 without 00 or +. | 86 |   |
|   |   |   | The mobile number of |   |   |
|   | > Document Version: 20260831 |   |   | 43 | 3 |

|   |   | The mobile number of |   |
|---|---|---|---|
| phoneNumber Parameter | string Type | tDhee saccrcioputnito onwner. | 156xxxxxxx Example |
| phoneNumberVerified | boolean | Indicates whether the mobile number has been verified. A value of true indicates that the mobile number has been verified by the user or has been set to the verified status by the administrator. A value of false indicates that the mobile number has not been verified. | true |
| email | string | The email address. | example@examp le.com |
| emailVerified | boolean | Indicates whether the email address has been verified. A value of true indicates that the email address has been verified by the user or has been set to the verified status by the administrator. A value of false indicates that the email address has not been verified. | true |
| userExternalId | string | The external ID of the account, which can be used to associate the EIAM account of IDaaS with an external system. By default, the external ID is the account ID. Note: For organizations with the same source type and source ID, each organization has a unique external ID. | user d6sbsuumet _ a4h66ec3il7yxxx x |
| userSourceType | string | The source type of the account. Valid values: build in: The _ organization was created in IDaaS. ding talk: The _ organization was imported from DingTalk. ad: The organization was imported from Microsoft Active Directory (AD). ld Th t | build in _ |
| 34 |   | > Documen | t Version: 2026083 |

|   |   | ldap: The account |   |
|---|---|---|---|
| Parameter | Type | Dewsacsr iimpptoiortned from a Lightweight | Example |
|   |   | Directory Access Protocol (LDAP) service. |   |
| userSourceId | string | The source ID of the account. If the organization was created in IDaaS, its source ID is the ID of the IDaaS instance. If the organization was imported, its source ID is the enterprise ID in the source. For example, if the organization was imported from DingTalk, its source ID is the corpId value of the enterprise in DingTalk. | idaas ue2jvisn35 _ ea5lmthk267xxx xx |
| status | string | The status of the account. Valid values: enabled disabled | enabled |
| accountExpireTime | long | The time when the account expires. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. | 1652085686179 |
| registerTime | long | The time when the account was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. | 1652085686179 |
| lockExpireTime | long | The time when the account lock expires. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. | 1652085686179 |

| Parameter | Type | TDhees tcimriep wtihoenn the account was created. | Example |
|---|---|---|---|
| createTime | long | This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. | 1652085686179 |
| updateTime | long | The last time when the account was modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. | 1652085686179 |
| description | string | The account description. | Test account |
| groups | array<object> | The groups to which the account belongs. |   |
| group | object | The information about the group to which the account belongs. |   |
| groupId | string | The group ID. | group ufdsasn35 _ ea5lmthk267xxx xx |
| groupName | string | The group name. | name test _ |
| description | string | The group description. | description demo _ |

**Examples**

Sample success responses `JSON` format

```json
  "instanceId": "idaas_ue2jvisn35ea5lmthk267xxxxx",
  "organizationalUnits": [
      "organizationalUnitId": "ou_wovwffm62xifdziem7an7xxxxx",
      "organizationalUnitName": "name001",
      "primary": true
```

`],`

```json
  "primaryOrganizationalUnitId": "ou_wovwffm62xifdziem7an7xxxxx",
  "customFields": [
      "fieldName": "xxxx",
      "fieldValue": "Field value"
```

`],`

```json
  "userId": "user_d6sbsuumeta4h66ec3il7yxxxx",
  "username": "name001",
  "displayName": "display_name001",
  "passwordSet": true,
  "phoneRegion": 86,
  "phoneNumber": "156xxxxxxx",
  "phoneNumberVerified": true,
  "email": "example@example.com",
  "emailVerified": true,
  "userExternalId": "user_d6sbsuumeta4h66ec3il7yxxxx",
  "userSourceType": "build_in",
  "userSourceId": "idaas_ue2jvisn35ea5lmthk267xxxxx",
  "status": "enabled",
  "accountExpireTime": 1652085686179,
  "registerTime": 1652085686179,
  "lockExpireTime": 1652085686179,
  "createTime": 1652085686179,
  "updateTime": 1652085686179,
  "description": "Test account",
  "groups": [
      "groupId": "group_ufdsasn35ea5lmthk267xxxxx",
      "groupName": "name_test",
      "description": "description_demo"
```

`]`

**Error codes**

For a list of error codes, see Service error codes.

**Change history**

| Time | Description | Operation |
|---|---|---|

| Time | Description | Operation |
|---|---|---|
| 2023-10-24 | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details |
| 2023-04-16 | The response structure of the operation is modified. | View change details |

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | invalid token _ | Access token is not valid | The token is invalid. |
| 400 | MissingParameter.xxx x | The specified parameter:xxx is required! | The xxxx parameter is not specified. |
| 400 | InvalidParameter.xxxx | The specified parameter:xxxx is required! | The value of the xxxx parameter is invalid. |
| 404 | ResourceNotFound.Us er | The specified User resource: user d6sbsuumeta4h6 _ 6ec3il7yxxxx not found. | The account is not found. |
| 404 | application not found _ _ | Application id not found: app mkv7rgt4d7i4u7z _ qtzev2mxxxx | The application is not found. |
| 403 | application disabled _ | Application is disabled | The application is disabled. |
| 403 | application api disable _ _ d | Application api invoke disabled | The application API is not available. |
| 403 | permission denied _ | Require scopes: [urn:alibaba:idaas:sco pe:user:read all] _ | The API authorization information is not specified. |
| 500 | Internal Server Error | Internal Server Error | An internal server error occurred. |

##### UpdateUserPassword - Update the

**password of an EIAM account**

Updates the password of a specified Enterprise Identity and Access Management (EIAM) account.

**Request syntax**

```
POST /v2/{instanceId}/{applicationId}/users/{userId}/actions/updateUserPassword HTTP/1.
```

**Request parameters**

| Name | Type | Required | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The authentication information. Format: Bearer ${access token} _ . Example: Bearer ATxxxx. | Bearer xxxx |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35 _ ea5lmthk267xxx xx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i _ 4u7zqtzev2mxxx x |
| userId | string | Yes | The account ID. | user d6sbsuumet _ a4h66ec3il7yxxx x |
| body | object | No | The request body. |   |
| password | string | No | The new password. For password rules, see the password policy in the console. | xxxx |

**Response parameters**

| Name | Type | Description | Example |
|---|---|---|---|

This API operation does not return any parameters.

**Examples**

Successful response example `JSON` format `{}`

##### DeleteUser

Deletes an Employee Identity and Access Management (EIAM) account. Debug

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request syntax**

DELETE /v2/{instanceId}/{applicationId}/users/{userId} HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The credential. The value is in the Bearer ${access token} format. _ Example: Bearer ATxxxx. | Bearer AT8csE2seYxxxxxij |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| userId | string | Yes | The account ID. | user d6sbsuumeta4h _ 66ec3il7yxxxx |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|

This operation does not return any operation-specific parameters.

**Examples**

Sample success responses `JSON` format `{}`

**Error codes**

For a list of error codes, see Service error codes.

**Change history**

| Time | Description | Operation |
|---|---|---|
| 2023-10-24 | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details |

**Error codes**

| HttpCode | Error Code | Error message | Description |
|---|---|---|---|
| 400 | invalid token _ | Access token is not valid | The token is invalid. |
| 404 | ResourceNotFound.Us er | The specified User resource: user d6sbsuumeta4h6 _ 6ec3il7yxxxx not found. | The account is not found. |
| 404 | application not found _ _ | Application id not found: app mkv7rgt4d7i4u7z _ qtzev2mxxxx | The application is not found. |
| 403 | application disabled _ | Application is disabled | The application is disabled. |
| 403 | application api disable _ _ d | Application api invoke disabled | The application API is not available. |
| 403 | permission denied _ | Require scopes: [urn:alibaba:idaas:sco pe:user:manager all] _ | The API authorization information is not specified. |
| 500 | Internal Server Error | Internal Server Error | An internal server error occurred. |

##### ListUsers

Queries the information about Employee Identity and Access Management (EIAM) accounts by page. Debug

**Debugging**

You can run this interface directly in OpenAPI Explorer, saving you the trouble of calculating signatures. After running successfully, OpenAPI Explorer dynamically generates SDK code samples for different programming languages.

**Request syntax**

GET /v2/{instanceId}/{applicationId}/users HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The authentication information. The value is in the Bearer ${access token} _ format. Example: Bearer ATxxxx. | Bearer AT8csE2seYxxxxxij |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| organizationalUni tId | string | No | The organization ID. | ou wovwffm62xifdzie _ m7an7xxxxx |
| pageNumber | integer | No | The page number. Default value: 1. | 1 |
| pageSize | integer | No | The number of entries per page. Default value: 20. Valid values: 1 to 100. | 20 |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|
|   | object | The response data. |   |
| totalCount | long | The total number of entries returned. | 1000 |
| data | array<object> | The data objects returned. |   |
| data | object | The data object returned. |   |
| instanceId | string | The instance ID. | idaas ue2jvisn35e _ a5lmthk267xxxxx |
| userId | string | The account ID. | user d6sbsuumet _ a4h66ec3il7yxxxx |
| username | string | The username of the account. | name001 |
| displayName | string | The display name of the | display name001 |

|   |   | p y |   |
|---|---|---|---|
| displayName Parameter | string Type | account. Description | display name001 _ Example |
| passwordSet | boolean | Indicates whether a password is set. | true |
| phoneRegion | string | The country code of the mobile number. For example, the country code of China is 86 without 00 or +. | 86 |
| phoneNumber | string | The mobile number. | 156xxxxxxx |
| phoneNumberVerified | boolean | Indicates whether the mobile number has been verified. A value of true indicates that the mobile number has been verified by the user or has been set to the verified status by the administrator. A value of false indicates that the mobile number has not been verified. | true |
| email | string | The email address. | example@exampl e.com |
| emailVerified | boolean | Indicates whether the email address has been verified. A value of true indicates that the email address has been verified by the user or has been set to the verified status by the administrator. A value of false indicates that the email address has not been verified. | true |
| userExternalId | string | The external ID of the account. The external ID can be used to map external data to the data of the account in EIAM of IDaaS. By default, the external ID is the account ID. Note: For organizations with the same source type and source ID, each organization has a unique external ID. | user d6sbsuumet _ a4h66ec3il7yxxxx |

|   | Parameter | Type | The source type of the Description account. Valid values: | Example |   |
|---|---|---|---|---|---|
|   | userSourceType | string | build in: The account _ was created in IDaaS. ding talk: The _ organization was imported from DingTalk. ad: The organization was imported from Microsoft Active Directory (AD). ldap: The organization was imported from a Lightweight Directory Access Protocol (LDAP) service. | build in _ |   |
|   | userSourceId | string | The source ID of the account. If the organization was created in IDaaS, its source ID is the ID of the IDaaS instance. If the organization was imported, its source ID is the enterprise ID in the source. For example, if the organization was imported from DingTalk, its source ID is the corpId value of the enterprise in DingTalk. | idaas ue2jvisn35e _ a5lmthk267xxxxx |   |
|   | status | string | The status of the account. Valid values: enabled disabled | enabled |   |
|   | accountExpireTime | long | The time when the account expires. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. | 1652085686179 |   |
|   | registerTime | long | The time when the account was registered. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. | 1652085686179 |   |
|   |   |   | The time when the account lock expires. |   |   |
| 4 | 44 |   | > Docume | nt Version: 2026083 | 1 |

| DaaS |   | Develope | r Guide·API Referenc |
|---|---|---|---|
|   |   | p |   |
| Parameter lockExpireTime | Type long | This value is a UNIX Description timestamp representing | Example 1652085686179 |
|   |   | the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. |   |
| createTime | long | The time when the account was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. | 1652085686179 |
| updateTime | long | The time when the account was last modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. | 1652085686179 |
| description | string | The description of the account. | Test account |

**Examples**

Sample responses `JSON` format

```json
  "totalCount": 1000,
  "data": [
      "instanceId": "idaas_ue2jvisn35ea5lmthk267xxxxx",
      "userId": "user_d6sbsuumeta4h66ec3il7yxxxx",
      "username": "name001",
      "displayName": "display_name001",
      "passwordSet": true,
      "phoneRegion": 86,
      "phoneNumber": "156xxxxxxx",
      "phoneNumberVerified": true,
      "email": "example@example.com",
      "emailVerified": true,
      "userExternalId": "user_d6sbsuumeta4h66ec3il7yxxxx",
      "userSourceType": "build_in",
      "userSourceId": "idaas_ue2jvisn35ea5lmthk267xxxxx",
      "status": "enabled",
      "accountExpireTime": 1652085686179,
      "registerTime": 1652085686179,
      "lockExpireTime": 1652085686179,
      "createTime": 1652085686179,
      "updateTime": 1652085686179,
      "description": "Test account"
```

`]`

**Error codes**

For a list of error codes, see Service error codes.

**Change history**

| Updated at | Description | Operation |
|---|---|---|
| 2023-10-24 | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details |

**Error codes**

| HttpCode | Error Code | Error message | Description |
|---|---|---|---|
| 400 | invalid token _ | Access token is not valid | The token is invalid. |
| 404 | application not found _ _ | Application id not found: app 001 _ | The application is not found. |
| 403 | application disabled _ | Application is disabled | The application is disabled. |
| 403 | application api disable _ _ d | Application api invoke disabled | The application API is not available. |

| DaaS |   | Devel | oper Guide·API Referenc |
|---|---|---|---|
| HttpCode | Error Code | Error message | Description |
| 403 | permission denied _ | Require scopes: [urn:alibaba:idaas:sco pe:user:read all] _ | The API authorization information is required. |
| 500 | Internal Server Error | Internal Server Error | An internal server error occurred. |

##### EnableUser

Enables an Employee Identity and Access Management (EIAM) account. Debug

**Debugging**

You can run this interface directly in OpenAPI Explorer, saving you the trouble of calculating signatures. After running successfully, OpenAPI Explorer dynamically generates SDK code samples for different programming languages.

**Request syntax**

POST /v2/{instanceId}/{applicationId}/users/{userId}/actions/enable HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The authentication information. The value is in the Bearer ${access token} _ format. Example: Bearer ATxxxx. | Bearer xxxx |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| userId | string | Yes | The account ID. | user 001 _ |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|

This operation does not return any operation-specific parameters.

**Examples**

Sample responses `JSON` format `{}`

**Error codes**

For a list of error codes, see Service error codes.

**Change history**

| Updated at | Description | Operation |
|---|---|---|
| 2023-10-24 | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details |

**Error codes**

| HttpCode | Error Code | Error message | Description |
|---|---|---|---|
| 400 | invalid token _ | Access token is not valid |   |
| 404 | ResourceNotFound.Us er | The specified User resource: user xxxx _ not found. |   |
| 404 | application not found _ _ | Application id not found: app mkv7rgt4d7i4u7z _ qtzev2mxxxx |   |
| 403 | application disabled _ | Application is disabled |   |
| 403 | application api disable _ _ d | Application api invoke disabled |   |
| 403 | permission denied _ | Require scopes: [urn:alibaba:idaas:sco pe:user:manager all] _ |   |
| 500 | Internal Server Error | Internal Server Error |   |

##### DisableUser

Disables an Enterprise Identity Access Management (EIAM) account.

| Debug Debugging | Debug |
|---|---|
| OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs. |   |

**Request syntax**

POST /v2/{instanceId}/{applicationId}/users/{userId}/actions/disable HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The authentication information. The value is in the Bearer ${access token} _ format. Example: Bearer ATxxxx. | Bearer xxxx |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| userId | string | Yes | The account ID. | user 001 _ |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|

This operation does not return any operation-specific parameters.

**Examples**

Sample success responses `JSON` format `{}`

**Error codes**

For a list of error codes, see Service error codes.

**Change history**

| Updated at | Description | Operation |
|---|---|---|
| 2023-10-24 | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details |

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | invalid token _ | Access token is not valid |   |
| 404 | ResourceNotFound.Us er | The specified User resource: user xxxx _ not found. |   |
| 404 | application not found _ _ | Application id not found: app mkv7rgt4d7i4u7z _ qtzev2mxxxx |   |
| 403 | application disabled _ | Application is disabled |   |
| 403 | application api disable _ _ d | Application api invoke disabled |   |
| 403 | permission denied _ | Require scopes: [urn:alibaba:idaas:sco pe:user:manager all] _ |   |
| 500 | Internal Server Error | Internal Server Error |   |

##### GetUserIdByEmail

Queries the ID of an Employee Identity and Access Management (EIAM) account by email address. Debug

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request syntax**

POST /v2/{instanceId}/{applicationId}/users/_/actions/getUserIdByEmail HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The credential. The value is in the Bearer ${access token} format. _ Example: Bearer ATxxxx. | Bearer AT8csE2seYxxxxxij |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |

| DaaS |   |   | Develo | per Guide·API Referenc |
|---|---|---|---|---|
| Parameter | Type | Requi red | Description | Example |

| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
|---|---|---|---|---|
| body | object | No | The request body. |   |
| email | string | Yes | The email address. | example@example.c om |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|
|   | object | The response parameters. |   |
| userId | string | The account ID. | user d6sbsuumeta4h66 _ ec3il7yxxxx |

**Examples**

Sample success responses `JSON` format

```json
  "userId": "user_d6sbsuumeta4h66ec3il7yxxxx"
```

**Error codes**

For a list of error codes, see Service error codes.

**Change history**

| Time | Description | Operation |
|---|---|---|
| 2023-10-24 | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details |

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | invalid token _ | Access token is not valid | The token is invalid. |

| Developer Guide·API Refe | rence |   | IDaa |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | application not found _ _ | Application id not found: app mkv7rgt4d7i4u7z _ qtzev2mxxxx | The application is not found. |
| 403 | application disabled _ | Application is disabled | The application is disabled. |
| 403 | application api disable _ _ d | Application api invoke disabled | The application API is not available. |
| 403 | permission denied _ | Require scopes: [urn:alibaba:idaas:sco pe:user:manager all] _ | The API authorization information is not specified. |
| 400 | MissingParameter.Ema il | The specified parameter: Email is required! | The email parameter is not specified. |
| 400 | ResourceNotFound.Us erId | The specified UserId resource: %s not found. | The account ID is not found. |
| 500 | Internal Server Error | Internal Server Error | An internal server error occurred. |

##### GetUserIdByPhoneNumber

Queries the ID of an Enterprise Identity Access Management (EIAM) account based on the mobile number. Debug

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request syntax**

POST /v2/{instanceId}/{applicationId}/users/_/actions/getUserIdByPhoneNumber HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The authentication information. The value is in the Bearer ${access token} _ format. Example: Bearer ATxxxx. | Bearer AT8csE2seYxxxxxij |

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| body | object | No | The request body. |   |
| phoneNumbe r | string | Yes | The mobile number. | 156xxxxxxx |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|
|   | object | The response parameters. |   |
| userId | string | The account ID. | user d6sbsuumeta4h66 _ ec3il7yxxxx |

**Examples**

Sample success responses `JSON` format

```json
  "userId": "user_d6sbsuumeta4h66ec3il7yxxxx"
```

**Error codes**

For a list of error codes, see Service error codes.

**Change history**

| Updated at | Description | Operation |
|---|---|---|
| 2023-10-24 | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details |

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | invalid token _ | Access token is not valid | The token is invalid. |

| Developer Guide·API Refe | rence |   | IDaa |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | application not found _ _ | Application id not found: app mkv7rgt4d7i4u7z _ qtzev2mxxxx | The application is not found. |
| 403 | application disabled _ | Application is disabled | The application is disabled. |
| 403 | application api disable _ _ d | Application api invoke disabled | The application API is not available. |
| 403 | permission denied _ | Require scopes: [urn:alibaba:idaas:sco pe:user:manager all] _ | The API authorization information is required. |
| 400 | MissingParameter.Pho neNumber | The specified parameter: PhoneNumber is required! | The email address is required. |
| 400 | ResourceNotFound.Us erId | The specified UserId resource: %s not found. | The account ID is not found. |
| 500 | Internal Server Error | Internal Server Error | An internal server error occurred. |

##### GetUserIdByUserExternalId

Queries the ID of an Employee Identity and Access Management (EIAM) account by external ID. Debug

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request syntax**

POST /v2/{instanceId}/{applicationId}/users/_/actions/getUserIdByExternalId HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The credential. The value is in the Bearer ${access token} format. _ Example: Bearer ATxxxx. | Bearer AT8csE2seYxxxxxij |

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| body | object | No | The request body. |   |
| userExternalI d | string | Yes | The external ID of the account. | xxx001 |
| userSourceTyp e | string | Yes | The source type of the account. Valid values: build in: The organization _ was created in IDaaS. ding talk: The _ organization was imported from DingTalk. ad: The organization was imported from Microsoft Active Directory (AD). ldap: The account was imported from a Lightweight Directory Access Protocol (LDAP) service. | build in _ |
| userSourceId | string | Yes | The source ID of the account. If the account was created in IDaaS, its source ID is the ID of the IDaaS instance. If the account was imported, its source ID is the enterprise ID in the source. For example, if the account was imported from DingTalk, its source ID is the corpId value of the enterprise in DingTalk. | idaas ue2jvisn35ea5l _ mthk267xxxxx |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|
|   | object | The response parameters. |   |
| userId | string | The account ID. | user d6sbsuumeta4h66 _ ec3il7yxxxx |

**Examples**

Sample success responses `JSON` format

```json
  "userId": "user_d6sbsuumeta4h66ec3il7yxxxx"
```

**Error codes**

For a list of error codes, see Service error codes.

**Change history**

| Time | Description | Operation |
|---|---|---|
| 2023-10-24 | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details |

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | invalid token _ | Access token is not valid | The token is invalid. |
| 404 | application not found _ _ | Application id not found: app mkv7rgt4d7i4u7z _ qtzev2mxxxx | The application is not found. |
| 403 | application disabled _ | Application is disabled | The application is disabled. |
| 403 | application api disable _ _ d | Application api invoke disabled | The application API is not available. |
| 403 | permission denied _ | Require scopes: [urn:alibaba:idaas:sco pe:user:manager all] _ | The API authorization information is not specified. |
| 400 | MissingParameter.User ExternalId | The specified parameter: UserExternalId is required! | The userExternalId parameter is not specified. |
| 400 | MissingParameter.User SourceType | The specified parameter: UserSourceType is required! | The userSourceType parameter is not specified. |
| 400 | MissingParameter.User SourceId | The specified parameter: UserSourceId is required! | The userSourceId parameter is not specified. |

| DaaS |   | Devel | oper Guide·API Referenc |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | ResourceNotFound.Us erId | The specified UserId resource: %s not found. | The account ID is not found. |
| 500 | Internal Server Error | Internal Server Error | An internal server error occurred. |

##### GetUserIdByUsername

Queries the ID of an account in Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM) based on the username. Debug

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request syntax**

POST /v2/{instanceId}/{applicationId}/users/_/actions/getUserIdByUsername HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The authentication information. The value is in the Bearer ${access token} _ format. Example: Bearer ATxxxx. | Bearer xxxx |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| body | object | No | The request body. |   |
| username | string | Yes | The account name. | username 001 _ |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|
|   | object | The response data. |   |
| userId | string | The account ID. | user d6sbsuumeta4h66 _ ec3il7yxxxx |

**Examples**

Sample success responses `JSON` format

```json
  "userId": "user_d6sbsuumeta4h66ec3il7yxxxx"
```

**Error codes**

For a list of error codes, see Service error codes.

**Change history**

| Change time | Summary of changes | Action |
|---|---|---|
| 2023-10-24 | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details |

##### SetUserPrimaryOrganizationalUnit - Set

**the primary organization for an EIAM account**

Sets the primary organization for an Enterprise Identity and Access Management (EIAM) account. The account is removed from the old primary organization and added to the new one.

**Request syntax**

```
POST /v2/{instanceId}/{applicationId}/users/{userId}/actions/setUserPrimaryOrganizationalUnit HTTP/1.1
```

**Request parameters**

| Name | Type | Required | Description | Example |
|---|---|---|---|---|

| Authorization | string | Yes | The authentication information. Format: Bearer ${access token} _ . Example: Bearer ATxxxx. | Bearer xxxx |
|---|---|---|---|---|
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35 _ ea5lmthk267xxx xx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i _ 4u7zqtzev2mxxx x |
| userId | string | Yes | The account ID. | user d6sbsuumet _ a4h66ec3il7yxxx x |
| body | object | No | The request body. |   |
| organizationalUni tId | string | Yes | The primary organization ID. | ou wovwffm62xif _ dziem7an7xxxxx |

**Response parameters**

| Name | Type | Description | Example |
|---|---|---|---|

This operation has no response parameters.

**Examples**

Sample success response `JSON` format `{}`

##### AddUserToOrganizationalUnits - Add an

**EIAM account to multiple EIAM organizations**

Adds an EIAM account to one or more organizations. If the account is already a member of a specified organization, no update is performed for that organization.

**Request syntax**

```
POST /v2/{instanceId}/{applicationId}/users/{userId}/actions/addUserToOrganizationalUnits HT TP/1.1
```

**Request parameters**

| Name | Type | Required | Description | Example value |
|---|---|---|---|---|
| Authorization | string | Yes | The authentication information. Format: Bearer ${access token} _ . Example: Bearer ATxxxx. | Bearer xxxx |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35 _ ea5lmthk267xxx xx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i _ 4u7zqtzev2mxxx x |
| userId | string | Yes | The account ID. | user d6sbsuumet _ a4h66ec3il7yxxx x |
| body | object | No | The request body. |   |
| organizationalUni tIds | array | Yes | A list of organization IDs. |   |
| organizationalUni tId | string | No | The organization ID. | ou wovwffm62xif _ dziem7an7xxxxx |

**Response parameters**

| Name | Type | Description | Example value |
|---|---|---|---|

This operation does not return any response parameters.

**Examples**

Sample success response `JSON` format `{}`

##### RemoveUserFromOrganizationalUnits -

**Remove an EIAM account from multiple**

**organizations**

Removes an Entity and Identity Access Management (EIAM) account from multiple organizations. If the account is not a member of the specified organizations, the operation succeeds by default.

**Request syntax**

```
POST /v2/{instanceId}/{applicationId}/users/{userId}/actions/removeUserFromOrganizationalUnits HTTP/1.1
```

**Request parameters**

| Name | Type | Required | Description | Example value |
|---|---|---|---|---|
| Authorization | string | Yes | The authentication information. Format: Bearer ${access token} _ . Example: Bearer ATxxxx. | Bearer xxxx |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35 _ ea5lmthk267xxx xx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i _ 4u7zqtzev2mxxx x |
| userId | string | Yes | The account ID. | user d6sbsuumet _ a4h66ec3il7yxxx x |
| body | object | No | The request body. |   |
| organizationalUni tIds | array | Yes | A list of organization IDs. |   |

| organizationalUni tId | string | No | The organization ID. | ou wovwffm62xif _ dziem7an7xxxxx |
|---|---|---|---|---|

**Response parameters**

| Name | Type | Description | Example value |
|---|---|---|---|

This operation does not return any parameters.

**Examples**

Sample response `JSON` format `{}`

##### ListGroupsForUser - List the groups for

**an EIAM account**

Lists the groups to which an EIAM account belongs.

**Request syntax**

```
GET /v2/{instanceId}/{applicationId}/users/{userId}/actions/listGroupsForUser HTTP/1.1
```

**Request parameters**

| Name | Type | Required | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The authentication information. Format: Bearer ${access token} _ . Example: Bearer ATxxxx. | Bearer xxxx |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35 _ ea5lmthk267xxx xx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i _ 4u7zqtzev2mxxx x |

| userId | string | Yes | The ID of the group. | user d6sbsuumet _ a4h66ec3il7yxxx x |
|---|---|---|---|---|
| nextToken | string | No | nextToken | NTxxx |
| maxResults | integer | No | The number of entries per page. Default value: 20. | 20 |

**Response parameters**

| Name | Type | Description | Example |
|---|---|---|---|
|   | object | DeveloperNextTokenR esponse |   |
| totalCount | long | The total number of records. | 1000 |
| data | array<object> | The response is a data object. |   |
| data | object | Returns a data object. |   |
| instanceId | string | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| groupId | string | Account ID | user d6sbsuumeta4h6 _ 6ec3il7yxxxx |
| groupMemberRelation SourceType | string | The source type of the group membership. | build in _ |
| groupMemberRelation SourceId | string | The source ID of the group membership. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| nextToken | string | The token for the next page of results. If this parameter is empty, all results have been returned. | NTxxx |

| maxResults | long | The maximum number of entries returned per page. | 20 |
|---|---|---|---|

**Examples**

Successful response `JSON` format

```json
  "totalCount": 1000,
  "data": [
      "instanceId": "idaas_ue2jvisn35ea5lmthk267xxxxx",
      "groupId": "user_d6sbsuumeta4h66ec3il7yxxxx",
      "groupMemberRelationSourceType": "build_in",
      "groupMemberRelationSourceId": "idaas_ue2jvisn35ea5lmthk267xxxxx"
```

`],`

```json
  "nextToken": "NTxxx",
  "maxResults": 20
```

#### API operations related to account

**group management**

##### GetGroup

Queries the details of a group. Debug

**Debugging**

You can run this interface directly in OpenAPI Explorer, saving you the trouble of calculating signatures. After running successfully, OpenAPI Explorer dynamically generates SDK code samples for different programming languages.

**Request syntax**

GET /v2/{instanceId}/{applicationId}/groups/{groupId} HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The authentication information. The value is in the Bearer ${access token} _ format. Example: Bearer ATxxxx. | Bearer xxxx |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| groupId | string | Yes | The group ID. | group wovwffm62xif _ dziem7an7xxxxx |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|
|   | object | DeveloperGroupDTO |   |
| instanceId | string | The instance ID. | idaas ue2jvisn35ea5lmt _ hk267xxxxx |
| groupId | string | The group ID. | group ufdsasn35ea5lmt _ hk267xxxxx |
| groupName | string | The group name. | name test _ |
| description | string | The group description. | description demo _ |
| groupExternalId | string | The external ID of the group. | group ufdsasn35ea5lmt _ hk267xxxxx |
| groupSourceType | string | The source type of the group. Valid values: build in (user- _ created), ding talk (imported _ from DingTalk), ad, and ldap (imported from LDAP). | build in _ |
| groupSourceId | string | The source ID of the group. | idaas ue2jvisn35ea5lmt _ hk267xxxxx |
| createTime | long | The time when the group was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. | 1652085686179 |
| updateTime | long | The time when the group was last updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. | 1652085686179 |

**Examples**

Sample responses `JSON` format

```json
  "instanceId": "idaas_ue2jvisn35ea5lmthk267xxxxx",
  "groupId": "group_ufdsasn35ea5lmthk267xxxxx",
  "groupName": "name_test",
  "description": "description_demo",
  "groupExternalId": "group_ufdsasn35ea5lmthk267xxxxx",
  "groupSourceType": "build_in",
  "groupSourceId": "idaas_ue2jvisn35ea5lmthk267xxxxx",
  "createTime": 1652085686179,
  "updateTime": 1652085686179
```

**Error codes**

For a list of error codes, see Service error codes.

##### CreateGroup

Creates a group in Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM). Debug

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request syntax**

POST /v2/{instanceId}/{applicationId}/groups HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The authentication information. The value is in the Bearer ${access token} _ format. Example: Bearer ATxxxx. | Bearer xxxx |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| body | object | No | The request body. |   |
| groupName | string | Yes | The organization name. | name001 |

| Developer Guide·API Re | ference |   |   | IDaa |
|---|---|---|---|---|
| Parameter | Type | Requi red | Description | Example |
| groupExternalI d | string | No | The external ID. | group 2bo6lefcewda _ usyyxxxx |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|
|   | object | GroupIdObject |   |
| groupId | string | The group ID. | group wovwffm62xifdzi _ em7an7xxxxx |

**Examples**

Sample success responses `JSON` format

```json
  "groupId": "group_wovwffm62xifdziem7an7xxxxx"
```

**Error codes**

For a list of error codes, see Service error codes.

##### PatchGroup

Modifies an Employee Identity and Access Management (EIAM) group. Debug

**Debugging**

You can run this interface directly in OpenAPI Explorer, saving you the trouble of calculating signatures. After running successfully, OpenAPI Explorer dynamically generates SDK code samples for different programming languages.

**Request syntax**

PATCH /v2/{instanceId}/{applicationId}/groups/{groupId} HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The authentication information. The value is in the Bearer ${access token} _ format. Example: Bearer ATxxxx. | Bearer xxxx |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| groupId | string | Yes | The group ID. | group xxx001 _ |
| body | object | No | The request body. |   |
| groupName | string | No | The group name. | name001 |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|

This operation does not return any operation-specific parameters.

**Examples**

Sample responses `JSON` format `{}`

**Error codes**

For a list of error codes, see Service error codes.

##### DeleteGroup

Deletes a group. Debug

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request syntax**

DELETE /v2/{instanceId}/{applicationId}/groups/{groupId} HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The authentication information. The value is in the Bearer ${access token} _ format. Example: Bearer ATxxxx. | Bearer xxxx |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| groupId | string | Yes | The group ID. | group wovwffm62xif _ dziem7an7xxxxx |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|

This operation does not return any operation-specific parameters.

**Examples**

Sample success responses `JSON` format `{}`

**Error codes**

For a list of error codes, see Service error codes.

##### ListGroups

Queries the information of Enterprise Identity Access Management (EIAM) groups by page. Debug

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request syntax**

GET /v2/{instanceId}/{applicationId}/groups HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The authentication information. The value is in the Bearer ${access token} _ format. Example: Bearer ATxxxx. | Bearer xxxx |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| groupNameStart With | string | No | The prefix of the group name. | group xxx _ |
| nextToken | string | No | nextToken | NTxxx |
| maxResults | integer | No | The number of entries per page. Default value: 20. | 20 |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|
|   | object | DeveloperNextTokenResponse |   |
| totalCount | long | The total number of entries returned. | 1000 |
| data | array<object> | The returned data. |   |
| data | object | The returned data. |   |
| groupName | string | The group name. | name test _ |
| instanceId | string | The instance ID. | idaas ue2jvisn3 _ 5ea5lmthk267xx xxx |
|   |   | The time when the group was |   |
| > Document Version: 20260831 |   |   | 47 |

|   |   | The time when the group was |   |
|---|---|---|---|
| ParametecrreateTime | lToyngpe | cDreeastcerdi.p Tthieo nvalue is a UNIX timestamp. Unit: milliseconds. | 1E6x5a2m08p5l6e86179 |
| groupId | string | The group ID. | group ufdsasn3 _ 5ea5lmthk267xx xxx |
| groupSourceType | string | The source type of the group. Valid values: build in, _ ding talk, ad, and ldap. _ | build in _ |
| description | string | The description of the group. | description dem _ o |
| groupSourceId | string | The source ID of the group. | idaas ue2jvisn3 _ 5ea5lmthk267xx xxx |
| updateTime | long | The time when the group was last updated. The value is a UNIX timestamp. Unit: milliseconds. | 1652085686179 |
| groupExternalId | string | The external ID of the group. | group ufdsasn3 _ 5ea5lmthk267xx xxx |
| nextToken | string | The start position of the query. If this parameter is left empty, the query starts from the beginning. | NTxxx |
| maxResults | integer | The maximum number of entries returned. | 20 |

**Examples**

Sample success responses `JSON` format

```json
  "totalCount": 1000,
  "data": [
      "groupName": "name_test",
      "instanceId": "idaas_ue2jvisn35ea5lmthk267xxxxx",
      "createTime": 1652085686179,
      "groupId": "group_ufdsasn35ea5lmthk267xxxxx",
      "groupSourceType": "build_in",
      "description": "description_demo",
      "groupSourceId": "idaas_ue2jvisn35ea5lmthk267xxxxx",
      "updateTime": 1652085686179,
      "groupExternalId": "group_ufdsasn35ea5lmthk267xxxxx"
```

`],`

```json
  "nextToken": "NTxxx",
  "maxResults": 20
```

**Error codes**

For a list of error codes, see Service error codes.

##### AddUsersToGroup

Adds multiple Enterprise Identity Access Management (EIAM) accounts to an EIAM group. If the accounts already belong to the specified group, no update is performed. Debug

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request syntax**

POST /v2/{instanceId}/{applicationId}/groups/{groupId}/actions/addUsersToGroup HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The authentication information. The value is in the Bearer ${access token} _ format. Example: Bearer ATxxxx. | Bearer xxxx |

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| groupId | string | Yes | The group ID. | group wovwffm62xif _ dziem7an7xxxxx |
| body | object | No | The request body. |   |
| userIds | array | Yes | The account IDs. |   |
| userId | string | No | The account ID. | user d6sbsuumeta4h _ 66ec3il7yxxxx |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|

This operation does not return any operation-specific parameters.

**Examples**

Sample success responses `JSON` format `{}`

**Error codes**

For a list of error codes, see Service error codes.

##### RemoveUsersFromGroup

Removes multiple Enterprise Identity Access Management (EIAM) accounts from an EIAM group. If the accounts no longer belong to the group, the removal succeeds by default. Debug

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request syntax**

POST /v2/{instanceId}/{applicationId}/groups/{groupId}/actions/removeUsersFromGroup HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The authentication information. The value is in the Bearer ${access token} _ format. Example: Bearer ATxxxx. | Bearer xxxx |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| groupId | string | Yes | The group ID. | group wovwffm62xif _ dziem7an7xxxxx |
| body | object | No | The request body. |   |
| userIds | array | Yes | The account IDs. |   |
| userId | string | No | The account ID. | user d6sbsuumeta4h _ 66ec3il7yxxxx |

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|

This operation does not return any operation-specific parameters.

**Examples**

Sample success responses `JSON` format `{}`

**Error codes**

For a list of error codes, see Service error codes.

##### ListUsersForGroup

Queries accounts in an Employee Identity and Access Management (EIAM) group. Debug

**Debugging**

OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.

**Request syntax**

GET /v2/{instanceId}/{applicationId}/groups/{groupId}/actions/listUsersForGroup HTTP/1.1

**Request parameters**

| Parameter | Type | Requi red | Description | Example |
|---|---|---|---|---|
| Authorization | string | Yes | The credential. The value is in the Bearer ${access token} format. _ Example: Bearer ATxxxx. | Bearer xxxx |
| instanceId | string | Yes | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| applicationId | string | Yes | The application ID. | app mkv7rgt4d7i4u7 _ zqtzev2mxxxx |
| groupId | string | Yes | The group ID. | group wovwffm62xif _ dziem7an7xxxxx |
| nextToken | string | No | nextToken | NTxxx |
| maxResults | integer | No | The number of entries per page. Default value: 20. | 20 |

If you set groupId to iggroup_all, the system queries accounts in all groups.

**Response parameters**

| Parameter | Type | Description | Example |
|---|---|---|---|
|   | object | DeveloperNextTokenResponse |   |
| totalCount | long | The total number of entries returned. | 1000 |
| data | array<object> | The data object returned. |   |
| data | object | The data object returned. |   |
| instanceId | string | The instance ID. | idaas ue2jvisn35ea5l _ mthk267xxxxx |
| userId | string | The account ID. | user 001 _ |
| nextToken | string | A pagination token. If NextToken is empty, no next page exists. | NTxxx |
| maxResults | integer | The maximum number of entries returned. | 20 |

**Examples**

Sample success responses `JSON` format

```json
  "totalCount": 1000,
  "data": [
      "instanceId": "idaas_ue2jvisn35ea5lmthk267xxxxx",
      "userId": "user_001"
```

`],`

```json
  "nextToken": "NTxxx",
  "maxResults": 20
```

**Error codes**

For a list of error codes, see Service error codes. records

## API change records

**Change time: 2023-10-24**

Change set release notes:

| Operation | Summary of changes | Action |
|---|---|---|
| UpdateUserPassword | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details View API document |
| RemoveUserFromOrganizati onalUnits | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details View API document |
| SetUserPrimaryOrganization alUnit | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details View API document |
| GetUserIdByUsername | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details View API document |
| GetOrganizationalUnitIdByE xternalId | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details View API document |
| GetUserIdByUserExternalId | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details View API document |
| GetUserIdByPhoneNumber | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details View API document |
| GetUserIdByEmail | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details View API document |
| ListOrganizationalUnits | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details View API document |
| PatchOrganizationalUnit | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details View API document |
| PatchUser | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details View API document |
| RevokeToken | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details View API document |
| ListUsers | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details View API document |

records

| Operation | Summary of changes | Action |
|---|---|---|
| GetUser | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details View API document |
| GetOrganizationalUnit | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details View API document |
| GetUserInfo | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details View API document |
| ListOrganizationalUnitParen tIds | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details View API document |
| AddUserToOrganizationalUn its | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details View API document |
| DisableUser | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details View API document |
| EnableUser | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details View API document |

**Change time: 2023-10-24**

Change set release notes:

| Operation | Summary of changes | Action |
|---|---|---|
| GenerateToken | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details View API document |

**Change time: 2023-04-16**

Change set release notes:

| Operation | Summary of changes | Action |
|---|---|---|
| PatchUser | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details View API document |
| GetUser | The response structure of the operation is changed. | View change details View API document |

**Change time: 2023-04-04**

Change set release notes:

| Operation | Summary of changes | Action |
|---|---|---|

records

| Operation | Summary of changes | Action |
|---|---|---|
| GenerateToken | The internal configurations of the operation are modified. You can still call the operation as expected. | View change details View API document |

elf-managed applications

## Integrate with self-

**managed applications**

### Connect to IDaaS for SSO

#### Implement SSO for custom applications

This topic describes how to use the Open ID Connect (OIDC) authorization code mode to connect a custom application to the single sign-on (SSO) service of Identity as a Service (IDaaS). This helps developers easily implement SSO for applications, and improves user experience and management efficiency.

**Background information**

IDaaS uses the authorization code mechanism based on the standard OIDC protocol to implement SSO for custom applications of enterprises. Social identity providers (IdPs) such as DingTalk and WeChat use the Open Authorization (OAuth) protocol to implement QR codebased login. The OIDC protocol used by IDaaS is an upgraded version of the OAuth protocol.

**Note**

**Compatibility with OAuth**: The OIDC 1.0 protocol creates a user identity layer on top of
the OAuth2.0 protocol. Therefore, the OIDC protocol is compatible with the OAuth2.0 protocol. The OIDC authorization code mechanism is similar to the OAuth2.0 authorization code mechanism. The difference is that when the OIDC authorization code mechanism is used, the user information endpoint is standardized, and the ID token of a user is returned from the token endpoint.

**How the authorization code mechanism works**

For custom applications, SSO is implemented by using the OIDC authorization code mechanism. Your application only needs to interact with IDaaS at the authorization endpoint and token endpoint to complete the main process of SSO. The login process is fully managed by IDaaS. Your application only needs to parse the login result.

**Connect to SSO**

1. **Create a custom application or an OIDC-based application**
You need to create a custom application or an OIDC-based application in IDaaS and obtain the application keys. If you have obtained the application keys, skip this step. For more information about how to create an application, see **User Guide (Tenant-side) >**
**Applications > Create an application > 3. Custom applications**.
You can obtain **client_id** and **client_secret** by performing the following steps: Click Application in the left-side navigation pane, click the application you want to manage on the Application page, and then click the **General** tab to view the information. This key pair is used in the subsequent API requests. For more information about how to manage or replace the key pair, see **User Guide**
**(Tenant-side) > Applications > Basic settings**.
2. **Send a request to the authorization endpoint**
The following steps need to be performed by the application developer. elf-managed applications When a user attempts to access your application, the application must determine whether a logged-in identity of the user is available. If the user needs to log in to your application, you must send a request to IDaaS for the authorization of the user to access their information. You can click **Application** in the leftside navigation pane, click the application you want to manage on the Application page, click the **Sign-In** tab, and then view the authorization endpoint of the application in the
**Application Settings** section.
As shown in the following example, generate a complete authorization request URL based on the authorization endpoint URL and initiate a 302 redirect in the browser.

```
{{Authorization Endpoint}}?
  client_id=app_***&
  redirect_uri=http%3A%2F%2Flocalhost%3A3000%2F***&
  response_type=code&
  scope=openid&
  state=525f49cc-***
```

| Field | Require d | Example | Description |
|---|---|---|---|
| client id _ | Yes | app michs7r****6pye _ | The client id obtained in the previous step. _ |
| scope | Yes | openid email profile | By default, the value is set to openid email profile for a custom application. This indicates that the application can obtain the ID, username, and email address of the logged-in account. If you use an OIDC-based application, the administrator can also select Phone on the configuration page. For more information about the parameter values that the application is authorized to obtain when a scope is specified, see the "Mappings between the field values accessible to applications and specified scopes" in this topic. |
| response type _ | Yes | code | Set the value to code, which indicates that the authorization code mode is used. |
| redirect _ uri | Yes | http://localhost:3000/ user/oauth2/aliyunida as/callback | The redirect URL of the login result that is returned by IDaaS to the application after the user logs in to the application. This URL is a relay address for the application to receive IDaaS parameters and can receive the authorization code . |

elf-managed applications

| state | No | 525f49cc-87c4-4655- b79c-4c4f971b1ad1 | A random string generated by the application. We recommend that you set a string with more than 32 characters in length. The state value is returned to the application in a subsequent step. The application verifies whether the state value is the same as the initial value that the application sends to the authorization endpoint. This ensures the request comes from the same session to prevent the Cross-Site Request Forgery (XSRF) security vulnerability. This field is optional, but we recommended that you set the field. |
|---|---|---|---|

3. **Log in to the application as a user**
If the request sent to the authorization endpoint is successful, the user is redirected to the IDaaS login page. The user can complete authentication by using a configured login method. IDaaS supports various login methods with different security levels, including login by scanning QR codes with DingTalk and login with a text message verification code. For more information, see
**User Guide (Tenant-side) > Login > General settings**.
When the login is successful, a 302 redirect is initiated to redirect the browser to the specified redirect_uri, which is returned along with the code and state parameters. Sample code:

```
{{redirect_uri}}?
  code=CO***&
  state=525f49cc-***
```

| Field | Example | Description |
|---|---|---|
| code | COE59pkCTm4A9nmowJUsfsfarGEaiSh j3TuDc7NCzLCYu9 | The authorization code. The application uses the authorization code in the access token request sent to IDaaS. |
| state | 525f49cc-87c4-4655-b79c- 4c4f971b1ad1 | Ensure that the state value received by the application is the same as the initial value the application sends to the authorization endpoint. |

4. **Send a request to the token endpoint**
After the application receives the authorization code in the previous step, the application uses the authorization code to send a POST request to the token endpoint. The steps to view the token endpoint are the same as those to view the authorization endpoint. Click **Application** in the left-side navigation pane, click the application you want to manage on the Application page, click the **Sign-In** tab, and then view the token endpoint in the **Application Settings** section. Sample request: elf-managed applications

```
POST /v2/<instance_id>/<app_id>/oauth2/token HTTP/1.0 Host: eiam-api-cn-hangzhou.aliyuncs.com Content-Type: application/x-www-form-urlencoded grant_type=authorization_code
  &code=n0esc3N*****5acc3f0ogp4
  &client_id=s6BhdR*****kqt3
  &client_secret=7Fjfp0ZBr1*****KtDRbnfVdmIw
  &redirect_uri=http%3A%2F%2Fwww.example.com%2Fsso%2Fcallback
```

Sample response:

```json
  "token_type": "Bearer",
  "access_token": "ATM4SoVDqWgUq***********wk3ZS5mtn6fcSp8NH8",
  "expires_in": 1200,
  "expires_at": 1644843164,
  "id_token": "eyJraWQiOiJLRVkyV************gRIadj-frOIRFChA"
```

The user is logged in to the application. You can use one of the following methods to obtain more identity information about the logged-in user and create the application-side login state: i. Use the id_token in the response to obtain the user ID after verification. ii. Use the access_token in the response to send a request to the IDaaS user endpoint to obtain the information of the logged-in user. For more information, see the following section.

**Important**

The scope of user data you can obtain is specified by the scope parameter in the request sent to the authorization endpoint in Step 1.
5. **Parse id_token by using a program**
An `id_token` is a signature token in JSON Web Token (JWT) format that contains the user identity information. The id_token issued by IDaaS contains user data that is visible in plaintext after decryption and the signature. You can copy the complete content of `id_token` to the website JWT decryption website to better understand the content. Sample content: elf-managed applications

```json
  "kid": "KEY2Ty1qL6u21NGKmccv3jwfd2ndmgtQPnag",
  "alg": "RS256"
}.{
  "sub": "user_uyvefotjn7kpbejfmxoos3rtmm",
  "jti": "jwt_aaaac7xyhclac6aqkgtjaxsthw5yotn5d77pmki",
  "iss": "https://pre-eiam-api-cn-hangzhou.aliyun-inc.com/v2/********/oidc",
  "iat": 1644841965,
  "nbf": 1644841965,
  "exp": 1644842265,
  "aud": "app_mhylgo3iairjqjdx5eop6uaf34",
  "at_hash": "XHEaGpMooM9zvQXaMzCNEA",
  "name": "testuser",
  "preferred_username": "testuser",
}.[Signature]
```

Before you use the content to log in to the application, you must verify the signature to ensure that the token is issued by IDaaS, rather than another third-party service. This ensures the security of the login. Login security is mandatory. i. **Obtain the public key for signature verification** Before you verify the signature, you must obtain the endpoint for the public key for signature verification that is openly distributed by IDaaS. You can click **Application** in the left-side navigation pane, click the application you want to manage on the Application page, click the **Sign-In** tab, and then view the endpoint for the public key for signature verification in the **Application Settings** section. The application can access this endpoint to obtain the public key information. You can also open this URL in a browser to view the public key information. Sample code:

```json
  "keys": [
      "kty": "RSA",
      "e": "AQAB",
      "use": "sig",
      "kid": "KEYkYnc55G********CTvT7So44RGDYdbfs",
      "n": "pXmYkIpy1vaNjTMclU86BQjfmDhjlqMAX8ySVvh9gO-nae4ayvG_*********-
v4gP27T7u6bUy0GXTlh3eKE0v1LYB81nfqjF2uazlPwPR5yYOhhWcK-gMNByLfE3CnkDc1YGwA3dZmIz-Zj OCKy8xLaBuqjrvwn5tpMpAoYEEaH4jIm7unTdhbKEKspNR- UXKD8q9RppMh5Tn2sB6oPHlQANudJDgqSwEOevIrdmHU0Zqxrb9cscGH9hH0QjmYEu72yI8BVeliPo3jK6JIo Icj5K_t8BJlFQ9QLJ8_o9tmd3BFv5_LVsh4BKGw"
```

`]` Then, you can use the code to verify the signature and obtain the content of `id_token` . ii. **Verify the signature and log in** You can find the tool in the corresponding language by visiting Libraries for Token Signing/Verification and use the tool in the code to verify signatures and parse

```
 id_token .
```

The following example uses the Java library: org.bitbucket.b_c:jose4j. elf-managed applications Add Maven dependencies:

```xml
<dependency>
  <groupId>org.bitbucket.b_c</groupId>
  <artifactId>jose4j</artifactId>
  <version>0.7.12</version>
</dependency>
```

Sample code:

```java
import org.jose4j.jwk.JsonWebKey; import org.jose4j.jwk.JsonWebKeySet; import org.jose4j.jwt.JwtClaims; import org.jose4j.jwt.consumer.JwtConsumer; import org.jose4j.jwt.consumer.JwtConsumerBuilder; public class IdTokenTest {
    public static void main(String[] args) throws Exception {
        // The issuer identifier (OIDC issuer URL) of EIAM.
        String issuer = "https://eiam-api-cn-
hangzhou.aliyuncs.com/v2/idaas_padyrlux3mphrlsex4uonyqhxu/**********/oidc";
        // The unique identifier of the current application (obtained from EIAM).
        String appId = "app_mkif4*****pxpzbasqmu";
        // Set the public key for parsing id_token in JSON format for JWT signature
verification, as shown in the following code.
        String jwkJson = "{\n" + "  \"keys\": [\n" + "    {\n" + "      \"kty\": \"
RSA\",\n" + " \"e\": \"AQAB\",\n" + " \"use\": \"sig\",\n" + " \"kid\": \"KEY2H82C2at57itnW4onT3p1ySjwH4nirjCk\",\n" + " \"n\": \"w7Jl3fAUJp_9GuxV*****QsOA4lnXR5OD4kF4QbIeBiDiH8_MThrFi9k2MB6YMkSzf5JfIkpAS3JCqZ7k6W ydp4pzaZNZAk3SGzdsa022RmAT" + "-Iayi4Yj6J9tSdTQCjwh2XkzzsIxA_Hla8rWiQ8Vhw1" +
```

`"-`

```
7QArgObfe67nSR7LxD55MFLxk9FU0*****RlGhrQGE_0LUuGWtCJG1r1e6aKquyswfxxAr3Rvj8QGIeJrG0R1 8m8d1_5OdULhB7149VqjM6D98WFjab0U2SNv0UlREZXTcS4p- 2QNm_1egYRRpJEY_00FZqNSYsmErMGepYhO_61KoGqd8cphWQ\"\n" + " }\n" + " ]\n" + "}";
        String jwt =
"eyJraWQiOiJLRVkySDgyQzJhdD*****uaXJqQ2siLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJ1c2Vy*****lm RjZjR3amFrbnBieGpjd3V1IiwianRpIjoiand0X2FhYWFkYWllYTc2eWg1cW0zcm11bnoyeGg0eHd5aTJzZHB jR6aSIsImlzcyI6Imh0dHBzOi8vZWlhbS1hcGktY24taGFuZ3pob3UuYWxpeXVuY3MuY29tL3YyL2lkYWFzX3 ZHlybHV4M21waHJsc2V4NHVvbnlxaHh1L2FwcF9ta2lmNGR3bHBlaDZkbnM0cHhwemJhc3FtdS9vaWRjIiwia 0IjoxNjUzNjMwMDQxLCJuYmYiOjE2NTM2MzAwNDEsImV4cCI6MTY1MzYzMDM0MSwiYXVkIjoiYXBwX21raWY0 dscGVoNmRuczRweHB6YmFzcW11IiwibmFtZSI6InRlc3QiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJ0ZXN0Iiw XBkYXRlZF9hdCI6MTY1MzYyODU5MH0.pAsUNB8OkdpIxJMZRfLJ7Pa31tsJyl44a1jVIlvdQxwOtPULAwrFxn X3eQx89hUGCdvYWl9FO9o-5kT7L-RER0wJYz9YNKqrVNBnaRwINRZyeYLRVurWMMzODQz- V0ULd9raM1M_i2f_SoWFs1gPFtYh_ijUARHISi7Q3q93ZfAuY8Lq2Nq07QunmDbosvioUd5wJG7WCxW5XXZYD e9p5IEYd1MSvnWuTOLbg7rKn0Vm4dNYGWjz1WuoAyCsc_QxOCqpmQ_2czoqPeN- SvPJAQ2CykLk7DSnGpABw1aNrjDidLS9Beqsga9VDCth86sk_0lyTZOaORtUrfVTtQ";
        // Parse the public JSON Web Key Set (JWKS).
        JsonWebKeySet jsonWebKeySet = new JsonWebKeySet(jwkJson);
        // Create a JWT validator.
        JwtConsumer jwtConsumer = createJwtConsumer(jsonWebKeySet, issuer, appId);
        // Perform signature verification and parse the claims.
        JwtClaims jwtClaims = jwtConsumer.processToClaims(jwt);
        // Signature verification is complete. The user information contained in id
token is output.
```

elf-managed applications `_`

```java
        System.out.println(jwtClaims);
    // The method used by the signature verification tool.
    public static JwtConsumer createJwtConsumer(JsonWebKeySet jsonWebKeySet, String
issuer, String appId) {
        // Use the builder pattern to configure the JWT validator.
        final JwtConsumerBuilder jwtConsumerBuilder = new JwtConsumerBuilder();
        // Configure the fields that must be verified.
        jwtConsumerBuilder.setExpectedIssuer(issuer);
        jwtConsumerBuilder.setRequireIssuedAt();
        jwtConsumerBuilder.setRequireExpirationTime();
        jwtConsumerBuilder.setAllowedClockSkewInSeconds(60);
        jwtConsumerBuilder.setExpectedAudience(appId);
        // Set the public key parser, and use kid to match the JSON Web Key (JWK).
        jwtConsumerBuilder.setVerificationKeyResolver((jws, nestingContext) - > {
            // Obtain kid from the JWT header.
            final String signKeyId = jws.getKeyIdHeaderValue();
            // Traverse the JWKS to find the matching key.
            for (JsonWebKey jsonWebKey: jsonWebKeySet.getJsonWebKeys()) {
                if (signKeyId.equals(jsonWebKey.getKeyId())) {
                    return jsonWebKey.getKey();
            throw new RuntimeException("Cannot find verification key: " +
signKeyId);
        });
        // Build a validator instance.
        return jwtConsumerBuilder.build();
```

**Important**

Replace the issuer, appId, jwkJson, and jwt field values in the code with the actual information that is obtained from EIAM. Sample output:

```
JWT Claims Set:{sub=user_dt6kj6yf64cf4wjaknpbxjcwuu,
                jti=jwt_aaaadaiea76yh5qm3rmunz2xh4xwyi2sdph64zi,
                iss=https://eiam-api-cn-
hangzhou.aliyuncs.com/v2/idaas_padyrlux3mphrlsex4uonyqhxu/app_**********/oidc,
                iat=1653630041,
                nbf=1653630041,
                exp=1653630341,
                aud=app_**********,
                name=test,
                preferred_username=test,
                updated_at=1653628590
```

This way, the application obtains the identity information about the logged-in user in IDaaS and uses the information for login. elf-managed applications
6. **Obtain the user information from the UserInfo endpoint**
You can also obtain user information from the UserInfo endpoint. You can click **Application** in the left-side navigation pane, click the application you want to manage on the Application page, click the **Sign-In** tab, and then view the endpoint for the public key for signature verification in the **Application Settings** section. The request for user information complies with the standard RFC6750. Sample request:

```json
GET /v2/<instance_id>/<app_id>/oauth2/userinfo HTTP/1.0 Host: eiam-api-cn-hangzhou.aliyuncs.com Authorization: Bearer <AccessToken> Sample response:
    "sub": "user_dt6kj6yf64cf4wjaknpbxjcwuu",
    "name": "test",
    "preferred_username": "test",
    "updated_at": 1653899948
```

**Note**

The characters returned by the UserInfo endpoint are consistent with the parameters in id_token. This indicates that the parameters configured in extended id_token are also returned from the UserInfo endpoint.

**Advanced settings**

If you have an in-depth understanding of the OIDC protocol, you may use the following concepts or capabilities.
1. **OIDC discovery endpoint**
The `issuer` of an OIDC-based application is the unique identifier of the token issuer (IDaaS). It uses the following format:

```
 https://<idaas-api-domain>/v2/<instance_id>/<application_id>/oidc
```

The following table describes the fields in the angle brackets:

| Field | Description | Example |
|---|---|---|
| idaas-api-domain | The user portal URL. | https://******.aliyunidaas.com |
| instance id _ | The instance ID. | idaas m********r2ed22e6m _ |
| application id _ | The application ID. | app m********jy6rbau _ |

IDaaS supports the OpenID Connect Discovery 1.0 standard. The OIDC discovery endpoint URL of the application is generated by suffixing `/.well-known/openid-configuration` to the

```
 issuer .
```

elf-managed applications You can discover the following endpoint information by sending a request to the discovery endpoint. You can access all request endpoints in the **Application Settings** section.

| Endpoint | Description |
|---|---|
| authorization endpoint _ | The authorization endpoint. |
| device authorization endpoint _ _ | Device mode . Only OIDC-based applications support this feature. Custom applications do not support login with device flow. |
| token endpoint _ | The token endpoint. |
| revocation endpoint _ | The token revocation endpoint. |
| userinfo endpoint _ | The user information endpoint. |
| jwks uri _ | The JWK public key endpoint. |

2. **Mappings between the field values accessible to applications and specified**

**scopes**

The following table lists the user information in id_token for OIDC-based applications when a scope is specified.

| Field | scope | Description |
|---|---|---|
| sub | openid | The userId of the user. |
| jti | openid | The token in JWT format. This is an auxiliary parameter. |
| iss | openid | The issuer of the JWT token. This is an auxiliary parameter. |
| iat | openid | The time when the JWT token was issued. This is an auxiliary parameter. |
| nbf | openid | The start time of the validity period of the JWT token. This is an auxiliary parameter. |
| exp | openid | The expiration time of the JWT token. This is an auxiliary parameter. |

elf-managed applications

| aud | openid | The ClientID of the application. This is an auxiliary parameter. |   |   |
|---|---|---|---|---|
| at hash _ | openid | The hash value of AccessToken. This is an auxiliary parameter. |   |   |
| phone number _ | phone | The mobile number of the user, such as +86 130****5678 . |   |   |
|   |   |   | +86 |   |
| phone number verifie _ _ d | phone | Whether the mobile number is verified. By default, the mobile number is verified. |   |   |
| email | email | The email address of the user, such as al***@example.com . |   |   |
| email verified _ | email | Whether the email address is verified. By default, the email address is verified. |   |   |
| name | profile | The display name of the user. |   |   |
| preferred username _ | profile | The username of the user. |   |   |
| updated at _ | profile | The time when the profile of the user was last updated. |   |   |

|   | 130****5678 |
|---|---|

3. **Authentication methods supported by the token endpoint**
According to the OIDC protocol, IDaaS provides flexibility and supports the following four authentication methods. The field `token_endpoint_auth_methods_supported` returned in the discovery endpoint specifies the supported authentication methods.

| Value | Description |
|---|---|
| none | Used for public clients. If the authentication method is none , grant type cannot be set to client credentials . _ _ |
| client secret basic _ _ | This authentication method is implemented based on RFC 6749 - The OAuth 2.0 Authorization Framework. |
| client secret post _ _ | This authentication method is implemented based on RFC 6749 - The OAuth 2.0 Authorization Framework. |

|   | none |
|---|---|
| client credentials _ |   |

elf-managed applications

| client secret jwt _ _ | This authentication method is implemented based on OpenID Connect Core 1.0. |
|---|---|

After the application receives the authorization code in the previous step and verifies that the request is valid (verifies that the state value is the same as the initial value the application sends to the authorization endpoint when it sends the request), the application uses the authorization code to send a POST request to the token endpoint. The following example shows a request sent to the token endpoint by using the `client_secret_basic` authentication method.

```
POST /token HTTP/1.0 Host: api.aliyunidaas.com Authorization: Basic YXBwX21pY2hzN3I0*******cHllOkNTKioqKioq grant_type=authorization_code& code=COE59pkCTm4J*******arGEaiShj7NCzLCYu9
```

For more information, see the OIDC Core 1.0 specifications.
4. **Client secret rotation for applications**
For more information, see the "Client secret rotation" section in **User Guide (Tenant-**
**side) > Applications > Application management > Basic settings**.

**Relevant standards**

RFC6749 - The OAuth 2.0 Authorization Framework RFC6750 - The OAuth 2.0 Authorization Framework: Bearer Token Usage RFC7009 - OAuth 2.0 Token Revocation RFC7515 - JSON Web Signature (JWS) RFC7517 - JSON Web Key (JWK) RFC7518 - JSON Web Algorithms (JWA) RFC7519 - JSON Web Token (JWT) RFC7636 - Proof Key for Code Exchange by OAuth Public Clients RFC8252 - OAuth 2.0 for Native Apps RFC8628 - OAuth 2.0 Device Authorization Grant OpenID Connect Core 1.0 OpenID Connect Discovery 1.0

#### Connect self-developed Java

**applications that use the Spring Boot**

**framework to IDaaS for SSO**

This topic describes how to connect Java applications that use the Spring Boot framework to Identity as a Service (IDaaS).

**Overview**

elf-managed applications

**Note**

Before you begin, make sure that you have read and understand Connect self-developed applications to IDaaS for SSO. IDaaS uses the OpenID Connect (OIDC) Authorization Code grant type to support connection to self-developed applications. This grant type is backward compatible with the OAuth 2.0 Authorization Code grant type, so you can use the OAuth toolkit `spring-boot-starter-oauth2-` `client` to implement SSO. This toolkit encapsulates all the code for authorization calls and id_token parsing in the OIDC Authorization Code flow.

**Procedure**

**Import the toolkit**

The following example shows how to add the dependency `spring-boot-starter-oauth2-` `client` to the `pom.xml` file:

```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.4.1</version>
</parent> <properties>
    <java.version>8</java.version>
</properties> <dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-oauth2-client</artifactId>
    </dependency>
</dependencies>
```

**Configure IDaaS information**

Configure `client_id` , `client_secret` , and `issuer-uri` in the `application.properties` file.

```
spring.security.oauth2.client.registration.aliyunidaas.client-id=app_*** spring.security.oauth2.client.registration.aliyunidaas.client-secret=CS*** spring.security.oauth2.client.provider.aliyunidaas.issuer-uri=<issuer>
```

The preceding information can be obtained after an application is created. For more information, see Connect self-developed applications to IDaaS for SSO.

**Configure Spring Security to require OAuth authentication**

elf-managed applications

```java
import org.springframework.security.config.annotation.web.builders.HttpSecurity; import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity; import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAda er; @EnableWebSecurity public class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.authorizeRequests()
            .anyRequest().authenticated()
            .and()
            .oauth2Login();
```

**Obtain user information**

The toolkit automatically completes all the authorization calls and id_token verification. You can obtain the user information by injecting `@AuthenticationPrincipal OAuth2User user` :

```java
import org.springframework.security.core.annotation.AuthenticationPrincipal; import org.springframework.security.oauth2.core.user.OAuth2User; import org.springframework.web.bind.annotation.GetMapping; import org.springframework.web.bind.annotation.RestController; @RestController public class SampleController {
    @GetMapping("/user")
    public OAuth2User user(@AuthenticationPrincipal OAuth2User user) {
        return user;
```

You can output user information on the /user endpoint. Use the user information to log the user on to complete the SSO process.

**Configurations when a proxy service is used**

elf-managed applications If you deploy an application such as Server Load Balancer (SLB) or NGINX behind a proxy, the following issue may arise: The user visits https://www.example.com. The `redirect_uri` generated when the user logs on to the application based on OIDC is changed to http://127.0.0.1:8080/oauth2/authorization/aliyunidaas. The login request will fail. To resolve this issue, you must modify the method through which Spring Boot generates the

```
 redirect_uri :
```

1. Add the following configuration item to the Spring Boot configuration file:

```
server.forward-headers-strategy = NATIVE
```

2. If you use SLB, you must select **Use the X-Forwarded-Proto header to retrieve the**
**listener protocol** in the advanced configuration of SLB, as shown in the following figure.
3. If you use an NGINX proxy between SLB and the application, you must configure the
following parameters on the proxy:

```
proxy_set_header Host $host; proxy_set_header X-Forwarded-Proto $proxy_x_forwarded_proto;
```

4. If you directly use an NGINX proxy to provide services over HTTPS, you must configure the
following parameters: elf-managed applications

```
proxy_set_header Host $host; proxy_set_header X-Forwarded-Proto https;
```

**Note**

If you use other proxy services or software, you need to check the configuration. Make sure that the correct HTTP headers `Host` and `X-forwarded-Proto` are specified in the request sent to Spring Boot.

**References**

https://datatracker.ietf.org/doc/html/rfc7239 https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/ https://docs.spring.io/springboot/docs/current/reference/html/howto.html#howto.webserver.use-behind-a-proxy-server

### Connect to IDaaS for account

#### synchronization

#### Overview

This topic provides an overview of the development reference for Alibaba Cloud Identity-as-a- Service Enterprise Identity Access Management (IDaaS EIAM), covering the core features, scenarios, and access guide, to help developers quickly integrate unified identity management and single sign-on (SSO) capabilities.

**Background information**

You can integrate self-developed applications with IDaaS to synchronize IDaaS organizations and accounts to the applications. For more information about how to synchronize application accounts to IDaaS, see API operations for application development. For more information about how to configure application synchronization, see **User Guide**

**(tenant side) > Applications > Application Management > Provisioning >**

**Synchronize IDaaS Account on Application > Callback Events**. This topic describes how
to integrate applications with IDaaS to implement account synchronization.
**Consistency of dependencies:** Related parties may rely on the identity data in your
application for marketing or verification. Therefore, you must promptly synchronize IDaaS account changes. For example, when an employee is onboarded, an account is created in IDaaS. To stay on schedule, an account must be created in the HR application at the same time. In this case, you can subscribe to the **Create account** event.
**Real-time requirements:** Your application must promptly respond to user operations. For
example, after a user logs in to the system and changes their mobile number, the mobile number of the user must be updated in your application by using the **Update account** event.

**Event callback mechanism**

The preceding examples are two simple scenarios. Based on different requirements, developers can subscribe to various events to process data accordingly. IDaaS provides a convenient and secure method to synchronize IDaaS changes to applications. You can quickly integrate applications with IDaaS to allow the applications to receive synchronization requests. elf-managed applications This method is implemented by using an event callback mechanism. In IDaaS, you can configure an event that you want to follow (such as the Create account event). When the event occurs, a synchronization request is automatically sent to the event subscriber by using `HTTP POST` . The event mechanism consists of the following two parts:
**Subscribe to events:** Log in to the IDaaS console and configure the IDaaS events that you
want to follow.
**Receive the event callback:** The developer must integrate the application with IDaaS to
implement account synchronization as required.

**Subscribe to events**

After you create an application in IDaaS, click **Provisioning** to configure account synchronization. For more information, see **User Guide (tenant side) > Applications > Application**
**Management > Synchronize IDaaS accounts to an application by using SCIM**.
You can subscribe the application to one or more events. The following figure shows the events that you can follow. When a selected event occurs, IDaaS sends a request to the application.

**Receive the event callback**

When a selected event occurs, IDaaS sends a `POST` request to the configured **URL for**
**receiving synchronization requests**.
The following code provides an example on how to configure request parameters:

```json
Content-Type: application/json;charset=utf-8 // An example of the body of a POST request from IDaaS. After the application obtains t he parameters, it verifies the signature. "event":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4 G9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
```

All the parameters are passed in the `event` field in the JSON Web Token (JWT) format, which contains the signature. For more information, see RFC 7515: JSON Web Signature (JWS).

**Event format**

You must use the universal open source tools for various languages to parse the JWT information. For testing purposes, you can also paste the value in the JWT format in the field at https://jwt.io/ to view the content. The `event` value consists of two parts: `header` and `payload` . Sample `header` : elf-managed applications

```json
    "kid": "KEYH1zR7XLCGcHw1hzhkCqVjnuyaAJUf6yMR",
    "typ": "JWT",
    "alg": "RS256"
```

Sample `payload` :

```json
  "iss":"urn:alibaba:idaas:app:event",
  "sub":"idaas-121313",
  "aud":"app_12131313",
  "exp":1640966400,
  "iat":1640966400,
  "jti": "cNetm9OD5bXqfVfdvqGMYw",
  "dataEncrypted":false,
  "cipherData":"",
  "plainData":{
    "aliUid":1231313,  // The ID of the Alibaba Cloud account.
    "instanceId":"instance ID",  // The ID of the instance.
    "eventVersion":"V1.0",  // The version number of the event.
    "eventData":[
        "eventId":"",     // The ID of the event.
        "eventType":"",   // The type of the event.
        "eventTime":121313,  // The time when the event occurred.
        "bizId":"business ID",  // The ID of the business. If the business is an
organization, the value is the ID of the organization.
        "bizData":{}       // The specific data details. This field value varies with
event types. For more information, see Address book events.
```

`]` The following table describes the fields contained.

|   | Paramete r | Position | Type | Description |
|---|---|---|---|---|
| header | alg | header | String | Fixed value: RS256. The SHA-256 RSA signature that is used. |

elf-managed applications

|   | kid | header | String | The ID of the public and private key pair issued by IDaaS. The public key of the kid is used for signature verification. In IDaaS, public and private key pairs can be rotated for synchronization. The synchronized public and private key pairs remain unchanged. |
|---|---|---|---|---|
| payload | iss | payload | String | Fixed value: urn:alibaba:idaas:app:event . Indicates that the event notification is initiated by IDaaS. |
|   | sub | payload | String | The ID of the IDaaS instance. |
|   | aud | payload | String | The ID of the IDaaS application. |
|   | exp | payload | Long | The expiration time of the event . Unit: milliseconds. The default value is 30 minutes after the creation time. If the current time is later than the expiration time, an error occurs when the request is parsed, and the application determines that the event is expired. |
|   | iat | payload | Long | The creation time of the event . Unit: milliseconds. If the current time is earlier than the creation time, an error occurs when the request is parsed, and the application determines that the event is invalid. |
|   | data encry _ pted | payload | Boolean | Indicates whether the event data is encrypted for transmission. |
|   | cipher dat _ a | payload | String | If encryption is enabled, this field is not empty. This field is the encrypted ciphertext of the event data. You must decrypt it to view the content. |
|   | plain data _ | payload | Object | If encryption is disabled, this field is not empty. This field contains all the event data. |

**Signature verification**

The JWT signature must be verified to confirm that the `event` information is issued by IDaaS. Signature verification prevents request forgery. elf-managed applications On the synchronization page, you can obtain the **public key endpoint** to verify the JWT signature and the source of the event sent to the application. We recommend that you use the open source JWT toolkit of the programming language.

**Data decryption (optional)**

The encrypted transmission of event synchronization data is supported. The encrypted fields are passed in the `cipher_data` field in `payload` .

```json
    ...
    "cipher_data":
"ZePq7ckODWnL54vqZc3kTw0vF7tjvIRZjqqy/gZm9oTEt71WMufD9swlmHzZkniSqyDGQpkmMRLCXz9gzRJ4BY2R LUPQW8ZDPSfmJKEf2m2w6wY1twoRlnHLoFCVhravsvN0afBqmxd3eK5tHd05Ze6MLOXS3fqxqH61dGAm2mwecvAFP KVeg6JXBYUvA2Uu6dmCOP3y938kFdhodD13O05MBIqWghq569wYvVjKMFMcnsZqmGGKXN0vRFhg+SR16sr24b1X/g bNqyMDICB9k3QMe09dOodwNEwvgxbf1v4PbyCRX1P9UO74nDQaWROWZFplE7qP/JMy3pBr0pxW+hJS9u/Zpvj/hvL BTAZkmhAKDKxlrYztqrgJbr4VOUv8mlqxWjDK4I7VZugODJMSwi1HdjXL+wlMzPMOeH8rkDFU+b5VH3dsxg3hZ64U 7exB62QyyeIJpfk0d57xw8UACiSsXadexQYpJPDycVdmJ7FAmIhxbJ8I6w9Kcv9U5sKybUz1YA8tONAw=="
    ...
```

After you enable the feature, you can enter an encryption key or generate an encryption key. Before IDaaS sends an event callback request, IDaaS uses this key to encrypt all the request data before transmission. IDaaS uses the AES-256 algorithm for symmetric encryption and encrypts events in the JSON Web Encryption (JWE) format. The application must use the same key for decryption to obtain the synchronization data. For more information, see Connect Java applications to IDaaS for account synchronization.

**Responses**

The application must return the processing result of the event according to IDaaS specifications. IDaaS records the result and processes the data based on the returned information.

**Successful execution**

If the request is processed, the application must return `eventId` and the result in the following formats.

| Return field | Data type | Description |
|---|---|---|
| successEvents | Array | The synchronization is successful. |
| skippedEvents | Array | The synchronization is skipped. (Example: The application receives a Delete account event, but the user does not exist in the application system.) |
| failedEvents | Array | The synchronization fails. |
| retriedEvents | Array | The synchronization is retried up to five times. |

elf-managed applications

| -eventId | String | The ID of the event in IDaaS. If this field is not sent or an invalid eventId is transmitted, a retry is triggered. |
|---|---|---|
| -eventCode | String | The error code returned. IDaaS records the result for troubleshooting. You can customize eventCode . |
| -eventMessage | String | The error message returned. IDaaS records the cause of the result for troubleshooting. You can customize eventMessage . |

Sample success responses:

```json
    "successEvents": [
            "eventId": "The ID of the event",
            "eventCode": "SUCCESS",
            "eventMessage": "SUCCESS"
```

`],`

```json
    "skippedEvents": [
            "eventId": "The ID of the event",
            "eventCode": "The error code returned",
            "eventMessage": "The error message returned"
```

`],`

```json
    "failedEvents": [
            "eventId": "The ID of the event",
            "eventCode": "The error code returned",
            "eventMessage": "The error message returned"
```

`],`

```json
    "retriedEvents": [
            "eventId": "The ID of the event",
            "eventCode": "The error code returned",
            "eventMessage": "The error message returned"
```

`]` elf-managed applications

|   | Important After the application receives the request, it must respond to the request with the HTTP 200 status code within 10 seconds. Otherwise, IDaaS determines that the synchronization fails and tries to push the event again up to five times at the respective intervals of 1s, 5s, 10s, 10s, and 10s. |   |   |
|---|---|---|---|
|   |   | HTTP |   |
|   | 200 |   |   |

**Failed execution**

If the processing fails, the application must return the `HTTP` 403, 429, or 500 status code. The following parameters are returned if the processing fails.

| Parameter | Data type | Description |
|---|---|---|
| error | String | The error code. |
| error description _ | String | The error message. |

Generally, the following error codes are returned.

| Error code | HTTP status code | Description |
|---|---|---|
| invalid token _ | 403 | The JWS token is invalid. |
| too many request _ _ | 429 | If the business is busy and returns this error code, IDaaS will use throttling policies. |
| internal error _ | 500 | Indicates an internal error. IDaaS automatically retries the synchronization. |

Sample error responses

```json
     "error": "invalid_token",
     "error_description": "The JWS token is invalid."
```

#### Address book events

This topic describes the event callback mechanism of Alibaba Cloud Identity-as-a-Service Enterprise Identity Access Management (IDaaS EIAM), and provides developers with a complete solution for synchronizing address book events of IDaaS to applications. By understanding the classification and processing procedure of event parameters, developers can achieve efficient system integration. elf-managed applications

**Usage notes**

Address book events in IDaaS are classified into the following categories. For more information about how the connection works and the call process, see Overview.
1. **Test events**
After the synchronization configuration of an application is complete, an administrator can click **Test Connectivity** to check whether the configuration is successful. This process triggers a special test event that can be received and processed by the application to ensure correct configuration.
2. **Incremental events**
Incremental events refer to operations that are automatically triggered by address book changes that occur in IDaaS. These events are used to continuously and incrementally synchronize data between IDaaS and third-party applications. By listening to incremental events, the data consistency between IDaaS and third-party applications can be effectively maintained. This is especially suitable for real-time or near-real-time data synchronization requirements.
3. **Full events**
Full events refer to synchronization operations that are manually triggered by an administrator in IDaaS. These events are used to import data from IDaaS to an application at one time. This type of synchronization is typically used for initial integration or in scenarios where all data needs to be updated.

**Events**

| Category | Event | Code |
|---|---|---|
| Test events | Test the connectivity | urn:alibaba:idaas:app:event:common:test |
|   | Create an account | urn:alibaba:idaas:app:event:ud:user:create |
|   | Delete an account | urn:alibaba:idaas:app:event:ud:user:delete |
|   | Update the basic information of an account | urn:alibaba:idaas:app:event:ud:user:update info _ |
|   | Change the password of an account | urn:alibaba:idaas:app:event:ud:user:update pass _ word |
|   | Disable an account | urn:alibaba:idaas:app:event:ud:user:disable |
|   | Enable an account | urn:alibaba:idaas:app:event:ud:user:enable |
|   | Lock an account | urn:alibaba:idaas:app:event:ud:user:lock |
|   | Unlock an account | urn:alibaba:idaas:app:event:ud:user:unlock |

elf-managed applications

| Incremental events for address book |   |   |
|---|---|---|
|   | Move an account | urn:alibaba:idaas:app:event:ud:user:update prim _ ary ou _ |
|   | Create an organization | urn:alibaba:idaas:app:event:ud:organizational un _ it:create |
|   | Delete an organization | urn:alibaba:idaas:app:event:ud:organizational un _ it:delete |
|   | Update an organization | urn:alibaba:idaas:app:event:ud:organizational un _ it:update |
|   | Move an organization | urn:alibaba:idaas:app:event:ud:organizational un _ it:update parent organizational unit _ _ _ |
|   | Create a group | urn:alibaba:idaas:app:event:ud:group:create |
|   | Update the basic information of a group | urn:alibaba:idaas:app:event:ud:group:update |
|   | Delete a group | urn:alibaba:idaas:app:event:ud:group:delete |
|   | Add members to a group | urn:alibaba:idaas:app:event:ud:group:add user _ |
|   | Remove members from a group | urn:alibaba:idaas:app:event:ud:group:remove us _ er |
| Full events for address book | Synchronize all organizations | urn:alibaba:idaas:app:event:ud:organizational un _ it:push |
|   | Synchronize all accounts | urn:alibaba:idaas:app:event:ud:user:push |
|   | Synchronize all groups | urn:alibaba:idaas:app:event:ud:group:push |

IDaaS passes the complete account or organization information for all account and organization events as parameters to the event listener. If the data contains sensitive information, we recommend that you use an HTTPS secure tunnel or enable **service data**
**encryption** during data transmission.

**Test events**

**Test the connectivity**

This event tests the connectivity based on the configuration information and validates the signature verification and encryption capabilities. elf-managed applications This event is a separate event type. Event code: urn:alibaba:idaas:app:event:common:test.

**Note**

This event can be triggered only by performing a test with one click in the IDaaS console. You cannot trigger the event by calling an API operation. The following code shows the `payload` part of a sample request after signature verification:

```json
  "iss": "urn:alibaba:idaas:app:event",
  "sub": "idaas_rhhoqmlnyu3cv7ow657gyvurky",
  "aud": "app_mjavzivahje6zxkbc4i2bierdu",
  "exp": 1648711369,
  "iat": 1648709570,
  "jti": "bNRrCYrqXjqe8B1xweqlZw",
  "dataEncrypted": false,
  "cipherData": "",
  "plainData": {
    "instanceId": "idaas_rhhoqmlnyu3cv7ow657gyvurky",
    "aliUid": 151971404963****,
    "eventVersion": "V1.0",
    "eventData": [
          "eventId":"evnt_aaaac766x2somw2ptotoyk6ag6bmfkt5xpqprpq",
          "eventType":"urn:alibaba:idaas:app:event:common:test",
          "eventTime":"1648709509849",
          "bizId":"evnt_aaaac766x2somw2ptotoyk6ag6bmfkt5xpqprpq",
          "bizData":"{\"bizData\":\"req_xxxxxxxxxxsdfsdfsfd\"}"
```

`]` After the application receives the request, the application must respond to the request and make sure that the value of the `eventId` parameter in `successEvents` is the same as that in the request. Otherwise, the test request fails. elf-managed applications

```json
  "successEvents": [
      "eventId": "evnt_aaaac766x2somw2ptotoyk6ag6bmfkt5xpqprpq",
      "eventCode": "SUCCESS",
      "eventMessage": "SUCCESS"
```

`],`

```json
  "skippedEvents": [
      "eventId": "",
      "eventCode": "",
      "eventMessage": ""
```

`],`

```json
  "failedEvents": [
      "eventId": "",
      "eventCode": "",
      "eventMessage": ""
```

`],`

```json
  "retriedEvents": [
      "eventId": "",
      "eventCode": "",
      "eventMessage": ""
```

`]`

**Incremental events for address book**

**User events**

1. **Create an account**
You can subscribe to this event to create an account for an onboarded employee. Event code: urn:alibaba:idaas:app:event:ud:user:create. Example of parsed `bizData` : elf-managed applications

```json
    "password": "ssGp96",
    "userId": "user_4alcbywzc7jyl23lu2srljsw7i",
    "username": "zhangsan",
    "displayName": "Bob",
    "passwordSet": true,
    "phoneRegion": "",
   "phoneNumber": "155****5620",
    "phoneVerified": false,
    "email":"zh***@163.com",
    "emailVerified": false,
    "userExternalId": "user_4alcbywzc7jyl23lu2srljsw7i",
    "userSourceType": "build_in",
    "userSourceId": "idaas_rhhoqmlnyu3cv7ow657gyvurky",
    "status": "enabled",
    "accountExpireTime": "-1",
    "registerTime": "1648531553621",
    "lockExpireTime": "-1",
    "createTime": "1648531553621",
    "updateTime": "1648531553621",
    "description": "",
    "customFields": [
            "fieldName": "test_custom_field",
            "fieldValue": "test_value"
```

`],`

```json
    "primaryOrganizationalUnitId": "ou_bvluxnp2ef36uupdwob6km34a4",
    "organizationalUnits": [
            "organizationalUnitId": "ou_bvluxnp2ef36uupdwob6km34a4",
            "organizationalUnitName": "R&D department",
            "primary": true
```

`]`

**Parameters**

| Parameter | Field data type | Description |
|---|---|---|
| userId | String | The unique identifier of the user. |
| username | String | The username. |
| displayName | String | The display name of the user, which is typically the username. |
| passwordSet | boolean | Indicates whether a password is set. |

elf-managed applications

| phoneRegion | String | The area code of the mobile number of the user. |
|---|---|---|
| phoneNumber | String | The mobile number. |
| phoneVerified | boolean | Indicates whether the mobile number of the user has been verified. This feature is not available now. |
| email | String | The email address. |
| emailVerified | boolean | Indicates whether the email address of the user has been verified. This feature is not available now. |
| userExternalId | String | The external ID of the user. If the account is created in IDaaS, the value of this parameter is the same as the userId value. If the account is synchronized from an external source, the value is the ID of the user from the external source. For example, if the account is synchronized from DingTalk, the value is the ID of the DingTalk user. |
| userSourceType | String | The source type of the account. If the account is created in IDaaS, the value is "build id". _ |
| userSourceId | String | The source ID of the account. |
| password | String | The password of the account. The value is passed if password synchronization is enabled and the user sets a password. |
| status | String | The status of the account. Valid values: enabled and disabled. |
| accountExpireTime | Long | The time when the account expires. |
| registerTime | Long | The time when the account was registered. |
| lockExpireTime | Long | The time when the lock on the account expires. The account is unlocked upon the lock expiration time. |
| createTime | Long | The time when the account was created. |

elf-managed applications

| updateTime | Long | The time when the information about the account was modified. |
|---|---|---|
| description | String | The description of the account. |
| customFields | List | The extended fields. |
| -fieldName | String | The name of the field. |
| -fieldValue | String | The value of the field. |
| primaryOrganizational UnitId | String | The primary organization to which the account belongs. |
| organizationalUnits | List | The organizations to which the account belongs. |
| -organizationalUnitId | String | The unique identifier of the organization to which the account belongs. |
| - organizationalUnitNa me | String | The name of the organization to which the account belongs. |
| -primary | boolean | Indicates whether the account belongs to a primary organization. Valid values: true: The account belongs to a primary organization. false: The account does not belong to a primary organization. |

2. **Delete an account**
You can subscribe to this event to delete an account from the address book when an employee is offboarded. Event code: urn:alibaba:idaas:app:event:ud:user:delete. For an example of parsed `bizData` , see the "Create an account" section of this topic.
3. **Update the basic information of an account**
You can subscribe to this event to update the basic information of an account, such as a change in the mobile number, email address, or username. This event can synchronize changes to applications at the earliest opportunity. Event code: urn:alibaba:idaas:app:event:ud:user:update_info. For an example of parsed `bizData` , see the "Create an account" section of this topic.
4. **Change the password of an account**
You can subscribe to this event in scenarios where an administrator needs to reset the password of a user or users need to change their own passwords. This event can synchronize the new password to applications. elf-managed applications

**Important**

Note: When you subscribe to this event, you must specify the synchronization scope for the event to take effect. Otherwise, changes are not synchronized to the applications. For more information about how to configure application synchronization, see

**Applications > Application Management > Synchronize accounts - IDaaS**

**event callback**.
Event code: urn:alibaba:idaas:app:event:ud:user:update_password. For an example of parsed `bizData` , see the "Create an account" section of this topic.
5. **Enable an account**
You can subscribe to this event to change the status of an account from disabled to enabled. Event code: urn:alibaba:idaas:app:event:ud:user:enable. For an example of parsed `bizData` , see the "Create an account" section of this topic.
6. **Disable an account**
You can subscribe to this event to change the status of an account from enabled to disabled. Event code: urn:alibaba:idaas:app:event:ud:user:disable. For an example of parsed `bizData` , see the "Create an account" section of this topic.
7. **Lock an account**
You can subscribe to this event to lock an account in scenarios where the account status changes to inactive. For example, the account is locked when the user enters an incorrect password multiple times. Event code: urn:alibaba:idaas:app:event:ud:user:lock. For an example of parsed `bizData` , see the "Create an account" section of this topic.
8. **Unlock an account**
You can subscribe to this event to change the status of an account from locked to normal. Event code: urn:alibaba:idaas:app:event:ud:user:unlock. For an example of parsed `bizData` , see the "Create an account" section of this topic.
9. **Move an account**
You can subscribe to this event to change the primary organization to which an account belongs. Event code: urn:alibaba:idaas:app:event:ud:user:update_primary_ou. For an example of parsed `bizData` , see the "Create an account" section of this topic.

**Organizational unit (OU) events**

1. **Create an organization**
You can subscribe to this event to create an organization. Event code: urn:alibaba:idaas:app:event:ud:organizational_unit:create. Example of parsed `bizData` : elf-managed applications

```json
    "organizationalUnitId": "ou_dqdvxesykpfhig2kvgrzpeoeyu",
    "organizationalUnitName": "Organization department",
    "parentId": "ou_dqdvxesykpdfasdfaseoeyu",
    "organizationalUnitExternalId": "ou_dqdvxesykpfhig2kvgrzpeoeyu",
    "organizationalUnitSourceType": "build_in",
    "organizationalUnitSourceId": "idaas_rhhoqmlnyu3cv7ow657gyvurky",
    "createTime": "1648451475209",
    "updateTime": "1648451475209",
    "description":"Created in IDaaS"
```

**Parameters**

| Parameter | Field data type | Description |
|---|---|---|
| organizationalUnitId | String | The unique identifier of the organization. |
| organizationalUnitNa me | String | The name of the organization. |
| parentId | String | The ID of the parent organization. |
| organizationalUnitExt ernalId | String | The external ID of the organization. The value of this parameter is the organizationalUnitId value if the organization is created in IDaaS. If the organization is synchronized from an external source, the value of this parameter is the ID of the organization from the external source. For example, if the organization is synchronized from DingTalk, the value is the ID of the corresponding DingTalk department. |
| organizationalUnitSou rceType | String | The source type of the organization. |
| organizationalUnitSou rceId | String | The source ID of the organization. |
| createTime | Long | The time when the organization was created. |
| updateTime | Long | The time when the organization was last updated. The value of this parameter is the same as the lastUpdatedTime value. |
| description | String | The description of the organization. |

elf-managed applications
2. **Delete an organization**
You can subscribe to this event to delete an organization. Event code: urn:alibaba:idaas:app:event:ud:organizational_unit:delete. For an example of parsed `bizData` , see the "Create an organization" section of this topic.
3. **Update an organization**
You can subscribe to this event to modify the basic information of an organization, such as the organization name. Event code: urn:alibaba:idaas:app:event:ud:organizational_unit:update. For an example of parsed `bizData` , see the "Create an organization" section of this topic.
4. Move an organization
You can subscribe to this event to update the parent organization of an organization. Event code: urn:alibaba:idaas:app:event:ud:organizational_unit:update_parent_organizational_unit. For an example of parsed `bizData` , see the "Create an organization" section of this topic.

**Group events**

1. **Create a group**
You can subscribe to this event to create a group. Event code: urn:alibaba:idaas:app:event:ud:group:create. Example of parsed `bizData` :

```json
    "groupId": "group_yvx3ugdi3yzaehnsd3uqzb4xha",
    "groupName": "test_2024",
    "groupExternalId": "test_2024"
```

Parameters

| Parameter | Field data type | Description |
|---|---|---|
| groupId | String | The unique identifier of the group. |
| groupName | String | The display name of the group. |
| groupExternalId | String | The external ID of the group. |
| allMembers | List | All members of the group. |
| memberId | String | The unique identifier of the user. |
| memberName | String | The display name of the user. |

elf-managed applications
2. **Update the basic information of a group**
You can subscribe to this event to update the basic information of a group. Event code: urn:alibaba:idaas:app:event:ud:group:update. For an example of parsed `bizData` , see the "Create a group" section of this topic.
3. **Delete a group**
You can subscribe to this event to delete a group. Event code: urn:alibaba:idaas:app:event:ud:group:delete. For an example of parsed `bizData` , see the "Create a group" section of this topic.
4. **Add members to a group**
You can subscribe to this event to add members to a group. Event code: urn:alibaba:idaas:app:event:ud:group:add_user. Example of parsed `bizData` :

```json
    "addedMembers": [
            "memberId": "user_zakg7oeeaftqqff2bzcv7wpqs4",
            "memberName": "Jim"
```

`],`

```json
    "groupId": "group_yvx3ugdi3yzaehnsd3uqzb4xha",
    "groupName": "test_2024_test",
    "groupExternalId": "test_2024"
```

Parameters

| Parameter | Field data type | Description |
|---|---|---|
| groupId | String | The unique identifier of the group. |
| groupName | String | The display name of the group. |
| groupExternalId | String | The external ID of the group. |
| addedMembers | List | The members that you want to add to the group. |
| -memberId | String | The unique identifier of the user. |
| -memberName | String | The display name of the user. |

5. **Remove members from a group**
You can subscribe to this event to remove members from a group. elf-managed applications Event code: urn:alibaba:idaas:app:event:ud:group:remove_user. Example of parsed `bizData` :

```json
    "removedMembers": [
            "memberId": "user_zakg7oeeaftqqff2bzcv7wpqs4",
            "memberName": "Jim"
```

`],`

```json
    "groupId": "group_yvx3ugdi3yzaehnsd3uqzb4xha",
    "groupName": "test_2024_test",
    "groupExternalId": "test_2024"
```

Parameters

| Parameter | Field data type | Description |
|---|---|---|
| groupId | String | The unique identifier of the group. |
| groupName | String | The display name of the group. |
| groupExternalId | String | The external ID of the group. |
| removedMembers | List | The members that you want to remove from the group. |
| -memberId | String | The unique identifier of the user. |
| -memberName | String | The display name of the user. |

**Full events for address book**

**Full synchronization events**

1. **Synchronize all organizations**
Event code: urn:alibaba:idaas:app:event:ud:organizational_unit:push. For an example of parsed `bizData` , see the "Create an organization" section of this topic.
2. **Synchronize all accounts**
Event code: urn:alibaba:idaas:app:event:ud:user:push. For an example of parsed `bizData` , see the "Create an account" section of this topic.
3. **Synchronize all groups**
You can subscribe to this event to synchronize all groups. Event code: urn:alibaba:idaas:app:event:ud:group:push. elf-managed applications Example of parsed `bizData` :

```json
    "allMembers": [
            "memberId": "user_zakg7oeeaftqqff2bzcv7wpqs4",
            "memberName": "Jim"
```

`},`

```json
            "memberId": "user_zakg7oeea1234ff2bzcexample",
            "memberName": "Bob"
```

`],`

```json
    "groupId": "group_yvx3ugdi3yzaehnsd3uqzb4xha",
    "groupName": "test_2024",
    "groupExternalId": "test_2024"
```

Parameters

| Parameter | Field data type | Description |
|---|---|---|
| groupId | String | The unique identifier of the group. |
| groupName | String | The display name of the group. |
| groupExternalId | String | The external ID of the group. |
| allMembers | List | All members of the group. |
| -memberId | String | The unique identifier of the user. |
| -memberName | String | The display name of the user. |

#### Connect Java applications to IDaaS for

**account synchronization**

This topic describes how to connect Java applications to Identity as a Service (IDaaS). For more information about how the connection works and the call process, see Overview. You must complete the following one or two steps to implement account synchronization:

**Signature verification**

**Decryption** (optional)
After the preceding procedure is completed, the application receives the request of this event and handles the request. elf-managed applications
1. . Signature verification**
Obtain the public key endpoint from the synchronization configuration of the application. For more information, see **User Guide (Tenant) > Applications > Application Management**
**> Synchronize IDaaS accounts to an application by using SCIM**.
In this topic, a Java utility class that directly obtains the public key from the public key endpoint is provided. If the programming language that you use requires public key information, you may need to click the public key endpoint URL to obtain the public key, and store the public key in a .pem file locally. The following code provides an example of a public key:

```json
  "keys": [
      "kty": "RSA",
      "e": "AQAB",
      "use": "sig",
      "kid": "KEY3PdQDx97********h83p8husNSC9AKMH",
      "n": "rLUnH5PNeGUZE-
********GGIxyM5O7TDdaG4********D9mV1CjE8hVHBxXM96IcCCH_1xmUZEZRp_MBP6m2XeNWUXanCpeyuIAD2k
aQAqituZdIlT4l3-q9gtccdY-khaE- OfH9qYZhlxFcYj0gVtOvKZFIkuGhME4IQJd_RAWS3OPXxtbGhO2fZYCiuuc8NWub5mcVQnqsy5aJPLwHbVwVUwYNO q97_m2TtPcIVWtw7AOzX8O78UrYnYt_QPrv7uVdJMbHleSOx2A1IXqrAkJWecwFfvTsBTCUOPPDeVRQEHzzwmf3zp KMgHZU1I5pyqi0KJ6BuMHWw"
```

`]` The following example shows how to add dependencies to your Maven project:

```xml
<dependency>
  <groupId>org.bitbucket.b_c</groupId>
  <artifactId>jose4j</artifactId>
  <version>0.7.9</version>
</dependency>
```

The following code is for the utility class that is used to obtain the public key from the IDaaS public key endpoint and verify the signature. You can directly copy and use the code.

```java
import org.apache.commons.codec.binary.StringUtils; import org.jose4j.jwk.JsonWebKey; import org.jose4j.jwk.JsonWebKeySet; import org.jose4j.jwt.consumer.JwtConsumer; import org.jose4j.jwt.consumer.JwtConsumerBuilder; import org.jose4j.lang.JoseException; import java.io.ByteArrayOutputStream; import java.io.IOException; import java.io.InputStream; import java.net.URL;
```

elf-managed applications

```java
import java.net.URLConnection; import java.nio.charset.StandardCharsets; import java.util.concurrent.ConcurrentHashMap; import java.util.concurrent.ConcurrentMap; public class JwtUtil {
    private final static ConcurrentMap<String, JsonWebKeySet> IDAAS_SIGN_JWK_SET_MAP =
new ConcurrentHashMap<>();
    public static JwtConsumer createJwtConsumerFromUrl(String jwkUrl, String appId) {
        try {
            final JsonWebKeySet jsonWebKeySet = getJsonWebKeySetByUrl(jwkUrl);
            return createJwtConsumer(jsonWebKeySet, appId);
        } catch (Exception e) {
            throw new RuntimeException("Fetch JWKs from url failed: " + e.getMessage()
+ ", " + jwkUrl, e);
    public static JwtConsumer createJwtConsumer(JsonWebKeySet jsonWebKeySet, String app
Id) {
        final JwtConsumerBuilder jwtConsumerBuilder = new JwtConsumerBuilder();
        jwtConsumerBuilder.setExpectedIssuer("urn:alibaba:idaas:app:event");
        jwtConsumerBuilder.setRequireExpirationTime();
        jwtConsumerBuilder.setRequireJwtId();
        jwtConsumerBuilder.setRequireIssuedAt();
        jwtConsumerBuilder.setRequireExpirationTime();
        jwtConsumerBuilder.setMaxFutureValidityInMinutes(1);
        jwtConsumerBuilder.setAllowedClockSkewInSeconds(120);
        jwtConsumerBuilder.setExpectedAudience(appId);
        jwtConsumerBuilder.setVerificationKeyResolver((jws, nestingContext) -> {
            final String signKeyId = jws.getKeyIdHeaderValue();
            for (JsonWebKey jsonWebKey : jsonWebKeySet.getJsonWebKeys()) {
                if (StringUtils.equals(jsonWebKey.getKeyId(), signKeyId)) {
                    return jsonWebKey.getKey();
            throw new RuntimeException("Cannot find verification key: " + signKeyId);
        });
        return jwtConsumerBuilder.build();
    synchronized private static JsonWebKeySet getJsonWebKeySetByUrl(String
jwkUrlString) throws IOException, JoseException {
        JsonWebKeySet jsonWebKeySet = IDAAS_SIGN_JWK_SET_MAP.get(jwkUrlString);
        if (jsonWebKeySet == null) {
            jsonWebKeySet = innerGetJsonWebKeySetByUrl(jwkUrlString);
            IDAAS_SIGN_JWK_SET_MAP.put(jwkUrlString, jsonWebKeySet);
        return jsonWebKeySet;
    private static JsonWebKeySet innerGetJsonWebKeySetByUrl(String jwkUrlString) throws
IOException, JoseException { finalURLjkUrl
```

`ne`

```
URL(jkUrlString)
```

elf-managed applications

```
        final URL jwkUrl = new URL(jwkUrlString);
        final URLConnection urlConnection = jwkUrl.openConnection();
        urlConnection.setConnectTimeout(50000);
        urlConnection.setReadTimeout(50000);
        final String jwkSetJson = new String(readAll(urlConnection.getInputStream()), S
tandardCharsets.UTF_8);
        return new JsonWebKeySet(jwkSetJson);
    public static byte[] readAll(InputStream inputStream) throws IOException {
        final byte[] buffer = new byte[1024 * 8];
        final ByteArrayOutputStream baos = new ByteArrayOutputStream();
        for (int len; ((len = inputStream.read(buffer)) != -1); ) {
            baos.write(buffer, 0, len);
        return baos.toByteArray();
```

The following code provides an example for the call:

```
// Public key -> Obtain the public key by accessing the public key endpoint in the synchronization configuration of the application on IDaaS. String publicKey = "{\n"
            + "  \"keys\": [\n"
            + "    {\n"
            + "      \"kty\": \"RSA\",\n"
            + "      \"e\": \"AQAB\",\n"
            + "      \"use\": \"sig\",\n"
            + "      \"kid\": \"KEYHH4yFa1c*******qNo1nJ7nM2FR3595P1\",\n"
            + "      \"n\": \"oy_xxxxxxxxxxxxxxxxxxxxxxx95d1padSEABqIbcTKcnlTaET3WHaR"
            + "-3MvsooeZWluv94GQEp-U2jzM1adgTqBl_7KPjUk0dwrZbob_8pOLX5UQMF7Oo_nH5-H5EyL9
-yGGhFA4oeuA"
            + "-
b73qXShxP7eHs5xTT1kiYEu2NE3rBZdtrRwUiC_h1DvZMtyWFOPwm3dpLiwCcdlgcKvVuSEXyCBj6Gjevn3_G1guV kHlNOVyNn6Ky1iGQJzXctJCEJ5fnBRs4XZZbPNSciYMD2-__cRdbYPtGyyuoEAfouw\"\n"
            + "    }\n"
            + "  ]\n"
            + "}";;
// Application ID -> Find the ID of the application in the application list. String appId = "app_mjavzivahje6zxxxx"; // JwtUtil -> The JwtUtil utility class is provided below. JwtConsumer jwtConsumer = JwtUtil.createJwtConsumer(new JsonWebKeySet(publicKey),appId); // Obtain the payload after the JSON Web Token (JWT) signature is verified. // The value of the event parameter -> The parameter value received by the API operatio
```

`n.`

```
JwtClaims jwtClaims=jwtConsumer.processToClaims ("The value of the event parameter"); // Obtain the specific payload. Map<String, Object> map = jwtClaims.getClaimsMap(); // Process the business based on the specific data.
```

elf-managed applications
2. . Decryption (optional)**

**Data decryption**

If Service Data Encryption is enabled for the application, the event data is encrypted and transmitted in cipher_data. The application must decrypt the value of cipher_data to obtain the event data. You can enter an encryption key or click Generate Key to generate an encryption key. Copy the key and use it during decryption. The following example shows how to add dependencies to your Maven project:

```xml
<dependency>
  <groupId>org.bitbucket.b_c</groupId>
  <artifactId>jose4j</artifactId>
  <version>0.7.9</version>
</dependency> <dependency>
  <groupId>org.bouncycastle</groupId>
  <artifactId>bcprov-jdk15on</artifactId>
  <version>1.70</version>
</dependency>
```

The following code provides an example for the decryption: elf-managed applications

```
public String decrypte(String cipherData,String key) throws JoseException {
    String alg = "AES";
    // Generate KeySpec by using the key.
    SecretKeySpec secretKeySpec = new SecretKeySpec(Hex.decode(key), alg);
    JsonWebKey jsonWebKey = JsonWebKey.Factory.newJwk(secretKeySpec);
    JsonWebEncryption receiverJwe = new JsonWebEncryption();
    // Set the encryption and decryption mechanisms.
    AlgorithmConstraints algConstraints = new
AlgorithmConstraints(AlgorithmConstraints.ConstraintType.PERMIT, new String[]{"dir"});
    receiverJwe.setAlgorithmConstraints(algConstraints);
    AlgorithmConstraints encConstraints = new AlgorithmConstraints(
        AlgorithmConstraints.ConstraintType.PERMIT, new String[]{"A256GCM", "A192GCM",
"A128GCM"});
    receiverJwe.setContentEncryptionAlgorithmConstraints(encConstraints);
    // Specify the key and the ciphertext.
    receiverJwe.setKey(jsonWebKey.getKey());
    receiverJwe.setCompactSerialization(cipherData);
    // Return the decrypted content.
    return new String(receiverJwe.getPlaintextBytes(), StandardCharsets.UTF_8);
```

#### SCIM 2.0 operations supported by EIAM

This topic describes System for Cross-domain Identity Management (SCIM) 2.0 operations that are supported by Employee Identity and Access Management (EIAM). This topic also describes the scope and limits of SCIM 2.0 operations. The operations described in this topic are required only if you want to synchronize data from your self-managed application to EIAM by using SCIM.

**Usage notes**

SCIM 2.0 operations are implemented based on RFC 7642, RFC 7643, and RFC 7644. For more information about the supported schemas, see the SCIM Schemas section of this topic.

**List of SCIM 2.0 operations**

1. You can use one of the following methods to obtain the bearer token:
i. **Static bearer token**: You can specify a static bearer token on the **Synchronize**
**Application to IDaaS** tab of the **Account Synchronization** tab of the application
management page in the Identity as a Service (IDaaS) console. ii. **Access token generated by using Client_Credentials** : You can dynamically obtain an access token by using the OAuth 2.0 Client Credentials authorization method provided by EIAM. In this case, you can use your client ID and client secret to request an access token. For more information, see GenerateToken.
2. The following table describes the SCIM 2.0 operations.

**Important**

elf-managed applications When you call an SCIM 2.0 operation, replace `{BaseUrl}` with the value of **SCIM Base**
**URL** in the application of an EIAM instance and replace `<BearerToken>` with a valid SCIM
bearer token.

| Category | SCIM 2.0 operation | Supported | Description |
|---|---|---|---|
| Discovery Endpoint | /ServiceProviderConfig | Yes | Obtains the features that are supported by EIAM. |
|   | /ResourceTypes | Yes | Obtains the resource types that are supported by EIAM. The details of users and user groups are returned. |
|   | /Schemas | Yes | Obtains the schemas that are supported by EIAM. The schemas of users, enterprise users, and user groups are returned. |
| /Users | POST /Users | Yes | Synchronizes users. |
|   | GET /Users/{id} | Yes | Queries a user by ID. |
|   | GET /Users | Yes | Queries the information about specific users or queries all users. If you do not specify the filter parameter, all users are queried. A maximum of 100 entries can be returned. Pagination is supported. |
|   | PUT /Users/{id} | Yes | Replaces the information about a user. |
|   | PATCH /Users/{id} | Yes | Updates the information about a user. |
|   | DELETE /Users/{id} | Yes | Deletes a user. |
|   | POST /Groups | Yes | Synchronizes a user group. |
|   | GET /Groups/{id} | Yes | Queries a user group and the user information about the user group. |

| DaaS |   |   |   |
|---|---|---|---|
| /Groups |   |   |   |
|   | GET /Groups | Yes | Queries the information about specific user groups or queries all user groups. If you do not specify the filter parameter, all user groups are queried. The user information about the user groups is not returned. A maximum of 100 entries can be returned. Pagination is supported. |
|   | PUT /Groups/{id} | Yes | Replaces the information about a user group. |
|   | PATCH /Groups/{id} | Yes | Updates the information about a user group. |
|   | DELETE /Groups/{id} | Yes | Deletes a user group. |
| /Me | N/A | No | N/A |
| /Bulk | N/A | No | N/A |
| /.Search | N/A | No | N/A |

**Operations and examples**

**Discovery Endpoint**

**/ServiceProviderConfig**

Obtains the features that are supported by EIAM.

**Limits**

No authentication is required.

**Sample request**

```bash
curl {baseUrl}/ServiceProviderConfig --header "Content-type:application/scim+json"
```

**Sample response**

elf-managed applications

```json
    "documentationUri": "",
    "patch": {
        "supported": true
```

`},`

```json
    "bulk": {
        "supported": false,
        "maxOperations": 0,
        "maxPayloadSize": 0
```

`},`

```json
    "filter": {
        "supported": true,
        "maxResults": 100
```

`},`

```json
    "changePassword": {
        "supported": true
```

`},`

```json
    "sort": {
        "supported": false
```

`},`

```json
    "etag": {
        "supported": false
```

`},`

```json
    "authenticationSchemes": [
            "name": "OAuth Bearer Token",
            "description": "Authentication scheme using the OAuth Bearer Token
Standard",
            "specUri": "https://www.rfc-editor.org/info/rfc6750",
            "type": "oauthbearertoken",
            "primary": true
```

`],`

```json
    "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:ServiceProviderConfig"
```

`]`

**/ResourceTypes**

Obtains the resource types that are supported by EIAM. The details of users and user groups are returned.

**Limits**

No authentication is required.

**Sample request**

```bash
curl {baseUrl}/ResourceTypes --header "content-type:application/scim+json"
```

**Sample response**

elf-managed applications

```json
    "startIndex": 1,
    "totalResults": 2,
    "itemsPerPage": 2,
    "Resources": [
            "name": "Group",
            "description": "Group",
            "endpoint": "/Groups",
            "schema": "urn:ietf:params:scim:schemas:core:2.0:Group",
            "id": "Group",
            "meta": {
                "resourceType": "Group",
                "location": "{BaseUrl}/ResourceTypes/Group"
```

`},`

```json
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:ResourceType"
```

`]` `},`

```json
            "name": "User",
            "description": "User Account",
            "endpoint": "/Users",
            "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
            "schemaExtensions": [
                    "schema":
"urn:ietf:params:scim:schemas:extension:enterprise:2.0:User",
                    "required": false
```

`],`

```json
            "id": "User",
            "meta": {
                "resourceType": "User",
                "location": "{BaseUrl}/ResourceTypes/User"
```

`},`

```json
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:ResourceType"
```

`]` `],`

```json
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:ListResponse"
```

`]`

**/Schemas**

Obtains the schemas that are supported by EIAM. The schemas of users and user groups are returned. elf-managed applications

**Limits**

Query by resource type is supported. Only the fields described in the following sample response are supported. No authentication is required.

**Sample request**

```bash
# The schema to request users.
curl {baseUrl}/Schemas --header "content-type:application/scim+json"
# The schema to request users.
curl {baseUrl}/Schemas/urn:ietf:params:scim:schemas:core:2.0:User --header "content-ty pe:application/scim+json"
# The schema to request users.
curl {baseUrl}/Schemas/urn:ietf:params:scim:schemas:core:2.0:Group --header "content-t ype:application/scim+json"
# The schema to request users.
curl {baseUrl}/Schemas/urn:ietf:params:scim:schemas:extension:enterprise:2.0:User --he ader "content-type:application/scim+json"
```

**Sample response**

**Schema to request users**

```json
    "startIndex": 1,
    "totalResults": 3,
    "itemsPerPage": 3,
    "Resources": [
            "name": "User",
            "description": "User Account",
            "attributes": [
                    "name": "userName",
                    "type": "string",
                    "multiValued": false,
                    "description": "Unique identifier for the User typically used by the
user to directly authenticate to the service provider.",
                    "required": true,
                    "caseExact": false,
                    "mutability": "readWrite",
                    "returned": "default",
                    "uniqueness": "server"
```

`},`

```json
                    "name": "displayName",
                    "type": "string",
                    "multiValued": false,
                    "description": "The name of the User, suitable for display to end-us
ers. The name SHOULD be the full name of the User being described if known.",
                    "required": false,
                    "caseExact": false,
                    "mutability": "readWrite",
```

elf-managed applications

```json
                    "returned": "default",
                    "uniqueness": "none"
```

`},`

```json
                    "name": "password",
                    "type": "string",
                    "multiValued": false,
                    "description": "The User's clear text password. This attribute is in
tended to be used as a means to specify an initial password when creating a new User or to reset an existing User's password.",
                    "required": false,
                    "caseExact": false,
                    "mutability": "writeOnly",
                    "returned": "never",
                    "uniqueness": "none"
```

`},`

```json
                    "name": "emails",
                    "type": "complex",
                    "subAttributes": [
                            "name": "value",
                            "type": "string",
                            "multiValued": false,
                            "description": "E-mail addresses for the user. The value\nSH
OULD be canonicalized by the Service Provider, e.g.\nbjensen@example.com instead of bje nsen@EXAMPLE.COM. Canonical Type\nvalues of work, home, and other.",
                            "required": false,
                            "caseExact": false,
                            "mutability": "readWrite",
                            "returned": "default",
                            "uniqueness": "none"
```

`},`

```json
                            "name": "display",
                            "type": "string",
                            "multiValued": false,
                            "description": "A human readable name, primarily used for di
splay purposes.",
                            "required": false,
                            "caseExact": false,
                            "mutability": "readWrite",
                            "returned": "default",
                            "uniqueness": "none"
```

`},`

```json
                            "name": "type",
                            "type": "string",
                            "multiValued": false,
                            "description": "A label indicating the attribute's function;
e.g., 'work' or 'home'.",
                            "required": false,
                            "canonicalValues": [
                                "work",
```

`"h` `"` elf-managed applications

```
                                "home",
                                "other"
```

`],`

```json
                            "caseExact": false,
                            "mutability": "readWrite",
                            "returned": "default",
                            "uniqueness": "none"
```

`},`

```json
                            "name": "primary",
                            "type": "boolean",
                            "multiValued": false,
                            "description": "A Boolean value indicating the 'primary' or
preferred attribute value for this attribute, e.g., the preferred mailing address or pr imary e-mail address. The primary attribute value 'true' MUST appear no more than once.
```

`",`

```json
                            "required": false,
                            "caseExact": true,
                            "mutability": "readWrite",
                            "returned": "default",
                            "uniqueness": "none"
```

`],`

```json
                    "multiValued": true,
                    "description": "E-mail addresses for the user. The value SHOULD be c
anonicalized by the Service Provider, e.g., bjensen@example.com instead of bjensen@EXAMPLE.COM. Canonical Type values of work, home, and other.",
                    "required": false,
                    "caseExact": true,
                    "mutability": "readWrite",
                    "returned": "default",
                    "uniqueness": "server"
```

`},`

```json
                    "name": "phoneNumbers",
                    "type": "complex",
                    "subAttributes": [
                            "name": "value",
                            "type": "string",
                            "multiValued": false,
                            "description": "Phone number of the User",
                            "required": false,
                            "caseExact": false,
                            "mutability": "readWrite",
                            "returned": "default",
                            "uniqueness": "none"
```

`},`

```json
                            "name": "display",
                            "type": "string",
                            "multiValued": false,
                            "description": "A human readable name, primarily used for di
splay purposes.", "required":false
```

elf-managed applications

```json
                            required: false,
                            "caseExact": false,
                            "mutability": "readWrite",
                            "returned": "default",
                            "uniqueness": "none"
```

`},`

```json
                            "name": "type",
                            "type": "string",
                            "multiValued": false,
                            "description": "A label indicating the attribute's function;
e.g., 'work' or 'home' or 'mobile' etc.",
                            "required": false,
                            "canonicalValues": [
                                "work",
                                "home",
                                "mobile",
                                "fax",
                                "pager",
                                "other"
```

`],`

```json
                            "caseExact": false,
                            "mutability": "readWrite",
                            "returned": "default",
                            "uniqueness": "none"
```

`},`

```json
                            "name": "primary",
                            "type": "boolean",
                            "multiValued": false,
                            "description": "A Boolean value indicating the 'primary' or
preferred attribute value for this attribute, e.g., the preferred phone number or prima ry phone number. The primary attribute value 'true' MUST appear no more than once.",
                            "required": false,
                            "caseExact": true,
                            "mutability": "readWrite",
                            "returned": "default",
                            "uniqueness": "none"
```

`],`

```json
                    "multiValued": true,
                    "description": "Phone numbers for the User.  The value SHOULD be can
onicalized by the Service Provider according to format in RFC3966 e.g., 'tel:555xxxx5555'. Canonical Type values of work, home, mobile, fax, pager and other."
```

`,`

```json
                    "required": false,
                    "caseExact": true,
                    "mutability": "readWrite",
                    "returned": "default",
                    "uniqueness": "server"
```

`},`

```json
                    "name": "phoneRegion",
                    "type": "string",
                    "multiValued": false,
```

elf-managed applications `u``t`

```json
aued: ase,
                    "description": "PhoneRegion for the User. eg.86.If not filled, the d
efault value is 86",
                    "required": false,
                    "caseExact": false,
                    "mutability": "writeOnly",
                    "returned": "never",
                    "uniqueness": "none"
```

`},`

```json
                    "name": "id",
                    "type": "string",
                    "multiValued": false,
                    "description": "A unique identifier for a SCIM resource as defined b
y the service provider.",
                    "required": true,
                    "caseExact": false,
                    "mutability": "readOnly",
                    "returned": "always",
                    "uniqueness": "server"
```

`},`

```json
                    "name": "externalId",
                    "type": "string",
                    "multiValued": false,
                    "description": "A String that is an identifier for the resource as d
efined by the provisioning client.",
                    "required": false,
                    "caseExact": false,
                    "mutability": "readWrite",
                    "returned": "default",
                    "uniqueness": "none"
```

`},`

```json
                    "name": "meta",
                    "type": "complex",
                    "subAttributes": [
                            "name": "resourceType",
                            "type": "string",
                            "multiValued": false,
                            "description": "The resource Type",
                            "required": false,
                            "caseExact": true,
                            "mutability": "readOnly",
                            "returned": "always",
                            "uniqueness": "none"
```

`},`

```json
                            "name": "location",
                            "type": "reference",
                            "multiValued": false,
                            "description": "The location (URI) of the resource",
                            "required": false,
                            "caseExact": true,
```

elf-managed applications

```json
                            "mutability": "readOnly",
                            "returned": "always",
                            "uniqueness": "none"
```

`],`

```json
                    "multiValued": false,
                    "description": ".",
                    "required": false,
                    "caseExact": false,
                    "mutability": "readOnly",
                    "returned": "default",
                    "uniqueness": "none"
```

`},`

```json
                    "name": "schemas",
                    "type": "string",
                    "multiValued": true,
                    "description": ".",
                    "required": true,
                    "caseExact": true,
                    "mutability": "readOnly",
                    "returned": "always",
                    "uniqueness": "none"
```

`],`

```json
            "id": "urn:ietf:params:scim:schemas:core:2.0:User",
            "meta": {
                "resourceType": "Schema",
                "location": "
{BaseUrl}/Schemas/urn:ietf:params:scim:schemas:core:2.0:User"
```

`},`

```json
            "name": "Group",
            "description": "Group",
            "attributes": [
                    "name": "displayName",
                    "type": "string",
                    "multiValued": false,
                    "description": "A human-readable name for the Group.",
                    "required": true,
                    "caseExact": false,
                    "mutability": "readWrite",
                    "returned": "default",
                    "uniqueness": "none"
```

`},`

```json
                    "name": "members",
                    "type": "complex",
                    "subAttributes": [
                            "name": "value",
                            "type": "string",
```

elf-managed applications

```json
                            "multiValued": false,
                            "description": "The identifier of a group member.",
                            "required": true,
                            "caseExact": false,
                            "mutability": "immutable",
                            "returned": "default",
                            "uniqueness": "none"
```

`},`

```json
                            "name": "ref",
                            "type": "reference",
                            "multiValued": false,
                            "description": "The URI of the member resource.",
                            "required": true,
                            "caseExact": true,
                            "mutability": "immutable",
                            "returned": "default",
                            "uniqueness": "none",
                            "referenceTypes": [
                                "User"
```

`]` `},`

```json
                            "name": "display",
                            "type": "string",
                            "multiValued": false,
                            "description": "A human readable name, primarily used for di
splay purposes.",
                            "required": false,
                            "caseExact": false,
                            "mutability": "immutable",
                            "returned": "default",
                            "uniqueness": "none"
```

`],`

```json
                    "multiValued": true,
                    "description": "A list of members of the Group.",
                    "required": false,
                    "caseExact": true,
                    "mutability": "readWrite",
                    "returned": "default",
                    "uniqueness": "none"
```

`},`

```json
                    "name": "id",
                    "type": "string",
                    "multiValued": false,
                    "description": "A unique identifier for a SCIM resource as defined b
y the service provider.",
                    "required": true,
                    "caseExact": false,
                    "mutability": "readOnly",
                    "returned": "always",
                    "uniqueness": "server"
```

elf-managed applications `},`

```json
                    "name": "externalId",
                    "type": "string",
                    "multiValued": false,
                    "description": "A String that is an identifier for the resource as d
efined by the provisioning client.",
                    "required": false,
                    "caseExact": false,
                    "mutability": "readWrite",
                    "returned": "default",
                    "uniqueness": "none"
```

`},`

```json
                    "name": "meta",
                    "type": "complex",
                    "subAttributes": [
                            "name": "resourceType",
                            "type": "string",
                            "multiValued": false,
                            "description": "The resource Type",
                            "required": false,
                            "caseExact": true,
                            "mutability": "readOnly",
                            "returned": "always",
                            "uniqueness": "none"
```

`},`

```json
                            "name": "location",
                            "type": "reference",
                            "multiValued": false,
                            "description": "The location (URI) of the resource",
                            "required": false,
                            "caseExact": true,
                            "mutability": "readOnly",
                            "returned": "always",
                            "uniqueness": "none"
```

`],`

```json
                    "multiValued": false,
                    "description": ".",
                    "required": false,
                    "caseExact": false,
                    "mutability": "readOnly",
                    "returned": "default",
                    "uniqueness": "none"
```

`},`

```json
                    "name": "schemas",
                    "type": "string",
                    "multiValued": true,
                    "description": ".",
                    "required": true,
"caseExact":true
```

elf-managed applications

```json
                    "caseExact": true,
                    "mutability": "readOnly",
                    "returned": "always",
                    "uniqueness": "none"
```

`],`

```json
            "id": "urn:ietf:params:scim:schemas:core:2.0:Group",
            "meta": {
                "resourceType": "Schema",
                "location": "
{BaseUrl}/Schemas/urn:ietf:params:scim:schemas:core:2.0:Group"
```

`},`

```json
            "name": "EnterpriseUser",
            "description": "Enterprise User",
            "attributes": [
                    "name": "organization",
                    "type": "string",
                    "multiValued": false,
                    "description": "Identifies the name of an organization.",
                    "required": false,
                    "caseExact": false,
                    "mutability": "readWrite",
                    "returned": "default",
                    "uniqueness": "none"
```

`],`

```json
            "id": "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User",
            "meta": {
                "resourceType": "Schema",
                "location": "
{BaseUrl}/Schemas/urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
```

`],`

```json
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:ListResponse"
```

`]`

**Users**

**POST /Users**

Synchronizes users.

**Limits**

You can use only the fields that are defined in the "/Schemas" section of this topic. elf-managed applications If you specify the organization to which the account belongs, the account is automatically assigned to the organization that you specify. If you do not specify the organization to which the account belongs, the account is assigned to the organization that you use as the synchronization target. For more information, see Sample request.

**Sample request**

```bash
curl {baseUrl}/Users --header 'Authorization: Bearer <BearerToken>' --header "content-t ype:application/scim+json" -X POST -d '<data>'
```

The following sample code provides an example of the data field:

**Example 1: Do not specify the organizational unit to which the account belongs**

```json
    "userName": "<user username>",
    "externalId": "<external Id>",
    "displayName": "<user display name>",
    "active": true,
    "emails": [
            "primary": true,
            "type": "work",
            "value": "<user email>"
```

`],`

```json
   "phoneRegion":"86"
   "phoneNumbers": [
            "primary": true,
            "type": "work",
            "value": "<user phoneNumber>"
```

`],`

```json
    "active":true,
    "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User"
```

`]`

**Example 2: Specify the organizational unit to which the account belongs**

elf-managed applications

```json
    "userName": "<user username>",
    "externalId": "<external Id>",
    "displayName": "<user display name>",
    "emails": [
            "primary": true,
            "type": "work",
            "value": "<user email>"
```

`],`

```json
   "phoneRegion":"86"
   "phoneNumbers": [
            "primary": true,
            "type": "work",
            "value": "<user phoneNumber>"
```

`],`

```json
  "active":true,
  "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User",
        "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
```

`],`

```json
  "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
    "organization": "<user organizationalUnitId>"
```

**Sample response**

elf-managed applications

```json
HTTP/1.1 201
    "id": "<userId>",
    "userName": "<user username>",
    "displayName": "<user display name>",
    "active": true,
    "emails": [
            "value": "<user email>",
            "type": "work",
            "primary": true
```

`],`

```json
    "phoneNumbers": [
            "value": "<user phoneNumber>",
            "type": "work",
            "primary": true
```

`],`

```json
    "externalId": "<external Id>",
    "active":true,
    "meta": {
        "resourceType": "User",
        "created": "2025-02-25T09:56:48.622Z",
        "lastModified": "2025-02-25T09:56:48.622Z",
        "location": "{BaseUrl}/Users/<userId>"
```

`},`

```json
    "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User",
        "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
```

`],`

```json
  "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
    "organization": "<user organizationalUnitId>"
```

**GET /Users/{id}**

Queries a user by ID.

**Limits**

If you specify the id parameter in the request, the user with the specified ID is returned. If the value of the id parameter is not the ID of an existing user, the request is rejected. You can query only users who are synchronized to EIAM by using SCIM.

**Sample request**

```bash
curl {BaseUrl}/Users/<userId> --header 'Authorization: Bearer <BearerToken>' --header " content-type:application/scim+json" -X GET
```

elf-managed applications

**Sample response**

```json
HTTP/1.1 200
    "id": "<userId>",
    "userName": "<user username>",
    "displayName": "<user display name>",
    "active": true,
    "emails": [
            "value": "<user email>",
            "type": "work",
            "primary": true
```

`],`

```json
    "phoneNumbers": [
            "value": "<user phoneNumber>",
            "type": "work",
            "primary": true
```

`],`

```json
    "externalId": "<external Id>",
    "active":true,
    "meta": {
        "resourceType": "User",
        "created": "2025-02-25T09:56:48.622Z",
        "lastModified": "2025-02-25T09:56:48.622Z",
        "location": "{BaseUrl}/Users/<userId>"
```

`},`

```json
    "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User",
        "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
```

`],`

```json
  "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
    "organization": "<user organizationalUnitId>"
```

**GET /Users**

Queries the information about specific users or queries all users.

**Limits**

If you specify the filter parameter, the user that meets the conditions in the filter parameter is returned. The filter parameter supports only the EQ and AND operators. The filter parameter must be URL-encoded. If you do not specify the filter parameter, you can query only users who are synchronized to EIAM by using SCIM. If you specify the filter parameter, you can query all users within the synchronization scope. elf-managed applications

**Sample request**

```bash
curl {BaseUrl}/Users<?parameters> --header 'Authorization: Bearer <BearerToken>' --head er "content-type:application/scim+json" -X GET
```

The following table describes the supported parameters.

| Param eter | Description | Example |
|---|---|---|
| filter | The eq expressions of the following fields are supported: externalId id userName emails[type eq "work"].value phoneNumbers[type eq "work"].value The filter parameter must be URL-encoded. | filter=externalId eq "<external Id>" filter=id eq "user xxxxxxxx" _ filter=userName eq "<user username>" filter=emails[type eq "work"].value eq "<user email>" filter=emails[type eq "work" and value eq "<user email>"] filter=phoneNumbers[type eq "work"].value eq "<user phoneNumber>" filter=phoneNumbers[type eq "work" and value eq " <user phoneNumber>"] |
| startIn dex | The page number. This parameter is optional. Default value: 1. | startIndex=1 |
| count | The number of users per page. This parameter is optional. Default value: 20. A maximum of 100 entries can be returned per page. If the number of entries exceeds 100, only 100 entries are returned. | count=20 |

**Sample response**

```json
HTTP/1.1 200
    "startIndex": 1,
    "totalResults": 2,
    "itemsPerPage": 20,
    "Resources": [
            "userName": "username1",
            "displayName": "displayName1",
            "active": true,
            "emails": [
```

elf-managed applications

```json
                    "value": "test1@example.com",
                    "type": "work",
                    "primary": true
```

`],`

```json
            "phoneNumbers": [
                    "value": "333*****333",
                    "type": "work",
                    "primary": true
```

`],`

```json
            "id": "user_addxxxxxxxxxxxxxxx1",
            "externalId": "externalId1",
            "meta": {
                "resourceType": "User",
                "created": "2025-03-06T03:16:40.201Z",
                "lastModified": "2025-03-06T03:16:40.201Z",
                "location": "{BaseUrl}/Users/user_addxxxxxxxxxxxxxxx1"
```

`},`

```json
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:User"
```

`]` `},`

```json
            "userName": "username2",
            "displayName": "displayName2",
            "active": true,
            "emails": [
                    "value": "test2@example.com",
                    "type": "work",
                    "primary": true
```

`],`

```json
            "phoneNumbers": [
                    "value": "333*****334",
                    "type": "work",
                    "primary": true
```

`],`

```json
            "id": "user_g3od4xxxxxxxxxxxxxxx2",
            "externalId": "externalId2",
            "meta": {
                "resourceType": "User",
                "created": "2025-03-06T06:58:35.997Z",
                "lastModified": "2025-03-06T06:58:35.997Z",
                "location": "{BaseUrl}/Users/user_g3od4xxxxxxxxxxxxxxx2"
```

`},`

```json
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:User"
```

`]` elf-managed applications `],`

```json
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:ListResponse"
```

`]`

**PUT /Users/{id}**

Replaces the information about a user.

**Limits**

The id parameter is required. You can modify only the fields that are defined in the "/Schemas" section of this topic. A PUT request is used to overwrite the original attributes. If you do not specify the id parameter, the original settings are retained. You can modify only users who are synchronized to EIAM by using SCIM and self-managed users. After you modify information about a self-managed user, the system automatically changes the user to one who is synchronized to EIAM by using SCIM.

**Sample request**

```bash
curl {BaseUrl}/Users/<userId> --header 'Authorization: Bearer <BearerToken>' --header " content-type:application/scim+json" -X PUT -d '<data>'
```

The following sample code provides an example of the data field: elf-managed applications

```json
    "id":"<userId>"
    "userName": "<user username>",
    "externalId": "<external Id>",
    "displayName": "<user display name>",
    "emails": [
            "primary": true,
            "type": "work",
            "value": "<user email>"
```

`],`

```json
   "phoneRegion":"86"
   "phoneNumbers": [
            "primary": true,
            "type": "work",
            "value": "<user phoneNumber>"
```

`],`

```json
  "active":true,
  "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User",
        "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
```

`],`

```json
  "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
    "organization": "<user organizationalUnitId>"
```

**Sample response**

elf-managed applications

```json
HTTP/1.1 200
    "id": "<userId>",
    "userName": "<user username>",
    "displayName": "<user display name>",
    "active": true,
    "emails": [
            "value": "<user email>",
            "type": "work",
            "primary": true
```

`],`

```json
    "phoneNumbers": [
            "value": "<user phoneNumber>",
            "type": "work",
            "primary": true
```

`],`

```json
    "externalId": "<external Id>",
    "active":true,
    "meta": {
        "resourceType": "User",
        "created": "2025-02-25T09:56:48.622Z",
        "lastModified": "2025-02-25T09:56:48.622Z",
        "location": "{BaseUrl}/Users/<userId>"
```

`},`

```json
    "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User",
        "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
```

`],`

```json
  "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
    "organization": "<user organizationalUnitId>"
```

**PATCH /Users/{id}**

Updates the information about a user.

**Limits**

The id parameter is required. You can modify only the fields that are defined in the "/Schemas" section of this topic. You can use a PATCH request for the Add and Replace operations, but not for the Remove operation. If you specify the Remove operation, it is ignored. The path parameter is optional. For more information, see the data field in Sample request. elf-managed applications You can modify only users who are synchronized to EIAM by using SCIM and self-managed users. After you modify information about a self-managed user, the system automatically changes the user to one who is synchronized to EIAM by using SCIM.

**Sample request**

```bash
curl {BaseUrl}/Users/<userId> --header 'Authorization: Bearer <BearerToken>' --header " content-type:application/scim+json" -X PATCH -d '<data>'
```

The following sample code provides an example of the data field:

**Example 1: Add the displayName field and do not specify the path parameter**

```json
    "Operations": [
            "op": "add",
            "value": {
                "diplayName": "updateDisplayName"
```

`],`

```json
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:PatchOp"
```

`]`

**Example 2: Modify the displayName field and specify the path parameter**

```json
    "Operations": [
            "op": "Replace",
            "path": "diplayName",
            "value": "updateDisplayName"
```

`],`

```json
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:PatchOp"
```

`]`

**Example 3: Modify the emails field and do not specify the path parameter**

elf-managed applications

```json
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:PatchOp"
```

`],`

```json
    "Operations": [{
          "op": "Replace",
          "value": {
            "emails": [{
                    "value": "test@example.com",
                    "type": "work",
                    "primary": true
```

`}]` `}]`

**Example 4: Modify the emails field and specify the path parameter**

```json
    "Operations": [
            "op": "Replace",
            "path": "emails[type eq \"work\"].value",
            "value": "test@example.com"
```

`],`

```json
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:PatchOp"
```

`]`

**Example 5: Disable the account field and specify the path parameter**

```json
    "Operations": [
            "op": "Replace",
            "path": "active",
            "value": "false"
```

`],`

```json
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:PatchOp"
```

`]`

**Example 6: Disable the account field and do not specify the path parameter**

elf-managed applications

```json
    "Operations": [
            "op": "Replace",
            "value": {
                "active": false
```

`],`

```json
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:PatchOp"
```

`]`

**Sample response**

```
HTTP/1.1 204
```

**DELETE /Users/{id}**

Deletes a user.

**Limits**

The id parameter is required. You can delete only synchronized users.

**Sample request**

```bash
curl {BaseUrl}/Users/<userId> --header 'Authorization: Bearer <BearerToken' --header "c ontent-type:application/scim+json" -X DELETE
```

**Sample response**

```
HTTP/1.1 204
```

**Group**

**POST /Groups**

Synchronizes a user group.

**Limits**

For more information about the limits on fields, see the "/Schemas" section of this topic. You can specify up to 1,000 users. If the number of users exceeds 1,000, an error occurs. If a specified user does not exist or is not synchronized, ignore the user. If you create a user group, the information about the user group is returned. elf-managed applications

**Sample request**

```json
  "externalId": "<external Id>",
  "displayName": "<group name>",
  "members": [
      "value": "user_4pnblmv5oxxxxxxxxxxxxo7pcuxwue",
      "$ref": "{BaseUrl}/Users/user_4pnblmv5oxxxxxxxxxxxxo7pcuxwue",
      "type": "User"
```

`},`

```json
      "value": "user_d3rmo3xxxxxxxxxbo6vhcfq",
      "$ref": "{BaseUrl}/Users/user_d3rmo3xxxxxxxxxbo6vhcfq",
      "type": "User"
```

`],`

```json
  "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:Group"
```

`]`

**Sample response**

```json
HTTP/1.1 201
    "id": "group_bz7xxxxxxxxxx3hhxdha",
    "displayName": "<group name>",
    "externalId": "<external Id>",
    "members": [
            "value": "user_4pnblmv5oxxxxxxxxxxxxo7pcuxwue",
            "$ref": "{BaseUrl}/Users/user_4pnblmv5oxxxxxxxxxxxxo7pcuxwue"
```

`],`

```json
    "meta": {
        "resourceType": "Group",
        "created": "2025-03-06T06:35:46.009Z",
        "lastModified": "2025-03-06T06:35:46.009Z",
        "location": "{BaseUrl}/Groups/group_bz7xxxxxxxxxx3hhxdha"
```

`},`

```json
    "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:Group"
```

`]`

**GET /Groups/{id}**

Queries a user group. elf-managed applications

**Limits**

The user group specified by the ID is returned. By default, the members value is returned. You can specify excludedAttributes=members. In this case, the members field is ignored if the request contains the excludedAttributes parameter. If the value of the id parameter is not the ID of an existing user group, the request is rejected. You can query only the user groups that are synchronized to EIAM by using SCIM.

**Sample request**

```bash
curl {BaseUrl}/Groups/<groupId><?parameters> --header 'Authorization: Bearer <BearerTok en>' --header "content-type:application/scim+json" -X GET
```

The following table describes the supported parameters.

| Parameter | Description | Example |
|---|---|---|
| excludedAttributes | Specifies which field is not returned. Set the value to members, which means that the members field is not returned. | members |

**Sample response**

```json
HTTP/1.1 200
    "id": "<groupId>",
    "displayName": "<group name>",
    "externalId": "<external Id>",
    "members": [
            "value": "user_4pnblmv5oxxxxxxxxxxxxo7pcuxwue",
            "$ref": "{BaseUrl}/Users/user_4pnblmv5oxxxxxxxxxxxxo7pcuxwue"
```

`],`

```json
    "meta": {
        "resourceType": "Group",
        "created": "2025-03-06T06:35:46.009Z",
        "lastModified": "2025-03-06T06:35:46.009Z",
        "location": "{BaseUrl}/Groups/group_bz7xxxxxxxxxx3hhxdha"
```

`},`

```json
    "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:Group"
```

`]`

**GET /Groups**

elf-managed applications Queries the information about specific user groups or queries all user groups.

**Limits**

If you specify the filter parameter, the user group that meets the conditions in the filter parameter is returned. The filter parameter supports only the EQ and AND operators. If you do not specify the filter parameter, all user groups are returned. The users in the user groups are not returned. The standard pagination method of SCIM 2.0 is supported. By default, 20 entries are returned per page. A maximum of 100 entries can be returned per page. If the number of entries exceeds 100, only 100 entries are returned. You can query only synchronized user groups.

**Sample request**

```bash
curl {BaseUrl}/Groups<?parameters> --header 'Authorization: Bearer <BearerToken>' --hea der "content-type:application/scim+json" -X GET
```

The following table describes the supported parameters.

| Parameter | Description | Example |
|---|---|---|
| filter | Only the eq expressions of displayName, externalId, and id are supported. The filter parameter must be URL-encoded. | filter=displayName eq "demoDisplayName" filter=externalId eq "demoExternalId" filter=id eq "demoGroupId" |
| startIndex | The page number. This parameter is optional. Default value: 1. | startIndex=1 |
| count | The number of users per page. This parameter is optional. Default value: 20. A maximum of 100 entries can be returned per page. If the number of entries exceeds 100, only 100 entries are returned. | count=20 |

**Sample response**

elf-managed applications

```json
HTTP/1.1 200
    "startIndex": 1,
    "totalResults": 2,
    "itemsPerPage": 20,
    "Resources": [
            "displayName": "GroupName1",
            "id": "group_7xh7xxxxxxxxxxgvajbbowpe",
            "externalId": "externalId1",
            "meta": {
                "resourceType": "Group",
                "created": "2025-03-07T10:03:21.784Z",
                "lastModified": "2025-03-07T10:03:21.784Z",
                "location": "{BaseUrl}/Groups/group_7xh7xxxxxxxxxxgvajbbowpe"
```

`},`

```json
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:Group"
```

`]` `},`

```json
            "displayName": "GroupName2",
            "id": "group_bz7qhxxxxxxxxxle3hhxdha",
            "externalId": "externalId2",
            "meta": {
                "resourceType": "Group",
                "created": "2025-03-06T06:35:46.009Z",
                "lastModified": "2025-03-06T10:46:36.549Z",
                "location": "{BaseUrl}/Groups/group_bz7qhxxxxxxxxxle3hhxdha"
```

`},`

```json
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:Group"
```

`]` `],`

```json
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:ListResponse"
```

`]`

**PUT /Groups/{id}**

Replaces the information about a user group.

**Limits**

The id parameter is required. You can modify only the fields that are defined in the "/Schemas" section of this topic. A PUT request is used to overwrite the original attributes. You can replace the users in the user groups. You can specify up to 1,000 users. If the number of users exceeds 1,000, an error is reported. elf-managed applications You can modify only the user groups that are synchronized to EIAM by using SCIM. You can replace only users that are synchronized to EIAM by using SCIM in the user groups. The information about the user group and all users are returned.

**Sample request**

```bash
curl {BaseUrl}/Groups/<groupId> --header 'Authorization: Bearer <BearerToken>' --header "content-type:application/scim+json" -X PUT -d '<data>'
```

The following sample code provides an example of the data field:

```json
    "id": "<groupId>",
    "displayName": "<group name>",
    "externalId": "<external Id>",
    "members": [
            "value": "user_4pnblmv5oxxxxxxxxxxxxo7pcuxwue",
            "$ref": "{BaseUrl}/Users/user_4pnblmv5oxxxxxxxxxxxxo7pcuxwue"
```

`],`

```json
    "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:Group"
```

`]`

**Sample response**

```json
HTTP/1.1 200
    "id": "<groupId>",
    "displayName": "<group name>",
    "externalId": "<external Id>",
    "members": [
            "value": "user_4pnblmv5oxxxxxxxxxxxxo7pcuxwue",
            "$ref": "{BaseUrl}/Users/user_4pnblmv5oxxxxxxxxxxxxo7pcuxwue"
```

`],`

```json
    "meta": {
        "resourceType": "Group",
        "created": "2025-03-06T06:35:46.009Z",
        "lastModified": "2025-03-06T06:35:46.009Z",
        "location": "{BaseUrl}/Groups/group_bz7xxxxxxxxxx3hhxdha"
```

`},`

```json
    "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:Group"
```

`]`

**PATCH /Groups/{id}**

elf-managed applications Updates the information about a user group.

**Limits**

The id parameter is required. You can modify only the fields that are defined in the "/Schemas" section of this topic. You can use a PATCH request for the Add, Replace, and Remove operations. You can replace up to 1,000 users. If the number of users exceeds 1,000, an error is reported. You can add up to 100 users. If the number of users exceeds 100, an error is reported. You can remove up to 100 users. If the number of users exceeds 100, an error is reported. You can modify only the user groups that are synchronized to EIAM by using SCIM. You can update only users that are synchronized to EIAM by using SCIM in the user groups. The information about the user group and all users are returned.

**Sample request**

```bash
curl {BaseUrl}/Groups/<groupId> --header 'Authorization: Bearer <BearerToken>' --header "content-type:application/scim+json" -X PATCH -d '<data>'
```

The following sample code provides an example of the data field:

**Example 1: Remove all users who are synchronized to EIAM by using SCIM from the**

**user group**

```json
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:PatchOp"
```

`],`

```json
    "Operations": [
            "op": "remove",
            "path": "members"
```

`]`

**Example 2: Add users to or remove users from the user group**

elf-managed applications

```json
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
    "Operations": [
        "op": "remove",
        "path": "members",
        "value": [{
            "value": "user_dm57xxxxxxxxxxx5wzecz"
```

`}]`

```json
        "op": "add",
        "path": "members",
        "value": [{
            "value": "user_sdfqxxxxxxxxxxkzhw5wz"
```

`}]` `]`

**Example 3: Replace users**

```json
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
    "Operations": [
        "op": "replace",
        "path": "members",
        "value": [{
            "value": "user_dm57xxxxxxxxxxx5wzecz"
```

`}]` `]`

**Sample response**

elf-managed applications

```json
HTTP/1.1 200
    "id": "<groupId>",
    "displayName": "<group name>",
    "externalId": "<external Id>",
    "members": [
            "value": "user_4pnblmv5oxxxxxxxxxxxxo7pcuxwue",
            "$ref": "{BaseUrl}/Users/user_4pnblmv5oxxxxxxxxxxxxo7pcuxwue"
```

`],`

```json
    "meta": {
        "resourceType": "Group",
        "created": "2025-03-06T06:35:46.009Z",
        "lastModified": "2025-03-06T06:35:46.009Z",
        "location": "{BaseUrl}/Groups/group_bz7xxxxxxxxxx3hhxdha"
```

`},`

```json
    "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:Group"
```

`]`

**DELETE /Groups/{id}**

Deletes a user group.

**Limits**

The id parameter is required. If a user is added to the user group, the user is removed from the user group when you delete the user group. You can delete only the user groups that are synchronized to EIAM by using SCIM.

**Sample request**

```bash
curl {BaseUrl}/Groups/<groupId> --header 'Authorization: Bearer <BearerToken>' --header "content-type:application/scim+json" -X DELETE
```

**Sample response**

```
HTTP/1.1 204
```

### Application development API

**reference**

elf-managed applications

#### API operations for application

**development**

1. . Overview**
This topic describes the API operations related to organizations and accounts that are provided by Identity as a Service (IDaaS). You can manage IDaaS account and organization data by referring to this topic. IDaaS provides four categories of API operations:
1. **API operation used to obtain a token** . All the other API operations are called based on
the returned token.
2. **API operation used to query and manage accounts** .
3. **API operation used to query and manage organizations** .
4. **API operation used to obtain synchronization scopes** . Only accounts and
organizations that are in the synchronization scope can be managed.
2. . Call methods**

**API authentication**

You must obtain an access token before you can call most of the API operations in IDaaS. . Obtain the client_id and client_secret from the common configurations of the application, and call the GenerateToken operation to generate an application authentication token.

**Note**

Note: Unlike Alibaba Cloud API operations, the Developer API operations provided by IDaaS rely on the secrets of applications in IDaaS for authentication, and users are granted permissions to call operations on the IDaaS API tab. Developer API permissions are not based on Resource Access Management (RAM).

**Sample code and debugging**

Use the Apache HttpClient toolkit to call API operations. For a list of API operations, see List of API operations by function.

**API operations**

The following table describes some API operations. For more information, see List of API operations by function.

| Category | Scenario | API operation | Permission (set on the IDaaS API tab) |
|---|---|---|---|
| Token | Obtain a token | Obtains a token: GenerateToken | - |

elf-managed applications

| Account | Manage accounts | Creates an account: CreateUser Updates an account: PatchUser Deletes an account: DeleteUser Enables an account: EnableUser Disables an account: DisableUser | urn:alibaba:idaas :scope:user:man ager all _ |
|---|---|---|---|
|   | Query accounts | Queries account information: GetUser Queries accounts: ListUsers Queries a password policy: GetUserPasswordPolicy | urn:alibaba:idaas :scope:user:read _ all |
| Organization | Manage organizations | Creates an organization: CreateOrganizationalUnit Modifies organization information: PatchOrganizationalUnit Deletes an organization: DeleteOrganizationalUnit | urn:alibaba:idaas :scope:organizati onal unit:manag _ er all _ |
|   | Query organizations | Queries organization information: GetOrganizationalUnit Queries organizations: ListOrganizationalUnits Queries parent IDs of an organization: ListOrganizationalUnitParentIds | urn:alibaba:idaas :scope:organizati onal unit:read all _ _ |
| Synchronizatio n scope | Query the synchronization scope | Queries the synchronization scope: GetApplicationProvisioningScope | - |

### Open source code

This topic describes the open source components, frameworks, and tools required or referenced during development on Identity as a Service (IDaaS) to help developers learn about the technologies behind IDaaS, the compliance requirements, and the potential limits of open source protocols.

**Applicable scenarios**

Enterprise applications must be integrated with IDaaS to implement identity authentication, Single Sign-On (SSO), or identity management.

**Open source code repositories**

IDaaS provides integration examples open sourced for enterprise application developers. The following table describes some open source code repositories. Each repository has comprehensive instructions on configuration, use, and development. elf-managed applications

| Repository | Description | Link |
|---|---|---|
| java-spring-oidc- sample | This repository shows how to implement SSO for an application based on the OpenID Connect (OIDC) Authorization Code. This method is the most frequently used method to implement SSO. It is also used to connect in-house applications to IDaaS for SSO. | https://github.com/aliy unidaas/java-spring- oidc-sample |
| java-spring-saml- sample | This repository shows how to implement SSO for an application based on Security Assertion Markup Language (SAML). | https://github.com/aliy unidaas/java-spring- saml-sample |
| java-device-code-flow- sample | This repository shows how to implement SSO for an application based on the OIDC Device Flow. It is used for secure logons when the device does not have a web browser. | https://github.com/aliy unidaas/java-device- code-flow-sample |
| java-fc-ram-user-push- sample | This repository uses Function Compute as an intermediate service to synchronize IDaaS accounts to Resource Access Management (RAM). | https://github.com/aliy unidaas/java-fc-ram- user-push-sample |
| java-sync-sdk | This SDK is used to receive events pushed by IDaaS. | https://github.com/aliy unidaas/java-sync-sdk |
| java-fc-sync-sdk | This SDK can be used together with java-sync-sdk to use the Function Compute endpoint to receive events pushed by IDaaS. | https://github.com/aliy unidaas/java-fc-sync- sdk |

**References**

You can get the URLs of IDaaS open source code repositories at https://github.com/aliyunidaas.
