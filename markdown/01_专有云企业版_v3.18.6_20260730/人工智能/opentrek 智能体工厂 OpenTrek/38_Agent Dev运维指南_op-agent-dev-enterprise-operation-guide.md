---
title: "智能体工厂 OpenTrek Agent Dev运维指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 82
source_pdf: "38_Agent Dev运维指南_op-agent-dev-enterprise-operation-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/opentrek/zh/op-agent-dev-enterprise-operation-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 智能体工厂 OpenTrek Agent Dev运维指南

智能体工厂 OpenTrek 维简介

## 运维简介

阿里云OpenTrek Agent Dev依托于云原生技术和AIGC技术，基于K8S构建，如果您具备基本的Linux经验和K8s的基本运维经验，便能够轻松上手敏捷版的基础运维，并能够快速入门。本文介绍OpenTrek Agent Dev的运维目的、要求、注意事项和寻求帮助的方式。 智能体工厂 OpenTrek

## 查看监控大盘

**管控侧**

登录ASO-云平台监控大盘-OpenTrek Agent Dev监控大盘

**K8s集群Node监控大盘**

单击集群Node监控大盘，可分节点查看CPU、内存、磁盘、IO、网络等指标智能体工厂 OpenTrek

**K8s集群Pod监控大盘**

单击集群Pod监控大盘，可分Pod查看CPU、内存、重启次数等指标

**Java应用监控大盘**

单击基础监控大盘，可分应用分Pod查看HTTP、JVM、Dubbo等指标智能体工厂 OpenTrek

**Python应用监控大盘**

单击基础监控大盘（Python），可分应用分Pod查看HTTP等指标

**Go应用（gin框架）监控大盘**

单击基础监控大盘（Go-gin），可分应用分Pod查看HTTP、Go heap、Goroute等指标智能体工厂 OpenTrek

**Go应用（arrow框架）监控大盘**

单击基础监控大盘（Go-arrow），可分应用分Pod查看HTTP、Go heap、Goroute等指标

**租户侧**

进入OpenTrek Agent Dev-全局资源管理-找到ACK集群名称进入Prometheus监控 2.0-Grafana大盘-单击目录sfm-找到对应集群的大盘智能体工厂 OpenTrek

**K8s集群Node监控大盘**

单击大盘sfm-tenant-cluster-node-dashboard，可查看CPU、内存、磁盘、IO、网络等指标智能体工厂 OpenTrek

**K8s集群Pod监控大盘**

单击大盘sfm-tenant-cluster-pod-dashboard，可分空间分Pod查看CPU、内存、重启次数等指标

**Java应用监控大盘**

单击大盘sfm-tenant-basic-java-dashboard，可分应用分Pod查看HTTP、JVM、Dubbo等指标智能体工厂 OpenTrek

**Go应用（gin框架）监控大盘**

单击大盘sfm-tenant-basic-go-gin-dashboard，可分应用分Pod查看HTTP、Go heap、Goroute等指标

**Go应用（arrow框架）监控大盘**

单击大盘sfm-tenant-basic-go-arrow-dashboard，可分应用分Pod查看HTTP、Go heap、Goroute等指标智能体工厂 OpenTrek 智能体工厂 OpenTrek

## 查看告警通知

**管控侧**

**告警查看**

登录ASO进入，监控告警-告警列表页，在资源归属下拉框，选择sfm即可查看OpenTrek Agent Dev的告警。

**告警规则**

监控告警-告警规则页面，高级筛选云产品的下拉框选择sfm查看告警规则的配置。 点击自定义变更后可以对该告警配置进行变更。 智能体工厂 OpenTrek

**告警通知配置**

在监控告警-告警设置-策略管理页面，添加联系人配置告警通知人，产品选择sfm。 在监控告警-告警设置-告警通知页面，对告警进行订阅

**租户侧**

进入Prometheus监控 2.0

**告警规则**

OpenTrek Agent Dev的告警规则标签均为SfmAlertRule，可以基于此过滤智能体工厂 OpenTrek 基于当前状态可以过滤出正在告警的规则

**告警通知配置**

基于标签SfmAlertRule，过滤出所有的OpenTrek Agent Dev告警规则将分页大小调至100，全选规则，点击配置通知方式智能体工厂 OpenTrek 智能体工厂 OpenTrek

## 常见问题排查

本文档介绍OpenTrek Agent Dev平台运行过程中常见问题的排查，详见个模块中心的问题排查清单。

### 智能体

#### 智能体问题排查手册

**智能体全链路进度查询**

**前提**

数据库查询——针对是智能体的业务库 ibp_system;(项目交付一般是polardb) 日志查询——针对是智能体的应用 ibp-agent-platform;(租户区应用,日志目录 /home/admin/logs/) 获取具体的sessionId、requestId、以及请求时间正常可以咨询调用方获取,响应体中会携带; `--` 如果只有`sessionId` `--` 可以通过下述语句对比调用的时间戳 `--` 得到预期的`requestId (index_name_5)` 以及 `gmt_create (`请求时间用于日志查询)

```
select gmt_create,index_name_5 from ibp_task where index_name_7 = '具体的sessionId';
```

`--` 确定`session_code` 是否真的创建成功

```
select * from ibp_agent_session where session_code like '111%'
```

`--` 确定`session_code` 对应的历史问答

```
select * from ibp_agent_cmd_message where session_id like '111%'
```

**数据库方案SQL**

**查询任务数据**

智能体工厂 OpenTrek `--` 查询任务执行过程; `-- index_name_1` 标识具体的任务执行结果,重点关注 `FAILED` 的场景; `-- index_name_2` 标识具体的任务类型,也就是画布左侧的节点类型 `-- index_name_2='LogTsak'` 标识第一步产生的任务 `-- index_name_2='UiTask'` 标识最后一步产生的任务 `--` 通过两两之间 `gmt_create`可以大致评估各个节点执行的耗时 `--` 通过`UiTask` 比对 `LogTsak`的 `gmt_create`可以评估整个完整文答的耗时 `-- CAST(feature AS JSON)->> 'startTime' API`相关的开始执行时间 `-- CAST(feature AS JSON)->> 'endTime' API`相关的执行结束时间 `-- unique_code` 标识任务`ID`

```
select * from ibp_task where index_name_7 = '具体的sessionId' order by id desc;
```

`--` 如果某次`sessionId`发起过多次请求,需要增加条件 `index_name_5 = '`具体的`requestId'` `--` 如果`index_name_2 = 'AgentInvocationTask'` 标识子智能体任务 `--` 需要获取子智能体任务当时的 `sessionId` 进一步递归排查

```
select CAST(feature AS JSON) ->> 'CHILD_INFO' from "ibp_task" where index_name_2 = 'AgentInvocationTask'
```

`and unique_code = '`第一步得出的任务ID'; `//` 某些异常场景,无法正常记录的,可以通过日志查询匹配关键字获取

```
select content from "ibp_record" where title like '入参打印%'
```

`and task_unique_code = '`第一步得出的任务ID';

**查询执行进度数据**

`--` 将日志按照任务、创建时间升序组合进行展示 `--` 可以观察到某一条任务的执行过程和执行时间差 `--` 重点关注 `{"recordLoggingStatus":"error"}` 相关的`content`信息 `--` 如果某次`sessionId`发起过多次请求,需要增加条件 `index_name_5 = '`具体的`requestId'`

```
select * from ibp_record where task_unique_code in (select unique_code as task_id
 from ibp_task where index_name_7 = '具体的sessionId')
order by task_unique_code,gmt_create asc;
```

**日志方案**

**分析某次requestId的耗时**

智能体工厂 OpenTrek '时耗`requestId'`中的 `requestId` 需要替换为真正的`requestId`数据; `--` 实时输出的日志中查询某次`requestId`的进度

```bash
kubectl get pods -A -o jsonpath='{range .items[*]} {.metadata.namespace}/{.metadata.name}{"\n"}{end}' | grep ibp-agent | while IFS=/ read -r ns pod; do
    echo "Processing $ns/$pod" >&2
    kubectl exec -n "$ns" "$pod" -- bash -c 'cat /home/admin/logs/ibp-agent.log 2>&1 |
grep --line-buffered "时耗requestId" 2>/dev/null' done > output1.log 2>&1
```

`--` 历史的日志中查询某次`requestId`的进度

```bash
kubectl get pods -A -o jsonpath='{range .items[*]} {.metadata.namespace}/{.metadata.name}{"\n"}{end}' | grep ibp-agent | while IFS=/ read -r ns pod; do
    echo "Processing $ns/$pod" >&2
    kubectl exec -n "$ns" "$pod" -- bash -c 'zcat /home/admin/logs/ibp-agent.log.2025*
2>&1 | grep --line-buffered "时耗requestId" 2>/dev/null' done > output1.log 2>&1
```

**分析某次requestId的异常**

咨询调用方获取响应体中会携带的异常信息; '异常描述' 需要替换为现场具体的异常信息; `--` 实时输出的日志中查询某次`requestId`的进度

```bash
kubectl get pods -A -o jsonpath='{range .items[*]} {.metadata.namespace}/{.metadata.name}{"\n"}{end}' | grep ibp-agent | while IFS=/ read -r ns pod; do
    echo "Processing $ns/$pod" >&2
    kubectl exec -n "$ns" "$pod" -- bash -c 'cat /home/admin/logs/ibp-agent.log 2>&1 |
grep --line-buffered -C 200 "异常描述" 2>/dev/null' done > output1.log 2>&1
```

`--` 历史的日志中查询某次`requestId`的进度 `--` 可以调整下述值 `.*` 为具体的时间点,比如 `ibp-agent.log.2025-05-08.*`

```bash
-- /home/admin/logs/ibp-agent.log.* kubectl get pods -A -o jsonpath='{range .items[*]} {.metadata.namespace}/{.metadata.name}{"\n"}{end}' | grep ibp-agent | while IFS=/ read -r ns pod; do
    echo "Processing $ns/$pod" >&2
    kubectl exec -n "$ns" "$pod" -- bash -c 'zcat /home/admin/logs/ibp-agent.log.* 2>&1
| grep --line-buffered -C 200 "异常描述" 2>/dev/null'
done > output1.log 2>&1 llmConsumeStream, sessionId=7d84076b-42eb-47b8-abe4-89c33b2489fd, cat agent.log | grep 'llmConsumeStream' | grep sessionId | grep node_id
```

**智能体维度一些流量统计(项目现场定开能力需自建只读库)**

-- 天维度智能体工厂 OpenTrek YYYYMMDD -- 小时维度 YYYYMMDDHH24 -- 分钟维度 YYYYMMDDHH24MI

**会话创建请求数**

`--` 创建`session` 总数

```
select count(*) from ibp_agent_session;
```

`--` 活跃`session` 总数(新增或者发起了新请求`),`天维度统计

```
SELECT
    TO_CHAR(gmt_modified, 'YYYYMMDD') AS days,
    COUNT(*)
FROM
    ibp_agent_session
WHERE
    gmt_modified > '2025-01-15 08:00:00'
GROUP BY
    TO_CHAR(gmt_modified, 'YYYYMMDD')
ORDER BY
    days;
```

**发起请求数**

`--` 调用智能体发起请求数; 表数据量会很大;

```
select COUNT(*) from "ibp_task" where index_name_2 = 'LogTask' ;
```

`--` 天维度统计

```
SELECT
    TO_CHAR(gmt_create, 'YYYYMMDD') AS days,
    COUNT(*)
FROM
    ibp_task
WHERE
    index_name_2 = 'LogTask' and gmt_create > '2025-01-15 08:00:00'
GROUP BY
    TO_CHAR(gmt_create, 'YYYYMMDD')
ORDER BY
    days;
```

**智能体维度流量统计**

`--` 填充 `gmt_create`区间 `--` 填充 `agent_code` 和 `agent_version` 设置智能体具体版本

```
SELECT
    TO_CHAR(gmt_create, 'YYYYMMDD') AS days,
    COUNT(*)
FROM
    (SELECT a.index_name_5,b."agent_code" ,b."agent_version",a.gmt_create
```

智能体工厂 OpenTrek

```
     FROM "ibp_task" a LEFT JOIN "ibp_agent_session"  b on a.index_name_7 =
b.session_code
     where a.index_name_2 = 'LogTask' and b.agent_code = '' and b.agent_version =''
    ) m
WHERE
    gmt_create > '' and  gmt_create < ''
GROUP BY
    TO_CHAR(gmt_create, 'YYYYMMDD')
ORDER BY
    days;
```

`--` 样例- 统计`2025-05-01` 之后每个智能体维度每天的调用量

```
select
  h."agent_name",
  n.*
from
  (
    SELECT
      agent_code,
      TO_CHAR(gmt_create, 'YYYYMMDD') AS days,
      COUNT(*) as number
    FROM
      (
        SELECT
          b.agent_code,
          b.agent_version,
          a.gmt_create
        FROM
          (
            select
```

*

```
            from
              "ibp_task"
            where
              index_name_2 = 'LogTask'
              and gmt_create > '2025-05-01 00:00:00'
          ) a
          LEFT JOIN "ibp_agent_session" b on a.index_name_7 = b.session_code
      ) m
    GROUP BY
      TO_CHAR(gmt_create, 'YYYYMMDD'),
      agent_code
    ORDER BY
      days desc,
      number desc
  ) n
  LEFT JOIN "ibp_agent_ref" h on n."agent_code" = h."agent_code"
```

**智能体请求维度内存占用**

智能体工厂 OpenTrek `--` 返回字段含义: 任务类型、`sessionId`、`requestId`、任务数据占用磁盘大小 `--` 返回条件: 指定时间范围内任务数据占用磁盘超过`1MB`的数据

```
SELECT
  index_name_2,index_name_7,index_name_5,
  pg_column_size(feature) AS size_bytes,
  ROUND(pg_column_size(feature) / 1024.0 / 1024.0, 2)
FROM ibp_task WHERE gmt_create > '2025-10-20 21:16:00' and pg_column_size(feature) > 1024 * 1024 ORDER BY size_bytes DESC;
```

**发起大模型节点任务调用数**

`--` 全平台

```
SELECT
    TO_CHAR(gmt_create, 'YYYYMMDD') AS days,
    COUNT(*)
FROM
    ibp_task
WHERE
    gmt_create > '2025-01-15 08:00:00' and index_name_2 = 'LLMReasoningTask'
GROUP BY
    TO_CHAR(gmt_create, 'YYYYMMDD')
ORDER BY
    days;
```

`--` 单个智能体w维度

```
SELECT
    TO_CHAR(gmt_create, 'YYYYMMDD') AS days,
    COUNT(*)
FROM
    (SELECT a.index_name_5,b."agent_code" ,b."agent_version",a.gmt_create
     FROM "ibp_task" a LEFT JOIN "ibp_agent_session"  b
     on a.index_name_7 = b.session_code
     and a.index_name_2 = 'LLMReasoningTask'
     and b.agent_code = '' and b.agent_version =''
    ) m
WHERE
    gmt_create > '' and  gmt_create < ''
GROUP BY
    TO_CHAR(gmt_create, 'YYYYMMDD')
ORDER BY
    days;
```

`--` 配置了哪些大模型

```
select distinct(a.modelCode) from ( SELECT CAST(node_config AS JSON) -> 'config' ->> 'modelCode' as modelCode from ibp_con fig_node where node_action = 'LLM' and node_config like '%modelCode%') a ;
```

智能体工厂 OpenTrek

**发起其他外部服务节点任务调用数(API\RAG\KC)**

```
SELECT
    TO_CHAR(gmt_create, 'YYYYMMDD') AS days,(CAST(feature AS JSON)->>
'custom_tool_type') AS toolType,
    COUNT(*)
FROM
    ibp_task
WHERE
    gmt_create > '2025-01-15 08:00:00' and index_name_2 = 'ToolInvocationTask'
GROUP BY
    TO_CHAR(gmt_create, 'YYYYMMDD'),CAST(feature AS JSON)->> 'custom_tool_type'
ORDER BY
    days;
```

**JAVA程序堆栈相关**

**虚拟线程堆栈**

下述脚本会dump虚拟线程堆栈，并合并重复堆栈，只保留线程名称，下面内容复制到环境中后用python 运行，结果会输出到 `/home/admin/stack_analyzed.log` 1、进入 `agent`对应的pod;

```
cd /home/admin vi javastack.py
```

2、执行

```
su admin /usr/local/bin/python3 javastack.py
```

3、将下述文件`copy`回来

```java
/home/admin/stack_analyzed.log from collections import OrderedDict import subprocess import os def get_java_pid():
```

# 执行 `ps -ef | grep java` 命令并获取结果

```
    try:
        result = subprocess.run(["ps", "-ef"], capture_output=True, text=True)
        processes = result.stdout.splitlines()
```

# 找到 `java` 进程的第一行

```python
        for line in processes:
            if "java" in line and "grep" not in line:
                return line.split()[1], line.split()[7]
    except Exception as e:
        print(f"Error occurred while getting Java PID: {e}")
    return None, None
```

智能体工厂 OpenTrek

```python
def dump_thread_stack(pid, jdk_bin, stack_file):
    try:
        command = [
            os.path.join(jdk_bin, "jcmd"),
            pid,
            "Thread.dump_to_file",
            "-format=text",
            "-overwrite",
            stack_file,
```

]
# 执行 `jcmd` 命令

```python
        subprocess.run(command)
        print(f"Thread stack dumped to {stack_file}")
    except Exception as e:
        print(f"Error occurred while dumping thread stack: {e}")
def main():
    stack_file = "/home/admin/stack.log"
    pid, java_exec = get_java_pid()
    if pid and java_exec:
        jdk_bin = os.path.dirname(java_exec)
        dump_thread_stack(pid, jdk_bin, stack_file)
    else:
        print("No Java process found.")
        return
    stacks = OrderedDict()
    with open(stack_file) as f:
        content = f.read()
        blocks = content.split("\n\n")
        for block in blocks:
            if not block.startswith("#"):
                continue
            split = block.split("\n", 1)
            thread = split[0]
            if len(split) <= 1:
                continue
            stack = split[1]
            if stack not in stacks:
                stacks[stack] = []
            stacks[stack].append(thread)
    stacks = OrderedDict(
        sorted(stacks.items(), key=lambda item: len(item[1]), reverse=True)
```

)

```
    result = ""
    for stack in stacks:
        result += (
```

智能体工厂 OpenTrek

```
esut (
            str(len(stacks[stack])) + " in total, " + " , ".join(stacks[stack]) + "\n"
```

)

```python
        result += stack + "\n\n"
    result_file = "/home/admin/stack_analyzed.log"
    with open(result_file, "w") as f:
        f.write(result)
    print(f"Thread stack analysis completed. Please check {result_file} for details.")
if __name__ == "__main__":
    main()
```

**jstack堆栈**

如下获取 pid; `--` 替换真实`pid`后,执行下述命令,将`agent.dump`传回来

```
/opt/graalvm/bin/jstack pid > agent.dump
```

**运维数据库情况**

**查看超大字段存储**

```
SELECT
    id,
    feature, index_name_2, name,
    pg_column_size(feature) AS column_size_bytes,
    (pg_column_size(feature) / 1024) AS column_size_kb
FROM
    ibp_task
WHERE
    gmt_create > '2025-09-08 00:00:00' and
    pg_column_size(feature) > 500 * 1024
ORDER BY
    column_size_kb DESC;
```

**查看数据库连接占用情况**

```
SELECT
    datname AS database_name,         -- 数据库名称
    COUNT(*) AS connection_count      -- 连接数
FROM pg_stat_activity GROUP BY datname ORDER BY connection_count DESC;
```

**查看数据库实时运行情况**

智能体工厂 OpenTrek

```
SELECT
    datname AS database_name,         -- 数据库名称
    pid,                            -- 进程 ID
    usename AS user_name,           -- 用户名
    application_name,               -- 应用程序名称
    client_addr AS client_address,  -- 客户端 IP 地址
    state,                          -- 当前状态 (active, idle, 等)
```

`query --` 当前执行的 `SQL` 查询

```
FROM pg_stat_activity WHERE state = 'active';
```

**业务数据情况**

**查看待调度的任务数量**

```
select count(*) from ibp_task where "index_name_11" = '0' and "index_name_2" in ('CustomerSupportTask','ToolInvocationTask','AgentInvocationTask');
```

**查看某次会话执行情况**

`--` 查询某次会话请求下的任务数据 `--` 任务类型、任务名称、任务结果、任务执行状态、是否被调度过、(时间相关参数)、执行入参数

```
select "index_name_2","name","index_name_1","index_name_9","index_name_11",
  "gmt_create" ,"gmt_modified" ,
  CAST(feature AS JSON)->> 'toolExecuteStartTime',CAST(feature AS JSON)->>
'toolExecuteEndTime',
  CAST(feature AS JSON)->> 'startTime',CAST(feature AS JSON)->> 'endTime',
  feature
from "ibp_task" WHERE index_name_7 = '真实的sessionId' and index_name_5 = '真实的requestI
```

`d'`

```
order by "gmt_create" desc; select "index_name_2","name","index_name_1","index_name_9","index_name_11",
  "gmt_create" ,"gmt_modified"
from "ibp_task" WHERE index_name_7 = '真实的sessionId' and index_name_5 = '真实的requestI
```

`d'`

```
order by "gmt_create" desc;
```

`--` 降序排列,比较每条记录之间的 `"gmt_create",`可以大概评估前序节点耗时(流式场景除外)

**数据积压情况**

智能体工厂 OpenTrek `--` 智能体会话相关大表数据量查询

```
select count(*) from ibp_task where gmt_create < '2025-12-16 10:33:39.559'; select count(*) from ibp_record where gmt_create < '2025-12-16 10:33:39.559'; select count(*) from ibp_agent_cmd_message icm where gmt_create < '2025-12-16 10:33:39 .559'; select count(*) from ibp_agent_stream_thougths iast where gmt_create < '2025-12-16 10 :33:39.559'; select count(*) from ibp_agent_memory_fragment iamf where gmt_create < '2025-12-16 1 0:33:39.559';
```

`--` 表容量使用情况查询`(PG`库)

```
SELECT
    schemaname AS table_schema,
    relname AS table_name,
    pg_total_relation_size(relid) / (1024.0 * 1024) AS total_size_mb
FROM
    pg_stat_user_tables
WHERE
    schemaname = 'public'
ORDER BY
    total_size_mb DESC;
```

`--` 表容量使用情况查询`(MYSQL)`

```
SELECT
    TABLE_NAME,
    TABLE_SCHEMA,
    ROUND((DATA_LENGTH + INDEX_LENGTH) / 1024 / 1024, 2) AS Total_Size_MB
FROM
    information_schema.TABLES
WHERE
    TABLE_SCHEMA = 'ibp_system'
ORDER BY
    Total_Size_MB DESC;
```

**效果追踪相关表字段说明**

**问答记录表**

**表说明**

ibp_agent_cmd_message 记录每次会话的问答

| session id _ | 会话ID |
|---|---|
| request id _ | 请求ID |
| from id _ | 来源, 智能体回复场景 from id=session id _ _ |

智能体工厂 OpenTrek

| to id _ | 目标, 智能体提问场景 to id=session id _ _ |
|---|---|
| message | 提问内容/回复内容 |

**相关SQL**

```xml
    select *
    from ibp_agent_cmd_message
    <where>
      <if test="requestId != null">
        request_id = #{requestId}
      </if>
      <if test="requestId == null">
        <if test="sessionId != null">
          session_id = #{sessionId}
        </if>
        <if test="sessionId == null">
          session_id in (
          SELECT session_code  FROM ibp_agent_session
          WHERE agent_code =  #{agentCode}
          <if test="agentVersion != null">
            and agent_version = #{agentVersion}
          </if>
          order by id desc
          limit 100
```

)

```
        </if>
      </if>
       and (from_id != session_id or from_id is null)
       and gmt_create > #{endDate}
    </where>
    order by gmt_create desc
    limit #{pageIndex},#{pageSize}
```

**任务详情**

**表说明**

ibp_task 记录每个节点创建的任务信息,以及任务执行调用信息智能体工厂 OpenTrek

```json
{
  "unique_code":""
 "index_name_1":"result",     //执行结果
```

`"index_name_2":"taskType", //` 任务类型,以 `LogTask` 开始以 `UiTask`结束

```json
 "index_name_3":"batchNo",
  "index_name_4":"debug",
  "index_name_5":"requestId",
 "index_name_6":"name",
 "index_name_7":"sessionId",
  "index_name_8":"title",       //任务名称
 "index_name_9":"status",     // 执行状态
 "index_name_10":"env",       //环境标
 "index_name_11":"isFire",    // 是否被调度
 "index_name_12":"breakPoint" // 断点标
```

`"feature":"" //` 扩展字段(包含入出参)

```
}
```

`LogTask:` 日志任务 `LLMReasoningTask:`大模型任务, `ScriptInvocationTask:`脚本任务, `ToolInvocationTask:`工具任务, `AgentInvocationTask:`智能体任务,

```
    //CONSIDER_TASK("ConsiderTask","规划任务"),
```

`CustomerSupportTask:`通用异步任务

```
    //OBSERVATION_TASK("ObservationTask", "结果观察任务"),
```

`//INVISIBLE_TASK("InvisibleTask", "`前端不可见任务`"),` `UiTask:` 结果渲染任务

**系统日志**

数据表 ibp_record

**思考过程**

数据表 ibp_agent_stream_thougths

#### 智能体节点执行失败

如智能体工厂 OpenTrek 可以从中间画布红点分辨那个节点报错，返回信息或者右侧的ErrorMessage中获取到节点的具体报错， 然后返回到设计页面去编辑修改报错的节点。 如果是api调用，可以在版本页面点击效果跟踪智能体工厂 OpenTrek 然后根据sessionId 和 requestId 来进入任务详情和系统日志来查看具体问题

### 数据中心

#### 数据集管理

##### 数据集列表

1. .** **数据集列表出现**“**请联系运维管理员，前往资源管理**>**全局服务管理中，创建检**

**索与解析服务并分配空间”报错**

问题描述：数据集列表出现“请联系运维管理员，前往资源管理>全局服务管理中，创建检索与解析服务并分配空间”报错。 问题原因：没有为当前空间分配数据集所需的存储资源。 智能体工厂 OpenTrek 解决方法：以运维管理员身份进入资源管理，将资源分配给当前指定空间。
2. .** **上传文件并构建了新子集后，数据集列表页显示行数**/**大小未变化**
问题原因：数据集列表上的数据集统计信息每1小时更新一次；且统计行数及大小均为子集大小，不包含原始文件。 解决方法：更新1小时后重新查看列表页信息。

##### 数据文件

本文为您介绍在使用数据文件功能时遇到的告警问题现象、可能原因及解决方案。
1. .** **上传文件出现****CROS****跨域报错**
问题描述：通过数据集-数据文件进行文件上传到OSS时，无法成功上传文件。控制台提示CROS跨域错误。 解决方法：登录OSS控制台-跨域设置，添加如下跨域规则
2. .** **上传文件出现** `This request has content must be served over HTTPS` **错误**
问题描述：通过数据集-数据文件进行文件上传时，无法成功上传文件。控制台提示 `This request has` `content must be served over HTTPS` 错误，如下： 问题原因：使用的对象存储未开启HTTPS访问导致解决方法：进入OSS控制台检查Bucket授权策略中是否开启仅HTTP可访问，切换至HTTPS或不进行限定； 检查资源管理中对象存储资源的访问协议是否配置为HTTP，切换至HTTPS访问协议。
3. .** **使用临时凭证上传文件提示****“The OSS Access Key Id you provided**

**does not exist in our records”错误**

问题描述：通过数据集OPENAPI获取数据集的上传凭证进行文件上传时，出现“The OSS Access Key Id you provided does not exist in our records”错误。 问题原因：临时访问凭证已过期，过期后自动失效。 智能体工厂 OpenTrek 解决方法：通过获取临时凭证接口返回的过期时间，在临时凭证过期前重新获取并更新凭证。
4. .** **使用临时凭证操作数据文件时，提示****“Access denied by authorizer's**

**policy”错误**

问题描述：通过数据集OPENAPI获取数据集上传/下载临时凭证后，进行数据文件操作时，提示“Access denied by authorizer's policy”错误。 问题原因：上传凭证仅提供对应数据集目录下的上传动作，下载凭证仅提供对应数据集目录下的下载动作。 当操作范围超过限制时提示上述错误，如使用上传凭证进行下载/删除动作、使用上传凭证将文件上传至数据集外的其他路径等解决方法： 若需要进行上传，使用上传凭证完成对应数据集目录下的上传动作若需要进行下载，使用下载凭证完成对应数据集目录下的下载动作若需要进行删除，调用数据集OPENAPI进行数据文件的删除动作
5. .** **删除文件出现** `403 Forbidden` **错误**
问题描述：在数据集-数据文件中可正常上传并查看文件，但点击删除时提示 `403 Forbidden` 。 问题原因：对象存储OSS的角色授权中未进行删除权限授权。 解决方法：在资源管理中确认使用的对象存储资源及配置的角色，通过OSS控制台为该角色增加 `DeleteObject` 权限。

##### 数据子集

本文为您介绍在使用数据子集功能时遇到的告警问题现象、可能原因及解决方案。
1. .** **创建**/**更新子集提示构建失败，提示****“No found any file types match**

**supported type”错误**

问题描述：创建子集提示构建失败，提示“No found any file types match supported type”错误。 问题原因： 选中用于创建子集的文件不在可识别的文件类型列表。 未正确配置通配符，无法匹配到目标数据文件。 解决方法： 若选中用于创建子集的文件不在可识别的文件类型列表，需要将其转换为可识别的文件类型。 若以通配符进行文件选择，可在配置完成后，点击创建子集页面的文件预览按钮，若编写正确则会展示前 100条匹配的数据文件，基于预览文件确认是否符合预期。
2. .** **创建**/**更新子集提示构建失败，提示****“Found multi file modal in your**

**paths”错误**

问题描述：创建/更新子集提示构建失败，提示“Found multi file modal in your paths”错误。 问题原因：数据子集的数据文件配置时，同时选中多种模态的文件。 解决方法：依据错误提示中的信息，仅保留一种模态的数据文件。
3. .** **进行子集数据预览时，提示视图分页数据过大，无法预览**
问题描述：进行子集数据预览时，提示视图分页数据过大，无法预览。 问题原因：加载子集分页所在的数据块时，超过了单次查询128MB内存限制，其中默认1000行数据划分为 1个数据块。 解决方法：拆解大字段为多个小字段或多行数据。 智能体工厂 OpenTrek
4. .** **无法进行新建**/**更新子集操作**
问题描述：打开目标数据集后，新建/更新子集按钮均置灰，无法进行新建/更新子集操作。 问题原因：仅数据集创建者及空间管理员具备子集修改权限解决方法：授权空间管理员角色

#### 数据加工

##### 知识库解析服务创建

1. .** **创建在线服务**
以下操作和用户创建在线解析服务链路相同：

**1.1. 基础信息**

开启镜像部署（无需选择模型）： 智能体工厂 OpenTrek

**1.2. 选择资源组**

如果用到文档深度解析，需要选择带智算设备的资源池。这里以基础解析为例进行演示：

**1.3. 选择服务镜像**

（正式环境可从公共镜像选择），基础解析对应CPU镜像，深度解析对应GPU镜像：

**企业版镜像名称为：**

nvidia-dke-online-parser:cuda12.6-ubuntu22.04-py3.10-v3.0 cpu-dke-online-parser:ubuntu22.04-py3.10-v3.0 apg-dke-online-parser:cuda12.6-ubuntu22.04-py3.10-v3.0 ascend-dke-online-parser:cuda12.6-ubuntu22.04-py3.10-v3.0 智能体工厂 OpenTrek dcu-dke-online-parser:cuda12.6-ubuntu22.04-py3.10-v3.0

**测试可使用自定义镜像：**

**1.4. 服务配置**

经典网络：必开，选择AI智能网关可忽略端口：Service端口、容器端口，按下图填写启动命令：按下图填写环境变量：按下图填写，SERVER_WORKERS 表示推理并行能力，根据资源配置进行调整更多配置参数：

| 环境变量 | 描述 | 推荐配置 | 设置值 |
|---|---|---|---|
| SERVER WORKERS _ | worker数量（请求最大并发数） | 8 | 8 |
| SERVER PORT _ | 服务端口号 | 8001 |  |

智能体工厂 OpenTrek

| RUNTIME SHARE PAT _ _ H | 日志/产物保存路径 | /runtime share _ | /runtime share _ |
|---|---|---|---|
| START TRITON SERVE _ _ R | 是否启动tritonserver | 1 | 1 |

**1.5. 【可选】高级配置**

开启异步推理，支持 Kafka 管理请求队列，持久化解析结果：

**1.6. 创建成功**

点击确认后，会看到服务列表中新增一条记录： 等待部署成功：

**1.7. 绑定ApiKey**

创建 ApiKey（最好不要用 admin 账号）。 智能体工厂 OpenTrek 给服务绑定这个apikey：

### 1.8. 模型接入

在线服务启动后，需要去 op 管理页面进行接入，才可以被使用。 使用创建 API Key 的用户，切换“资源管理员”角色，进入op页面： 智能体工厂 OpenTrek 点击“接入模型”，选择模型服务，类型选择“在线解析服务”，选择刚绑定的 ApiKey，可以选择全部空间共享。 智能体工厂 OpenTrek 创建成功后进行调试，返回正常后，点击“调试通过”，使其变绿： 回到列表页，点击启用，才可以在知识库被选到：

###### 自定义镜像上传

**上传镜像**

专有云 ACR 需要自己在测试的资源集下创建仓库，密码自行修改（一般用 AliOS%1688）： 智能体工厂 OpenTrek
# mac上传本地镜像到远端

```
podman push reg.docker.alibaba-inc.com/dke/data-mixer-operators:2.1.1-hotx.3-cpu-1031-r elease --creds=ascm-org-1756263186183:AliOS%1688 --tls-verify=false docker://cr-ee.regi stry.cn-wulan-env38g1-d02.inter.env223.shuguang.com/dke/data-mixer-operators:2.1.1-hotx .3-cpu-1031-release
```

# linux/windows使用`skopeo`命令

```
skopeo copy \
  --src-tls-verify=false \
  --src-creds chihou.wc:chihou@aliyun \
  docker://reg.docker.alibaba-inc.com/dke/data-mixer-operators:2.1.1-hotx.3-gpu-1110-re
lease \
  docker://cr-ee.registry.cn-wulan-env17e-
d01.inter.env17e.shuguang.com/aipaas_test/data-mixer-operators:2.1.1-hotx.3-gpu-1110-re lease \
  --dest-creds ascm-org-1760067243940:AliOS%1688 \
  --dest-tls-verify=false
```

注意：新推的镜像也要手动增加版本。

###### AI 网关创建指南

**创建集群**

https://one.console.con.env17e.shuguang.com/cop/gateway 智能体工厂 OpenTrek 注意一下两点：

**创建 AI Gateway**

我配置的时候保存报错了，但是最后成功了。。 智能体工厂 OpenTrek

**配置 AI Gateway**

绑定新配置的网关实例即可

###### Kafka 及 Topic 创建指南

**创建kafka实例**

先找到ai-gateway所在集群的vpc网络id，记录下来： 开启异步推理时，会提示交换机id，记录下来： 智能体工厂 OpenTrek 创建kafka实例，如下填写，使用上面的vpc/vsw： 智能体工厂 OpenTrek

**创建SASL用户和权限**

创建用户：aistudio / Admin123@ascm 智能体工厂 OpenTrek 创建ACL权限(3个)： 智能体工厂 OpenTrek

**创建分区**

###### 创建 VLM 推理服务

**创建服务**

Step0. 先去 MaaS 市场下载模型（按需下载，本文以 Qwen2.5 为例），搜索 `Qwen2.5-VL-7B-`

```
Instruct ：
```

智能体工厂 OpenTrek Step1. 新建在线服务，资源选择 16c64g + 64g共享内存 + 1卡（A10/A100） Step2. 选择镜像（nvidia-vllm-lws）： Step3. 选择模型 `Qwen2.5-VL-7B-Instruct` ，挂载路径 `/models/Qwen2.5-VL-7B-Instruct` ： Step4. 开启经典网络，不开经典网络就要开AI网关，否则没法调用： Step5. 配置端口和启动命令，容器端口 8000，启动命令（ `--tensor-parallel-size` 等于卡数）： 智能体工厂 OpenTrek

```
python3 -m vllm.entrypoints.openai.api_server --max_num_batched_tokens 65536 --dtype bf loat16 --gpu-memory-utilization 0.9 --tensor-parallel-size 1 --trust-remote-code --serv ed-model-name Qwen2.5-VL-7B-Instruct --model /models/Qwen2.5-VL-7B-Instruct --disable-c ustom-all-reduce --host 0.0.0.0 --port 8000
```

Step6. [可选]创建成功后开启 AI 网关，添加网页链接。

**模型测试**

查看调用信息，办公网使用经典网络地址访问（需要手动开启）。 智能体工厂 OpenTrek

```json
curl -X POST 'http://d4e36c8d.classic.inter.env17e.shuguang.com/v1/chat/completions' \ -H 'Authorization: Bearer sk-3daefc8d0d0b9040b7' \ -H 'Content-Type: application/json' \ -d '{
    "messages": [
        {
            "role": "user",
            "content": [
                {
```

`"text": "`哥伦布是谁`",`

```json
                    "type": "text"
                }
```

]

```
        }
```

`],`

```json
    "model": "Qwen2.5-VL-7B-Instruct",
    "temperature": 1.0,
    "top_p": 1.0,
    "presence_penalty": 0.0,
    "max_tokens": null,
    "stream": false
}'
```

智能体工厂 OpenTrek

```json
curl -X POST 'http://d4e36c8d.classic.inter.env17e.shuguang.com/v1/chat/completions' \ -H 'Authorization: Bearer sk-3daefc8d0d0b9040b7' \ -H 'Content-Type: application/json' \ -d '{
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "image_url": {
                        "url": "http://dke.oss-cn-wulan-env17e-d01-
a.inter.env17e.shuguang.com/datasets%2Ftest%2Fimage_0001.jpg? Expires=1762528157&OSSAccessKeyId=w0mbe5gdBHxX4y5r&Signature=GZFQYP%2BSwh4NHl3iA%2BWi7NCU c%3D"
                    },
                    "type": "image_url"
                },
                {
```

`"text": "`你是一个智能图像描述助手，请使用简短的语句描述图中内容。`",`

```json
                    "type": "text"
                }
```

]

```
        }
```

`],`

```json
    "model": "Qwen2.5-VL-7B-Instruct",
    "temperature": 1.0,
    "top_p": 1.0,
    "presence_penalty": 0.0,
    "max_tokens": null,
    "stream": false
}'
```

##### 知识库文档解析问题排查

**服务可用性检查**

切换为“资源集管理员”或“运维管理员”角色登录“OpenTrek Agent Dev”： 智能体工厂 OpenTrek 进入注册好的在线解析服务，点击“调试”，检查服务联通性。返回结果证明服务可用。 智能体工厂 OpenTrek

**查看服务日志**

进入“AI Studio”产品页面，进入“在线服务”，找到手动部署的在线解析服务，点击进入详情页。 查看“资源实例”页面的副本运行状态，确认是否运行正常，点击“日志”，可查看是否有报错。 智能体工厂 OpenTrek 完整日志，可进入“事件&日志”页面查询。 如果实例状态异常，可进入“事件”页面，查看 K8s 事件。

**常见问题**

1. .** **在线服务由于****OOM Kill****重启**
在线实例，由于并发过多或者是单文件较大导致解析进程 OOM 重启。可根据实际情况对服务进行变配，调整 CPU/内存/共享内存配置。推荐配置： Nvidia系列显卡：单副本 8C 32G 16G共享内存 worker=8 APG系列显卡：单副本 8C 80G 16G共享内存 worker=4 海光系列显卡：单副本 8C 80G 16G共享内存 worker=4 华为系列显卡：单副本 8C 80G 16G共享内存 worker=4 变配操作：先将服务停止，在“在线服务”列表页，找到变配服务，点击右侧“Service配置”-“资源变更” 智能体工厂 OpenTrek 在弹框中填写变更后资源配置，“确认”后，点击“重启”，等待服务启动成功。

##### 知识库解析服务镜像热更新

步骤一：将热更新镜像推送至租户侧 ACR，创建自定义镜像，添加镜像版本。参考自定义镜像上传。 步骤二：停止在线服务，点击“编辑配置” 在弹框中选择刚刚上传并添加的自定义镜像，点击页面底部“确定”。在列表页点击“重启”，等待服务启动成功。 智能体工厂 OpenTrek

##### 加工任务问题排查

1. .** **查看加工任务的运行日志**

**1.1. 打开日志页面**

首先进入任务运行总览页面，搜索任务名称（或者通过任务的运维按钮直接进入），找到对应运行实例记录，点击右侧的详情按钮。 智能体工厂 OpenTrek 切到日志Tab

**1.2. 先看任务配置：**

查询 `cfg.process is:` ，找到对应如下参数配置信息确认有哪些算子，使用了哪些参数

**1.3. 再找报错算子：**

查找 `- OP [` ，寻找哪些算子执行完成，错的是哪一步智能体工厂 OpenTrek 每一步算子完成后，都会有总结日志，包含运行时间和输出样本数量

**1.4. 再看报错详情：**

如上python 日志堆栈可查看具体的报错原因，然后根据原因去查找常见QA，无常见QA能解决，再查看算子开发，进行研发定位；
2. . PDF****来源文件转换失败造成解析失败**
日志中包含soffice 和转换失败的逻辑输入源文件无法自动转换成pdf文件进行解析；可能是文件偏大或者文件本身问题，导致无法转换； 智能体工厂 OpenTrek
3. .** **深度解析执行报错，日志报错中包含**

**expand_page_images_to_rows_mapper和**

**image_caption_backfill_selector的拼接**

[2026-01-08 16:14:58.286] 2026-01-08T16:14:58.281+08:00 | INFO | data_mixer_operators.core.data:240 - OP [expand_page_images_to_rows_mapper] Done in 1.213s. Left 192 samples. [2026-01-08 16:14:58.292] 2026-01-08T16:14:58.289+08:00 | ERROR | data_mixer_operators.utils.error_handler:44 - An error [DATA-403] <Unexpected error occurred in Op [image_caption_backfill_selector]: dict_keys(['imagePath', 'pageNumber', 'pageReadingOrder']) doesn't meet the req of ['pageNumber', 'pageReadingOrder', 'imagePath', 'imageCaption'].> occurred in operation image_caption_backfill_selector when processing sample: Dataset({ [2026-01-08 16:14:58.292] features: ['__idx', 'doc', '__dm__stats__', 'converted_doc', 'layout_analysis', '__tok... [2026-01-08 16:14:58.292] 2026-01-08T16:14:58.290+08:00 | ERROR | data_mixer_operators.core.data:244 - GLOBAL ERROR LOG: An error occurred during Op [image_caption_backfill_selector], pipeline crashed. 可观察到日志中发现执行完成**PDF****版面分析图片增强解析**-**图片解包**算子，即图中的 expand_page_images_to_rows_mapper后，直接报**PDF****版面分析图片增强解析**-**图片解析内容合并算** 子的错误，即图中的image_caption_backfill_selector的输入内容错误； 这表示用户执行链路配置不全，在深度解析链路中，需要同时配置：

**PDF版面分析图片增强解析-图片解包**

**PDF版面分析图片增强解析-图片增强服务调用**

**PDF版面分析图片增强解析-图片解析内容合并**

或者同时打开开关，或者同时删除以上三个算子； 用户有可能因为环境缺乏VLM模型的情况下，只删除PDF版面分析图片增强解析-图片增强服务调用算子的情况； 该问题，请用户删除前面三个算子即可解决；
4. .** **深度解析执行报错，日志中包含****Failed to convert document**
在pdf解析链路中，支持预置转换文件格式时报错，需要排查源文件是否格式异常；可以通过以下步骤排查
1. 先使用对应的PC应用，比如Word、Excel、Libreoffice 等打开该文件，确认文件本身打开没有问题；
2. 对文件进行另存为新文件，对比新旧文件的大小差异，如以下文档，另存为后发现文档大小有差异，标识
源文件有格式错误，已被PC应用自动修复；
3. 新文件再次进行解析的运行，可以正常运行；
4. 也可以在PC上对源文件直接另存为PDF格式文件，直接解析PDF文件；
5. .** **深度解析知识片段内容重复，解析结果中****chunkBboxs****里的数据前后知识片**

**段有重复内容**

在知识片段（chunk）的结果中，chunkBboxs的列表里出现重复内容，如以下文件的知识片段，有前后两个chunk，对应的chunkContent不一样，chunkBboxs相同； 智能体工厂 OpenTrek 对应情况是： 对应文档解析的结果中，按页解析成不同的段落作为结果列表保存对应的段落长度有长有短，长度超过用户设置的知识片段切分长度的段落，会被切成两个chunk 两个chunk的结果中，都会带上相同的chunkBboxs，用于回溯片段来源第一个知识片段内容到文本： “...死气沉沉” 第二个知识片段内容从文本： “...死气沉沉”之前，补充了overlap的token长度后，输出对应文本： 智能体工厂 OpenTrek
6. . PPU****环境：****processor running error: [500] in ensemble**

**'layout_analysis_ensemble', Stub process**

**'layout_analysis_det_0_3' is not healthy.**

结论：**PPU**比N**卡吃内存，这个错误是** **OOM** **模型进程被** **kill** **掉。推荐** **ppu-1.4.3** **至少** **70G** **内存。**

**ppu-1.5.1 至少 50G 内存。**

现象是：triton启动后前几次运行正常（99环境测试），某次运行后layout_analysis_det_0_3这个模型就一直是不健康状态。 dmesg -T 查看oom事件：

```
[五 5月 30 14:29:16 2025] triton_python_b invoked oom-killer: gfp_mask=0xcc0(GFP_KERNEL), order=0, oom_score_adj=0 [五 5月 30 14:29:16 2025] oom_kill_process.cold+0xb/0x28 [五 5月 30 14:29:16 2025] [ pid ] uid tgid total_vm rss pgtables_bytes swapent s oom_score_adj name [五 5月 30 14:29:16 2025] oom-kill:constraint=CONSTRAINT_MEMCG,nodemask=(null),cpuset=0d 3888b689ecbb71ff8e119e700b4302822812bbb6fd16dd6cb68ddb7467d944,mems_allowed=0-1,oom_mem cg=/docker/0d3888b689ecbb71ff8e119e700b4302822812bbb6fd16dd6cb68ddb7467d944,task_memcg=/d ker/0d3888b689ecbb71ff8e119e700b4302822812bbb6fd16dd6cb68ddb7467d944,task=triton_python_b id=1355052,uid=0 [五 5月 30 14:29:19 2025] oom_reaper: reaped process 1355052 (triton_python_b), now anon -rss:0kB, file-rss:0kB, shmem-rss:9896kB
```

docker启动参数配置了 8G 内存，并且开启了 mem_swap。 docker stats查看内存分配生效： 智能体工厂 OpenTrek 06.19 发现如下依赖和triton-ppu基础镜像对不齐确认后并不影响。
7. . PPU****环境：****layout_analysis.utils.element.DocException:**

**process page error: pool index 85 process time too long, cancel**

**with timeout!**

模型处理超时，降低并发：np=4 -> np=2
8. . H200****环境：****unable to enqueue for inference**

**table_cell_detect_0_1**

该链路执行日志中体现，pdf其他模型识别正常，但表格解析子模型执行报错；数据集执行结果表格解析的 chunk为空； 智能体工厂 OpenTrek 通过现场执行算法程序排查，发现镜像打包时使用的是H20的driver编译的模型文件，到现场执行表格解析报错； 通过现场直接编译模型文件的方式解决；碰到类似问题确认gpu 型号和驱动，如有必要，联系算法在现场进行模型编译，生成适配的模型文件来排除；
9. .** **解析链路下载文件失败：**
当前版本在各web服务启动了相应的referer配置，例如，oss启动了防盗链： 智能体工厂 OpenTrek 防盗链配置的地址应该与环境中使用的referer配置能够匹配；以上配置中未在inter.env*.*.com的地址上使用https协议名称，修改为带https://开头的才正常：
10. .** **常见****gpu** **模型服务启动失败，一般如果没有成功运行过，就应该是镜像打包**

**问题，需要找镜像发布者确认，并热更新镜像**

错误截图： 智能体工厂 OpenTrek

**注意：211及以下版本，报错如下错误，是因为算法内部的重启逻辑有问题，无需更新镜像，手动进入容器**

**重启即可**

正常triton的模型启动时，所有模型服务应该都为ready 状态； 模型拉起正常，没有明显报错，但是triton服务调用失败： 智能体工厂 OpenTrek 可通过 `dmesg -T` 检查是否有 oom kill 的信息： 询问算法内存需求： 按照需求调整在线服务对应 deployment 的 mem 配置为（limit+request） 50G。
12. . DCU****环境：在线解析服务调用失败**
问题同上， `dmesg -T` 可见 oom kill 信息。正常内存需求如下： 按照需求调整在线服务对应 deployment 的 mem 配置为（limit+request） 80G，有疑问联系。
13. .** **如何进入在线容器手动重启****tritonserver**
进入在线服务所在集群，master 的 `/root/.kube` 一般有 kubeconfig： 智能体工厂 OpenTrek

```
cd /root/.kube
```

# 假设是北京`A10`集群，设置`KUBECONFIG`环境变量

```
export KUBECONFIG=/root/.kube/config_A10_beijing
```

# 找到运行中的在线实例

```bash
kubectl get pod -A | grep elastic | grep Running
```

# 进入容器

```bash
kubectl exec -it -n xlm-cluster-alpqxj dke-elastic-pod-lpl4pm6l3uhn-54d8688777-k4qd8 -c server -- bash
```

`cat /home/admin/bin/start.sh` 查看trionserver启动命令： 将红框命令复制出来，直接在终端上执行即可。可查看日志 `tail -fn1000 /tmp/tritonserver.log` 验证，有个表格模型都 ready 则模型启动正常：
14. .** **文档深度解析任务结果中常见的边框****bbox****逻辑说明**
在文档深度解析任务输出结果中，常见解析内容中的边框位置表达格式为数组，样例如下：

**样例：**

[0.1250, 0.2500, 0.1667, 0.2500]

**假设：**

智能体工厂 OpenTrek 页面尺寸：width=800, height=600 标记边界框：x0=100, y0=150, x1=300, y1=250

**计算：**

x0/width = 100/800 = 0.1250 y0/height = 150/600 = 0.2500 (y1-y0)/height = (250-150)/600 = 100/600 ≈ 0.1667 (x1-x0)/width = (300-100)/800 = 200/800 = 0.2500

**含义：**

该边界框从图像左边 12.5%、顶部 25% 的位置开始，高度占图像 16.67%，宽度占 25%。

##### 管控应用热更新

数据加工管控应用包含：data-engine-console，data-engine-workflow，更新方法一致。
1. .** **获取镜像文件**
通常为 oci 文件，原厂履约或产研提供。
2. .** **分发镜像到客户仓库**
使用 skopeo 命令，将应用镜像oci 文件推送到镜像仓库：

```bash
# sfm-kn-data-engine
skopeo copy oci-archive:sfm-kn-data-engine_2.1.0-hotx.1.oci docker://__your_repo_endpoint__/sfm/sfm-kn-data-engine:<YOUR_TAG>
# sfm-kn-workflow
skopeo copy oci-archive:sfm-kn-workflow_2.1.0-hotx.1.oci docker://__your_repo_endpoint__/sfm/sfm-kn-workflow:<YOUR_TAG>
```

3. .** **更新镜像**
注意：备份好原始配置，参考命令： `kubectl get pod -n sfm data-engine-workflow -o yaml >`

```
data-engien-workflow_deploy.yaml.bak
```

进入ops集群，编辑对应管控应用的 deploy 配置：
# data-engine-workflow，修改`image`为最新镜像`tag`

```bash
kubectl edit deploy -n sfm data-engine-workflow
```

# data-engine-console，修改`image`为最新镜像`tag`

```bash
kubectl edit deploy -n sfm data-engine-console
```

编辑后会自动重启，等到如下状态，则更新成功： 更新完记得回到产品界面验证下受影响的功能。

##### 离线镜像热更新

智能体工厂 OpenTrek
1. .** **获取镜像文件**
通常为 oci 文件，原厂履约或产研提供。
2. .** **分发镜像到客户仓库**
使用 skopeo 命令，将加工任务镜像oci 文件推送到镜像仓库： 注意事项：
1. 不要覆盖客户已有镜像，方便回滚。在 tag 后增加 `-MMDD-release` 更新时间。
2. 2.1.1-hotx.2 比较新的版本，online/offline是相同的镜像，推一次即可
# NVIDIA:离线、在线

```
skopeo copy oci-archive:data-mixer-operators.offline.gpu.oci docker://__your_repo_endpoint__/sfm/data-mixer-operators:2.1.1-full-tritionserver-inclm odel-MMDD-release
```

# PPU（平头哥`APG`）:离线、在线

```
skopeo copy oci-archive:data-mixer-operators.offline.ppu.oci docker://__your_repo_endpoint__/sfm/data-mixer-operators:2.1.1-non-sci-tritionserver-pp u-inclmodel-MMDD-release
```

# DCU（海光`K100/BW1000`）:离线、在线

```
skopeo copy oci-archive:data-mixer-operators.offline.dcu.oci docker://__your_repo_endpoint__/sfm/data-mixer-operators:2.1.1-non-sci-tritionserver-dc u-inclmodel-MMDD-release
```

# Atlas（华为`910B`）:离线、在线

```
skopeo copy oci-archive:data-mixer-operators.offline.atlas.oci docker://__your_repo_endpoint__/sfm/data-mixer-operators:2.1.1-non-sci-tritionserver-at las-inclmodel-MMDD-release
```

**注意：如果 skopeo 命令无法安装或使用，可以用 sfm-deploy-tool 镜像内的 skopeo 命令进行镜像**

**push**

# 仅供参考，参数根据实际情况进行替换

```bash
docker run --rm -it --name skopeo -v /root/data-mixer/2.1.1-hotx.2/data-mixer-operators .gpu.oci:/app/data-mixer-operators.gpu.oci sfm-deploy-tool:1.0.0 skopeo --insecure-poli cy copy --dest-creds username:pwd --dest-tls-verify=false oci-archive:/app/data-mixer-o perators.gpu.oci docker://acr-opentrek-prd-registry-vpc.cnshanghai.cr.aliyuncs.com/sfm/data-mixer-operators:2.1.1-hotx.2-gpu-MMDD-release
```

3. .** **修改数据库镜像标签**

**先对客户的 kn_kv 表配置做备份！！！**

**先对客户的 kn_kv 表配置做备份！！！**

**先对客户的 kn_kv 表配置做备份！！！**

**3.1. 正常更新流程**

由于增加了 `-MMDD-release` 的 tag 后缀，需要修改数据库更新默认镜像标签。 如何连接数据库，参考本篇文档的“其他” 章节 N卡离线镜像tag： 智能体工厂 OpenTrek PPU离线镜像tag：
# 更新对应的`tag`，直接根据`value`替换即可
# 注意⚠️：保存好历史镜像标签，如果新镜像有问题，可以更新数据库回滚
# 例如：更新N卡离线镜像标签

```
update kn_kv set value='2.1.0-full-tritonserver-inclmodel-0810-release' where value='2.1.0-full-tritonserver-inclmodel-0804-release';
```

**3.2. 特例：如果 process.imageTag.xxx 不包含客户卡型号**

比如：华为系列显卡、海光系列显卡、英伟达 A800、H200、H100 等不太常见型号，没有默认支持，需要手动在数据库里添加“型号-镜像标签”的映射关系。 由于部分项目中的型号是手动配置的，所以需要检查清楚再修改数据库。 这里看下资源组里面的 GPU 类型（以 H200 为例）： 然后执行如下SQL（value对应 data-mixer-operators 的镜像 tag）：

```
insert into public.kn_kv (key, value) values ('process.imageTag.NVIDIA-H200', '2.1.1-non-sci-tritonserver-inclmodel');
```

4. .** **使用更新后的镜像**

**4.1. 新任务**

新建任务会直接读取数据库中的镜像 tag 配置，直接使用新镜像。 智能体工厂 OpenTrek

**4.2. 存量任务**

存量任务由于已经创建，镜像标签不会自动修改，需要执行 “下线” -> “编辑” -> “保存” -> “上线” 完成更新。 什么都不用改，直接保存： 发布后，点运行即可生效：

**4.3. 确认使用新镜像**

“任务运行总览”页，点击日志，在日志头部，可以看到“Successfully pulled image”的完整镜像信息，如果和配置的 tag 相同，则操作成功。 智能体工厂 OpenTrek

**其他**

**如何连接DKE管控数据库？**

# 获取`console`数据库连接信息

```bash
kubectl exec -n sfm $(kubectl get pods -n sfm -l "app=data-engine-console" -o jsonpath= '{.items[0].metadata.name}') -- sh -c 'env | grep -E "postgres_host|postgres_port"' kubectl exec -n sfm $(kubectl get pods -n sfm -l "app=data-engine-console" -o jsonpath= '{.items[0].metadata.name}') -- sh -c 'env | grep knDataEngine'
```

# 获取`workflow`数据库连接信息

```bash
kubectl exec -n sfm $(kubectl get pods -n sfm -l "app=data-engine-console" -o jsonpath= '{.items[0].metadata.name}') -- sh -c 'env | grep -E "postgres_host|postgres_port"' kubectl exec -n sfm $(kubectl get pods -n sfm -l "app=data-engine-console" -o jsonpath= '{.items[0].metadata.name}') -- sh -c 'env | grep knWorkflow'
```

# 返回如下信息(knDataEngine|knWorkflow后缀不同)：

```
_AUTOCONF_postgres_host=pc-xxx.pg.polardb.rds.aliyuncs.com _AUTOCONF_postgres_port=3433 _AUTOCONF_postgres_database_knDataEngine=kn_data_engine_ctl _AUTOCONF_postgres_username_knDataEngine=polar_admin _AUTOCONF_postgres_password_knDataEngine=xxx
```

##### 视频数据处理常见问题FAQ

**输出数据集**

**结果子集没有创建**

**错误信息**

pipeline日志，执行结果为空智能体工厂 OpenTrek

```
2025-09-11 17:09:02.367 | INFO | data_mixer_operators.utils.trace_utils:36 - ==|> P ROCESS_DATA took 52.0905 seconds <|== 2025-09-11 17:09:02.368 | INFO | data_mixer_operators.core.executor:243 - All OPs a re done in 52.091s. 2025-09-11 17:09:02.368 | INFO | data_mixer_operators.core.executor:246 - Exporting dataset to disk... 2025-09-11 17:09:02.369 | WARNING | data_mixer_operators.core.exporter:224 - Dataset i s empty, skipping export.
     ,----.          ___        _ __     ,--.--------.
  ,-.--` , \  .-._ .'=.'\    .-`.' ,`.  /==/,  -   , -\  ,--.-.  .-,--.
 |==|-  _.-` /==/ \|==|  |  /==/, -   \ \==\.-.  - ,-./ /==/- / /=/_ /
 |==|   `.-. |==|,|  / - | |==| _ .=. |  `--`\==\- \    \==\, \/=/. /
/==/_ , / |==| \/ , | |==| , '=',| \==\_ \ \==\ \/ -/
|==|    .-'  |==|- ,   _ | |==|-  '..'        |==|- |     |==|  ,_/
|==|_  ,`-._ |==| _ /\   | |==|,  |           |==|, |     \==\-, /
/==/ , / /==/ / / , / /==/ - | /==/ -/ /==/._/ `--`-----`` `--`./ `--` `--`---' `--`--` `--`-`
```

**问题原因**

以下面的加工任务日志为例：image_aspect_ratio_filter 算子执行结束后，返回了空的dataset，"OP [image_aspect_ratio_filter] returns empty dataset"。对比输入数据集和算子参数配置后发现是因为输入的都是竖屏图像，但算子的最小宽高比是1，导致输入数据全部被过滤掉。

```
2025-09-11 17:09:01.682 | INFO | data_mixer_operators.manager.download_manager:130
- Downloading[opentrek] took 0.000992 seconds.
2025-09-11 17:09:01.695 | INFO | data_mixer_operators.manager.download_manager:436
- use cache skip download.
2025-09-11 17:09:01.696 | INFO | data_mixer_operators.manager.download_manager:130
- Downloading[opentrek] took 0.000856 seconds.
2025-09-11 17:09:01.708 | INFO | data_mixer_operators.manager.download_manager:436
- use cache skip download.
2025-09-11 17:09:01.709 | INFO | data_mixer_operators.manager.download_manager:130
- Downloading[opentrek] took 0.000853 seconds.
image_aspect_ratio_filter_compute_stats (num_proc=4): 100%|##########| 280/280 [00:01<0 0:00, 245.00 examples/s] image_aspect_ratio_filter_process (num_proc=4): 0%| | 0/280 [00:00<?, ? examples/s] image_aspect_ratio_filter_process (num_proc=4): 25%|##5 | 70/280 [00:00<00:00, 6 13.39 examples/s] image_aspect_ratio_filter_process (num_proc=4): 100%|##########| 280/280 [00:00<00:00, 994.38 examples/s] 2025-09-11 17:09:02.245 | WARNING | data_mixer_operators.core.data:257 - OP [image_asp ect_ratio_filter] returns empty dataset.
```

**解决方法**

结合实际需求，修改算子的参数配置。

**结果样本量比预期小**

**问题现象**

视频解析结果中有8个关键帧，但抽帧模板执行完成后，结果子集中只有2个样本。 智能体工厂 OpenTrek

**问题原因**

抽帧模板除了抽帧算子以外，还包含了图像模糊过滤、图像宽高比过滤等算子，缺失的样本是被这些过滤算子滤掉了。

**解决方法**

检查加工任务日志中，每个算子返回的样本数量，定位到是哪个算子减少了样本数，再结合实际需求对算子的入参做调整。在日志中搜索"Done in"，可快速定位到算子执行结果。

```
[2025-09-17 11:06:52.543] 2025-09-17 11:06:52.542 | INFO | data_mixer_operators.utils.trace_utils:36 - ==|> VideoParseOfflineMapper took 1286.2090 seconds <|== [2025-09-17 11:06:52.575] 2025-09-17 11:06:52.574 | INFO | data_mixer_operators.core.data:261 - OP [video_parse_offline_mapper] Done in 1286.211s. Left 20 samples.
```

**音频提取转换与上传-audio_extract_mapper**

**FFmpeg执行失败**

**错误信息**

智能体工厂 OpenTrek 加工任务日志，“Output file #0 does not contain any stream”

```
2025-09-08 18:04:12.006 | ERROR | data_mixer_operators.utils.exception_utils:13 - Tr aceback (most recent call last):
  File "/home/admin/data-mixer-
operators/data_mixer_operators/ops/mapper/audio_extract_mapper.py", line 156, in proces
```

s

```
    raise RuntimeError(f"FFmpeg执行失败 (代码: {process.returncode}):
{stderr_bytes.decode(errors='ignore')}") RuntimeError: FFmpeg执行失败 (代码: 1): ffmpeg version 4.4.2-0ubuntu0.22.04.1 Copyright ( c) 2000-2021 the FFmpeg developers
  built with gcc 11 (Ubuntu 11.2.0-19ubuntu1)
  configuration: --prefix=/usr --extra-version=0ubuntu0.22.04.1 --toolchain=hardened --
libdir=/usr/lib/x86_64-linux-gnu --incdir=/usr/include/x86_64-linux-gnu --arch=amd64 -enable-gpl --disable-stripping --enable-gnutls --enable-ladspa --enable-libaom --enable -libass --enable-libbluray --enable-libbs2b --enable-libcaca --enable-libcdio --enablelibcodec2 --enable-libdav1d --enable-libflite --enable-libfontconfig --enable-libfreety pe --enable-libfribidi --enable-libgme --enable-libgsm --enable-libjack --enable-libmp3 lame --enable-libmysofa --enable-libopenjpeg --enable-libopenmpt --enable-libopus --ena ble-libpulse --enable-librabbitmq --enable-librubberband --enable-libshine --enable-lib snappy --enable-libsoxr --enable-libspeex --enable-libsrt --enable-libssh --enable-libt heora --enable-libtwolame --enable-libvidstab --enable-libvorbis --enable-libvpx --enab le-libwebp --enable-libx265 --enable-libxml2 --enable-libxvid --enable-libzimg --enable -libzmq --enable-libzvbi --enable-lv2 --enable-omx --enable-openal --enable-opencl --en able-opengl --enable-sdl2 --enable-pocketsphinx --enable-librsvg --enable-libmfx --enab le-libdc1394 --enable-libdrm --enable-libiec61883 --enable-chromaprint --enable-frei0r --enable-libx264 --enable-shared
  libavutil      56. 70.100 / 56. 70.100
  libavcodec     58.134.100 / 58.134.100
  libavformat    58. 76.100 / 58. 76.100
  libavdevice    58. 13.100 / 58. 13.100
  libavfilter     7.110.100 /  7.110.100
  libswscale      5.  9.100 /  5.  9.100
  libswresample   3.  9.100 /  3.  9.100
  libpostproc    55.  9.100 / 55.  9.100
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from '/tmp/dm_video_4vo7cz01.tmp':
  Metadata:
    major_brand     : mp42
    minor_version   : 0
    compatible_brands: mp42isom
    creation_time   : 2018-11-14T02:30:13.000000Z
    encoder         : mp4creator 1.4.4
  Duration: 00:01:32.03, start: 0.000000, bitrate: 276 kb/s
  Stream #0:0(eng): Video: mpeg4 (Simple Profile) (mp4v / 0x7634706D), yuv420p, 1280x72
0 [SAR 1:1 DAR 16:9], 275 kb/s, 30 fps, 30 tbr, 90k tbn, 30 tbc (default)
    Metadata:
      creation_time   : 2018-11-14T02:30:13.000000Z
      vendor_id       : [0][0][0][0]
Output #0, wav, to '/tmp/dm_audio_ozay80n_.wav': Output file #0 does not contain any stream
```

**报错原因**

输入的视频文件不包含音频，导致算子执行失败智能体工厂 OpenTrek

**解决方法**

使用内置算子批量过滤掉没有声音的视频

**选不到ASR模型**

**问题表象**

Funasr模型下拉框为空，没有可用的模型服务

**问题原因**

没有部署ASR服务，或者已经部署了服务，但是没有注册到OpenTrek Agent Dev

**解决方法**

请到aistudio使用公共镜像 cpu-funasr 部署在线服务，建议单实例配置16C32G资源（不需要GPU），支持13个并发。下面仅介绍关键步骤，具体操作请参考aistudio的文档。
1. aistudio 部署在线服务
智能体工厂 OpenTrek 智能体工厂 OpenTrek
2. OpenTrek Agent Dev注册aistudio的模型服务

### 模型接入

**AIStudio 模型连通失败排查**

检查OP租户区与AIStudio模型服务网络是否打通，在智能体应用agent pod中curl访问AIStudio vpc网络地址，检查是否域名解析及网络正常，如遇Unknowhost等报错则网络不通，检查是否部署在同一VPC 中，网络部署架构如下根据OpenTrek Agent Dev中的模型提供方服务code，在AIStudio产品中检查AIStudio模型服务状态是否在运行中。若模型服务为停用状态或已删除，均为异常，需要恢复根据OpenTrek Agent Dev中的模型服务APIKey，在AiStudio产品中检查模型APIKey有效性

**OpenTrek Agent Dev模型接入模型选择列表为空排查**

检查当前登录方式，OpenTrek Agent Dev需要通过“角色授权访问”跳转登录智能体工厂 OpenTrek 跳转AIStudio产品，检查模型在线服务列表是否有运行中模型服务

**OpenTrek Agent Dev模型接入模型APIKey列表为空排查**

以当前账号“资源集管理员”角色跳转到AIStudio产品，检查APIKey是否绑定了对应的模型服务智能体工厂 OpenTrek

**AIStudio在线服务状态检查**

根据服务ID查询AIStudio在线服务，检查模型服务状态检查AI网关是否开启，在访问设置中检查是否配置AI网关，以及查询VPC专有网络地址是否存在智能体工厂 OpenTrek APIKey有效性检查
