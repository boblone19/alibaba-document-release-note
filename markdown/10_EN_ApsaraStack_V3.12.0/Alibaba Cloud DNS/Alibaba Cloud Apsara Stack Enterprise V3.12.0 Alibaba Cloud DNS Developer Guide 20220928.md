---
title: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Alibaba Cloud DNS Developer Guide 20220928"
product_version: "V3.12.0"
doc_version: "20220928"
pdf_pages: 19
source_pdf: "Alibaba Cloud Apsara Stack Enterprise V3.12.0 Alibaba Cloud DNS Developer Guide 20220928.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/V3.12/%E7%BD%91%E7%BB%9C/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20V3.12.0%20Alibaba%20Cloud%20DNS%20Developer%20Guide%2020220928.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise V3.12.0 Alibaba Cloud DNS Developer Guide 20220928

## Table of Contents

- 1 Overview
  - 1.1 Calling methods
  - 1.2 Supported formats
  - 1.3 Instructions
  - 1.4 Time format
- 2 List of operations by function
- 3 Prerequisites
  - 3.1 Obtain an AccessKey pair
  - 3.2 Obtain an endpoint
- 4 SDK example
  - 4.1 Create a client
  - 4.2 Obtain global authoritative zones
  - 4.3 Obtain global authoritative RRSets
  - 4.4 Add global RRSets
  - 4.5 Delete global RRSets
  - 4.6 Update global RRSets
  - 4.7 Configure descriptions for global RRSets

## 1 Overview

### 1.1 Calling methods

You can use a pair of AccessKey ID and AccessKey Secret to call API operations. You can use SDKs of different languages, or create a client based on the signature description provided by the POP gateway.

### 1.2 Supported formats

AccessKey ID and AccessKey Secret of an Apsara Stack tenant account Temporary AccessKey ID and AccessKey Secret of an Apsara Stack tenant account AccessKey ID and AccessKey Secret of a RAM user account Temporary AccessKey ID and AccessKey Secret of a RAM user account

### 1.3 Instructions

The AccessKey ID is used to identify users. The AccessKey Secret is used to compute the request signature.

### 1.4 Time format

Unless otherwise specified, the time string is a UTC+0 time in the format of YYYY-MM-DDTHH:mm:ssZ. For example, 2018-01-16T09:00:01Z indicates 17:00:01 on January 16, 2018, in China Standard Time (UTC+8). by function

## 2 List of operations by function

DNS V2.0 provides the following API operations.

| API | Description |
|---|---|
| ObtainGlobalAuthZoneList | Obtains global authoritative zones |
| ObtainGlobalAuthRecordList | Obtains global authoritative RRSets |
| AddGlobalRrSet | Adds global RRSets |
| DeleteGlobalRrSet | Deletes global RRSets |
| UpdateGlobalRrSet | Updates global RRSets |
| RemarkGlobalRrSet | Configures descriptions for global RRSets |

## 3 Prerequisites

### 3.1 Obtain an AccessKey pair

You can obtain an AccessKey pair in the Apsara Stack Cloud Management (ASCM) console. Obtain the AccessKey pair of an organization To obtain the AccessKey pair of an organization, perform the following operations:
1. Log on to the ASCM console as an administrator.
2. In the top navigation bar, click Ent erprise.
3. In the left-side navigation pane of the Ent erprise page, click Organizat ions.
4. In the Organizations structure, click the
icon on the right of the organization to be added.
5. Choose AccessKey from the shortcut menu.
6. In the AccessKey dialog box that appears, view the AccessKey pair of the organization.
Not e An AccessKey pair is automatically allocated to a level-1 organization. Subordinate organizations use the same AccessKey pair as their level-1 organization. Obtain the AccessKey of a personal account To obtain the AccessKey pair of a personal account, perform the following operations:
1. Log on to the ASCM console as an administrator.
2. In the upper-right corner of the homepage, move the pointer over the user profile picture and click
User Inf ormat ion.
3. In the Apsara St ack AccessKey Pair section of the User Information page, view your AccessKey
pair. Not e The AccessKey pair is made up of the AccessKey ID and AccessKey secret. These credentials provide you full permissions on Apsara Stack resources. You must keep the AccessKey pair confidential.

### 3.2 Obtain an endpoint

Procedure
1. Log on to the Apsara Infrastructure Management Framework console as an administrator.
2. In the top navigation bar, choose Operat ions > Clust er Operat ions.
3. On the Clust er Operat ions page, select dnsProduct from the Project drop-down list.
4. In the Service Instances section, click Det ails in the Actions column corresponding to dnsService.
5. In the Machine Information section, click T erminal in the Actions column corresponding to a server
to go to the console.
6. Run the `sudo docker ps -l` command to obtain the ID of the current container.
7. Run the sudo docker inspect ${container id} |grep env command to obtain the endpoint of
the current environment. The endpoint is the value corresponding to pop_out_endpoint (the string starting with "api.").

## 4 SDK example

### 4.1 Create a client

You need to specify a region ID, AccessKey ID, and AccessKey Secret to create a client.

```
1.    if client, err := genesisdns.NewClientWithAccessKey(RegionId, AccessKey, AccessSecret
); err == nil {
2.      //Normal business logic
3.    } else {
4.      //Business logic to handle exceptions
5.    }
1.    from aliyunsdkcore.client import AcsClient
2.    from aliyunsdkcore.acs_exception.exceptions import ClientException
3.    from aliyunsdkcore.acs_exception.exceptions import ServerException
```

`4.` `5.`

```
6.    client = AcsClient("<access-key-id>",
7.       "<access-key-secret>",
8.       "<region-id>");
1.    public static void main(String[] args) {
2.         DefaultProfile profile = DefaultProfile.getProfile("{regionid}","{ak}", "{secret
}");
3.         IAcsClient client = new DefaultAcsClient(profile);
4.    }
```

### 4.2 Obtain global authoritative zones

```
1. if client, err := genesisdns.NewClientWithAccessKey("{regionid}","{ak}", "{secret}"); er
r == nil {
2.     request := genesisdns.CreateObtainGlobalAuthZoneListRequest()
3.     request.SetDomain("{endpoint}")
4.     if response, err := client.ObtainGlobalAuthZoneList(request); err == nil {
5.         fmt.Println(response.ZoneList)
6.     }
7. }
```

```
1. client = AcsClient("{ak}", "{secret}", "{regionid}");
```

`2.`

```
3. request = ObtainGlobalAuthZoneListRequest.ObtainGlobalAuthZoneListRequest()
4. request.set_PageSize(10)
5. region_provider.modify_point("GenesisDns", "{regionid}","{endpoint}")
6. try:
7.     response = client.do_action_with_exception(request)
8.     print(response)
9. except ServerException as e:
10.     print(e)
11. except ClientException as e:
12.     print(e)
1. public static void main(String[] args) {
2.     DefaultProfile profile = DefaultProfile.getProfile("{regionid}","{ak}", "{secret}");
3.     IAcsClient client = new DefaultAcsClient(profile);
4.     ObtainGlobalAuthZoneListRequest request = new ObtainGlobalAuthZoneListRequest();
5.     try {
6.         request.setEndpoint("{endpoint}");
7.         request.setConnectTimeout(1000);
8.         request.setReadTimeout(1000);
9.         request.setPageSize(10);
10.         ObtainGlobalAuthZoneListResponse response = client.getAcsResponse(request);
11.         System.out.println(JSON.toJSONString(response.getZoneList()));
12.     } catch (Exception ex) {
13.         System.out.println(ex.getMessage());
14.     }
15. }
```

### 4.3 Obtain global authoritative RRSets

RRSets

```
1. if client, err := genesisdns.NewClientWithAccessKey("{regionid}","{ak}", "{secret}")); e
rr == nil {
2.     request := genesisdns.CreateObtainGlobalAuthRecordListRequest()
3.     request.SetDomain("{endpoint}")
4.     request.Id = requests.Integer("{zone id}")
5.     if response, err := client.ObtainGlobalAuthRecordList(request); err == nil {
6.         fmt.Println(response.Records)
7.     }
8. }
```

```
1. from aliyunsdkcore.client import AcsClient
2. from aliyunsdkcore.profile import region_provider
3. from aliyunsdkcore.acs_exception.exceptions import ClientException
4. from aliyunsdkcore.acs_exception.exceptions import ServerException
5. from aliyunsdkgenesisdns.request.v20180925 import ObtainGlobalAuthRecordListRequest
7. client = AcsClient("{ak}", "{secret}", "{regionid}")
9. request = ObtainGlobalAuthRecordListRequest.ObtainGlobalAuthRecordListRequest()
10. request.set_PageSize(10)
11. request.set_Id({zone id})
12. region_provider.modify_point("GenesisDns", "{regionid}", "{endpoint}")
13. try:
14.     response = client.do_action_with_exception(request)
15.     print(response)
16. except ServerException as e:
17.     print(e)
18. except ClientException as e:
19.     print(e)
1. public static void main(String[] args) {
2.     DefaultProfile profile = DefaultProfile.getProfile("{regionid}","{ak}", "{secret}");
3.     IAcsClient client = new DefaultAcsClient(profile);
4.     ObtainGlobalAuthRecordListRequest request = new ObtainGlobalAuthRecordListRequest();
5.     try {
6.         request.setEndpoint("{endpoint}");
7.         request.setConnectTimeout(1000);
8.         request.setReadTimeout(1000);
9.         request.setPageSize(10);
10.         request.setId(Long.parseLong("{zone id}"));
11.         ObtainGlobalAuthRecordListResponse response = client.getAcsResponse(request);
12.         System.out.println(JSON.toJSONString(response.getRecords()));
13.     } catch (Exception ex) {
14.         System.out.println(ex.getMessage());
15.     }
16. }
```

### 4.4 Add global RRSets

The following examples describe how a Resource Record Set (RRSet) is defined.

```
1.         request.RrSet = "[\"2001:0:0:0:0:0:0:1\"]" //A RRSet with an AAAA record
2.         request.RrSet = "[\"2001:0:0:0:0:0:0:1\", \"2001::2\"]" //A RRSet with two AAAA
records
3.         request.RrSet = "[\"2001:0:0:0:0:0:0:1 10\", \"2001::2 10\"]" //A RRSet with two
weighted AAAA records
4.         request.Type = "AAAA"
```

`5.`

```
6.         request.RrSet = "[\"www.aliyun.com. \"]" //A RRSet with a CNAME record
7.         request.RrSet = "[\"www.aliyun.com. 10\",\"www.taobao.com 30\"]" //A RRSet with
two weighted CNAME records
8.         request.Type = "CNAME"
```

`9.`

```
10.         request.RrSet = "[\"10 mailserver1.example.com. \"]" //A RRSet with an MX recor
```

`d`

```
11.         request.Type = "MX"
12.
13.         request.RrSet = "[\"10 mailserver1.example.com.\",\"20 mailserver2.example.com.
\"]" //A RRSet with two MX records
14.         request.RrSet = "[\"v=spf1 ip4:192.168.0.1/16 ip6:2001::1/96 ~all\"]" //A RRSet
with a TXT record
15.         request.Type = "TXT"
16.
17.         request.RrSet = "[\"1 10 8080 www1.example.com.\", \"2 20 8081 www2.example.com
. \"]" //A RRSet with two SRV records
18.         request.Type = "SRV"
19.
20.         request.RrSet = "[\"100 50 \\\"S\\\" \\\"Z3950+I2L+I2C\\\" \\\"\\\" _z3950._tcp
.example.com. \"]" //A RRSet with a NAPTR record
21.         request.Type = "NAPTR"
22.
23.         request.RrSet = "[\"0 issue \\\"caa.example.com\\\"\",\"0 issuewild \\\";\\\"\"
]" //A RRSet with a CAA record
24.         request.Type = "CAA"
25.
26.         request.RrSet = "[\"inner-ns1.example01.com. hostmaster.example01.com. 1 7200 9
00 1209600 86400\"]" //A RRSet with an SOA record
27.         request.Type = "SOA"
28.
29.         request.RrSet = "[\"ns1.example.com.\",\"ns2.example.com. \"]" //A RRSet with t
wo NS records
30.         request.Type = "NS"
```

```
1. func main()  {
2.     if client, err := genesisdns.NewClientWithAccessKey("{regionid}","{ak}", "{secret}")
; err == nil {
3.         request := genesisdns.CreateAddGlobalRrSetRequest()
4.         request.SetDomain("{endpoint}")
5.         request.ZoneId = requests.Integer("{zone id}")
6.         request.Ttl = requests.Integer("300")
7.         request.Type = "A"
8.         request.RrSet = "[\"1.1.1.1\"]"
9.         request.Rr = "sdka"
10.
11.         if response, err := client.AddGlobalRrSet(request); err == nil {
12.             fmt.Println(response.RequestId, response.Id)
13.         }
14.     }
15. }
1. from aliyunsdkcore.client import AcsClient
2. from aliyunsdkcore.profile import region_provider
3. from aliyunsdkcore.acs_exception.exceptions import ClientException
4. from aliyunsdkcore.acs_exception.exceptions import ServerException
5. from aliyunsdkgenesisdns.request.v20180925 import AddGlobalRrSetRequest
7. client = AcsClient("{ak}", "{secret}", "{regionid}")
9. request = AddGlobalRrSetRequest.AddGlobalRrSetRequest()
10. request.set_ZoneId(93)
11. request.set_Rr("sdk_python_a")
12. request.set_RrSet("[\"3.3.3.3\"]")
13. request.set_Ttl(300)
14. request.set_Type("A")
15.
16. region_provider.modify_point("GenesisDns", "{regionid}", "{endpoint}")
17. try:
18.     response = client.do_action_with_exception(request)
19.     print(response)
20. except ServerException as e:
21.     print(e)
22. except ClientException as e:
23.     print(e)
```

```
1. public static void main(String[] args) {
2.     DefaultProfile profile = DefaultProfile.getProfile("{regionid}","{ak}", "{secret}");
3.     IAcsClient client = new DefaultAcsClient(profile);
4.     AddGlobalRrSetRequest request = new AddGlobalRrSetRequest();
5.     try {
6.         request.setEndpoint("{endpoint}");
7.         request.setConnectTimeout(1000);
8.         request.setReadTimeout(1000);
9.         request.setZoneId(Long.parseLong("93"));
10.         request.setRr("sdk_java_a");
11.         request.setTtl(300);
12.         request.setType("A");
13.         request.setRrSet("[\"1.1.1.1\", \"2.2.2.2\"]");
14.         AddGlobalRrSetResponse response = client.getAcsResponse(request);
15.         System.out.println(JSON.toJSONString(response));
16.     } catch (Exception ex) {
17.         System.out.println(ex.getMessage());
18.     }
19. }
```

### 4.5 Delete global RRSets

```
1.    package main
```

`2.`

```
3.    import (
4.        "fmt"
5.        "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
6.        "github.com/aliyun/alibaba-cloud-sdk-go/services/genesisdns"
7.    )
9.    func main()  {
10.        if client, err := genesisdns.NewClientWithAccessKey("{regionid}","{ak}", "{secre
t}"); err == nil {
11.            request := genesisdns.CreateDeleteGlobalRrSetRequest()
12.            request.SetDomain("{endpoint}")
13.            request.Id = requests.Integer("{rrSet id")
14.
15.            if response, err := client.DeleteGlobalRrSet(request); err == nil {
16.                fmt.Println(response.RequestId)
17.            }
18.        }
19.    }
```

```
1.    from aliyunsdkcore.client import AcsClient
2.    from aliyunsdkcore.profile import region_provider
3.    from aliyunsdkcore.acs_exception.exceptions import ClientException
4.    from aliyunsdkcore.acs_exception.exceptions import ServerException
5.    from aliyunsdkgenesisdns.request.v20180925 import DeleteGlobalRrSetRequest
7.    client = AcsClient("{ak}", "{secret}", "{regionid}")
9.    request = DeleteGlobalRrSetRequest.DeleteGlobalRrSetRequest()
10.    request.set_Id(170)
11.
12.    region_provider.modify_point("GenesisDns", "{regionid}", "{endpoint}")
13.    try:
14.        response = client.do_action_with_exception(request)
15.        print(response)
16.    except ServerException as e:
17.        print(e)
18.    except ClientException as e:
19.        print(e)
1.    public static void main(String[] args) {
2.        DefaultProfile profile = DefaultProfile.getProfile("{regionid}","{ak}", "{secret}
");
3.        IAcsClient client = new DefaultAcsClient(profile);
4.        DeleteGlobalRrSetRequest request = new DeleteGlobalRrSetRequest();
5.        try {
6.            request.setEndpoint("{endpoint}");
7.            request.setConnectTimeout(1000);
8.            request.setReadTimeout(1000);
9.            request.setId(Long.parseLong("{RrSet id}"));
10.            DeleteGlobalRrSetResponse response = client.getAcsResponse(request);
11.            System.out.println(JSON.toJSONString(response));
12.        } catch (Exception ex) {
13.            System.out.println(ex.getMessage());
14.        }
```

### 4.6 Update global RRSets

```
1.    package main
```

`2.`

```
3.    import (
4.        "fmt"
5.        "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
6.        "github.com/aliyun/alibaba-cloud-sdk-go/services/genesisdns"
7.    )
9.    func main()  {
10.        if client, err := genesisdns.NewClientWithAccessKey("{regionid}","{ak}", "{secre
t}"); err == nil {
11.            request := genesisdns.CreateUpdateGlobalRrSetRequest()
12.            request.SetDomain("{endpoint}")
13.            request.RrsetId = requests.Integer("{RrSet id}")
14.            request.Rr = "go_sdk_a"
15.            request.RrSet = "[\"8.8.8.8\"]"
16.            request.Ttl = requests.Integer("300")
17.            request.Type = "A"
18. 19.
20.            if response, err := client.UpdateGlobalRrSet(request); err == nil {
21.                fmt.Println(response.RequestId)
22.            }
23.        }
24.    }
1.    from aliyunsdkcore.client import AcsClient
2.    from aliyunsdkcore.profile import region_provider
3.    from aliyunsdkcore.acs_exception.exceptions import ClientException
4.    from aliyunsdkcore.acs_exception.exceptions import ServerException
5.    from aliyunsdkgenesisdns.request.v20180925 import UpdateGlobalRrSetRequest
7.    client = AcsClient("{ak}", "{secret}", "{regionid}")
9.    request = UpdateGlobalRrSetRequest.UpdateGlobalRrSetRequest()
10.    request.set_RrsetId(165)
11.    request.set_Type("A")
12.    request.set_Rr("sdk_python_a")
13.    request.set_RrSet("[\"3.3.3.3\"]")
14.    request.set_Ttl(300)
15.
16.    region_provider.modify_point("GenesisDns", "{regionid}", "{endpoint}")
17.    try:
18.        response = client.do_action_with_exception(request)
19.        print(response)
20.    except ServerException as e:
21.        print(e)
22.    except ClientException as e:
23.        print(e)
```

```
1.    public static void main(String[] args) {
2.        DefaultProfile profile = DefaultProfile.getProfile("{regionid}","{ak}", "{secret}
");
3.        IAcsClient client = new DefaultAcsClient(profile);
4.        UpdateGlobalRrSetRequest request = new UpdateGlobalRrSetRequest();
5.        try {
6.            request.setEndpoint("{endpoint}");
7.            request.setConnectTimeout(1000);
8.            request.setReadTimeout(1000);
9.            request.setRrsetId(Long.parseLong("165"));
10.            request.setRr("sdk_java_a");
11.            request.setRrSet("[\"4.4.4.4\"]");
12.            request.setTtl(300);
13.            request.setType("A");
14.
15.            UpdateGlobalRrSetResponse response = client.getAcsResponse(request);
16.            System.out.println(JSON.toJSONString(response));
17.        } catch (Exception ex) {
18.            System.out.println(ex.getMessage());
19.        }
20.    }
```

### 4.7 Configure descriptions for global RRSets

RRSets

```
1. package main
```

`2.`

```
3. import (
4.     "fmt"
5.     "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
6.     "github.com/aliyun/alibaba-cloud-sdk-go/services/genesisdns"
7. )
9. func main()  {
10.     if client, err := genesisdns.NewClientWithAccessKey(""{regionid}","{ak}", "{secret}
"); err == nil {
11.         request := genesisdns.CreateRemarkGlobalRrSetRequest()
12.         request.SetDomain("{endpoint}")
13.         request.Id = requests.Integer("165")
14.         request.Remark = "go remark"
15. 16.
17.         if response, err := client.RemarkGlobalRrSet(request); err == nil {
18.             fmt.Println(response.RequestId)
19.         }
20.     }
21. }
1. from aliyunsdkcore.client import AcsClient
2. from aliyunsdkcore.profile import region_provider
3. from aliyunsdkcore.acs_exception.exceptions import ClientException
4. from aliyunsdkcore.acs_exception.exceptions import ServerException
5. from aliyunsdkgenesisdns.request.v20180925 import RemarkGlobalRrSetRequest
7. client = AcsClient("{ak}", "{secret}", "{regionid}")
9. request = RemarkGlobalRrSetRequest.RemarkGlobalRrSetRequest()
10. request.set_Id(165)
11. request.set_Remark("test remark python")
12. region_provider.modify_point("GenesisDns", "{regionid}", "{endpoint}")
13. try:
14.     response = client.do_action_with_exception(request)
15.     print(response)
16. except ServerException as e:
17.     print(e)
18. except ClientException as e:
19.     print(e)
```

```
1. public static void main(String[] args) {
2.     DefaultProfile profile = DefaultProfile.getProfile("{regionid}","{ak}", "{secret}");
3.     IAcsClient client = new DefaultAcsClient(profile);
4.     RemarkGlobalRrSetRequest request = new RemarkGlobalRrSetRequest();
5.     try {
6.         request.setEndpoint("{endpoint}");
7.         request.setConnectTimeout(1000);
8.         request.setReadTimeout(1000);
9.         request.setId(Long.parseLong("165"));
10.         request.setRemark("test java remark");
11.
12.         RemarkGlobalRrSetResponse response = client.getAcsResponse(request);
13.         System.out.println(JSON.toJSONString(response));
14.     } catch (Exception ex) {
15.         System.out.println(ex.getMessage());
16.     }
17. }
```
