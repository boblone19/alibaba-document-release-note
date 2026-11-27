# tools链说明 —— 这个仓库是怎么把阿里云文档变成可交付 Markdown 的

面向"接手就要改东西的人"。每节都给**能直接贴跑的命令**。仓库根的路径、册数、包体积以
`doc_cache_index.json` 与 `ApsaraStack_Markdown_split_manifest.json` 为准，别信任何文档里写死的数字（含本文件）。

---

## 0. 一句话架构

```
阿里云站点/接口 ──list_docs.py──▶ 候选清单 ──cache.decide()──▶ 该下哪些
                                                            │
                       release_batch.py / pull_docs.py ─────┤ 下载 PDF
                                                            ▼
                                              pdf2md.py（纯文本转换内核）
                                                            ▼
                       交付树 markdown/… （转完即删 PDF，本地只留 Markdown）
                                                            ▼
        redact_vendor_docs.py（脱敏）→ build_indexes.py（人读清单）→ make_split_zip.py（分卷）
                                                            ▼
                              check_leaks.py（pre-commit 钩子）→ git push
```

三条不可破坏的约定：

1. **`doc_cache_index.json` / `.csv` 是唯一真源**（"已下载 + 已转换 + 该放哪"）。人读清单、
   分卷、release note 全部从它派生；它坏了等于交付坏了。
2. **本地只留 Markdown，不留 PDF**。PDF 是过路料，每本转成功即删（`--no-delete` 才保留）。
   云端 PDF 位置记在 `pdfCloud` / `mdCloudKey` 两列。
3. **`mdCloudKey` / `pdfCloud` 是 OSS 对象键**，指向阿里云已发布包里的**中文路径**。
   本地目录改名时**绝不能跟着改**，否则这两个键就指错东西（`rename_*` 脚本里已明确跳过）。

---

## 1. 数据契约（先读这个再动代码）

`tools/cache.py` 定义字段与判重逻辑：

| 字段 | 含义 | 谁在用 |
|---|---|---|
| `id` | 稳定身份 = `lang:` + URL 去掉文件名里的 8 位日期 | 所有脚本的 join key |
| `versionStamp` | 文件名里的 8 位日期（文档版本） | 判"官方是否发了新版" |
| `key` | `id@versionStamp` | 版本比对 |
| `url` | 原始 PDF 直链 | 下载入口（`source_url` 也写进 md front matter） |
| `pdfCloud` | `apsara-docs/zips*/…zip`，PDF 所在云端大包 | 云端核对、缺件回溯 |
| `mdCloudKey` | `apsara-docs/markdown…zip#<包内路径>`，云端 Markdown 位置 | 云端同步、去重 |
| `localPath` | 交付树里的 PDF 名义路径（**本地不存在该文件**） | 展示、云端对照 |
| `markdown` | 交付树里的 md 路径（真实存在） | 打包、清单、校验 |
| `markdownSha256` `markdownKB` | md 内容指纹与体量 | 判重、回归比对 |
| `inScope` | 是否纳入口径 | `release_batch` / 清单 |

判重五态（`cache.decide()`）：

| 判定 | 条件 | 动作 |
|---|---|---|
| `SKIP` | 同 id 同 stamp 且有 `markdown` | 跳过，不下转 |
| `CONVERT` | 同 id 同 stamp、无 `markdown`、`inScope` 真 | 只转不重下 |
| `SCOPE` | 同上但 `inScope` 假 | **不重评、不下载**；要扩范围得明确加回来 |
| `FETCH` | 同 id、stamp 更新 | 只下这一本 |
| `NEW` | 全新 id | 整本下转 |

判重实际只看三件事：`id`（是不是同一本书）、`versionStamp`（官方有没有发新版）、
`markdown` + `markdownSha256`（有没有已转好的产物）。`cache.FIELDS` 共 22 列，`.csv` 表头与它**完全一致**；
JSON 里另有 `md5pdf` / `mdChars` / `key` 等历史列（`md5pdf` 存 584 行），**代码不读它们，别依赖**。

---

## 2. 阶段与脚本

### 2.1 取站点清单（不下载 PDF）
```bash
export APSARA_COOKIE='…'                      # 只有中文需要；英文站免登录
python3 tools/list_docs.py --langs en    --out ../../.scratch/en_all.json
python3 tools/list_docs.py --langs zh,en --version V3.18.6 --out ../../.scratch/all.json
```
- 英文：抓下载页里内嵌的 `"cardItems":[…]` JSON，按 `Version` 归版本，书名里解析出**英文产品名**。
- 中文：走 `help.aliyun.com/apsara/api`；cookie 失效会返回空清单并在 stderr 明说（**不静默降级**）。
- `localPath` 已是英文路径（域用 `rename_cn_dirs.DOMAIN_EN` 那张表，产品/手册用接口给的 ASCII code）。
  以后新抓的书不会再落中文目录。

核对"站点到底有几本"的**唯一可靠做法**：解析页面 cardItems 后按 `Version` 取 `href` 去重，再与索引
`url` 求差集。页面上显示的行数（例如 v3.18.6 系列显示 554）是卡片行数 1,108÷2 = 554 行，
其中 2 行是空条目（`href` 与书名都空），**不是缺书**。靠肉眼数筛选器会得出错误结论。

### 2.2 判重要下哪些 / 少量增补
```bash
python3 tools/pull_docs.py                                   # 只出决策表
python3 tools/pull_docs.py --langs en --fetch --into-tree    # 只补 NEED，并按登记路径写回
```

### 2.3 新版本线整批接入（下载→转换→校验→登记→删 PDF）
```bash
python3 tools/release_batch.py --manifest ../../.scratch/en_all.json --version V3.18.3 \
        --dl-workers 6 --cv-workers 3 --dry-run     # 先探体积，0 流量
python3 tools/release_batch.py --manifest ../../.scratch/en_all.json --version V3.18.3 \
        --dl-workers 6 --cv-workers 3
```
- 自动跳过索引已登记且有 md 的书（幂等，中断后重跑接着来）。
- **有失败就不删暂存目录**，留下的 PDF 下次 `download()` 直接复用；全成功才 rmtree。
- 逐本落账（转换成功即写索引），进程被杀不白跑。
- 转换前会挡：正文过短（疑似图片型 PDF）、正文含内嵌图片、`%PDF` 头不对。

### 2.4 转换内核 `pdf2md.py`（唯一该改"转换质量"的地方）
单独跑一本：
```bash
python3 tools/pdf2md.py --pdf x.pdf --out y.md --url <原链> --title "<书名>" \
        --prodver V3.18.6 --docver 20260924
```
内部机制（改动前务必看懂，这些位置都是踩过坑修出来的）：

| 机制 | 位置 | 为什么这样 |
|---|---|---|
| 裁前导页 | `Manual.start` | 封面/法务/约定/目录页按第一页书签之前裁掉 |
| 标题层级 | `HEAD_MIN_PT=13.5` + `HEAD_NUM` | 大字号编号行直接当标题 |
| **小字号标题升级** | `num_head()` | 大量英文手册 3~6 级标题只排 9.8–10.9pt；**能与书签编号对上文字的行一律按编号层级升标题**，否则 `junk()` 会当目录残留整行删掉（静默丢正文） |
| 两行式标题 | `NUM_ONLY` + `drop_next` | API 手册常把 `1.5.2.` 单独成行、标题在下一行；合并且只输出一次，标签格没配上正文格时正文格留给下一轮按自身类型处理（曾整格跳过导致 -10k 字符） |
| 提示框 | `note_kind()`+`note_lines()` → `emit_note()`；文本级兜底 `note_blocks()` | PDF 里 note 是独立文本块、整块同一灰（实测 `0x73777a`／`0x777777`，`_grey_ratio()` + `_near()` 容差比色，标签色由 `scan_frequency()` 里的 `line_label()` 反推）；输出 `> **Note:** …`，框内列表 `> - …`，无标签灰框 `> …`；标签自成一格按纵向间距 ≤26pt 与正文格合并；表格单元与代码块内不转（GFM 表格放不下引用块） |
| **页眉判据** | `junk(edge=…)` | 只按"跨页重复次数"判页眉会误杀正文套话（DNS 手册每接口必现的"该接口使用公共请求头…"被删 101 处）。现要求**同时落在顶/底 14% 页眉带** |
| 引用块边界 | `close_quote()` + `_quote_blank()` | 引用块后面必须隔空行，否则 CommonMark lazy continuation 把下一段吸进引用 |
| 目录标题行 | `_toc_head(lang=…)` | 中文册用 `## 目录`。**语言必须由调用方传**（`convert(lang=)`），"见汉字就当中文册"会把夹带中文字形的英文册误判 |
| front matter | `convert(src_pdf=…)` | 中文册交付命名 `21_手册名_手册code.pdf` 不能被暂存临时名覆盖 |
| 无书签兜底 | `fallback_toc()` | PDF 没书签时用转换中收集到的编号标题拼目录 |

front matter 里的 `converter:` 标记就是转换器的版本号。当前链路：
`toc+numbered-headings` → `+note-quotes` → `+edge-junk`。
**改了转换逻辑必须同时升 `pdf2md.py` 的标记串和 `reconvert_en.py` 的 `NEW_TAG`**，
否则重转会把已处理的书当成"跳过"（这是幂等判断的唯一依据）。

### 2.5 整批重转（提升存量质量）
```bash
python3 tools/reconvert_en.py --plan                      # 只统计待重转
python3 tools/reconvert_en.py --lang zh --limit 5         # 先试点
python3 tools/reconvert_en.py --lang zh --workers 3       # 中文全量
python3 tools/reconvert_en.py --lang en --workers 3       # 英文全量
python3 tools/reconvert_en.py --only ../../.scratch/redo.json --force   # 指定清单
```
每本从 front matter 的 `source_url` 重下 PDF（按 URL 派生临时名，可复用）、原地覆盖同名 md、
更新索引 sha/KB/字符数、删 PDF。**跑之前一定先预检 PyMuPDF**（见 §4 坑 1）。

### 2.6 交付树改名
```bash
python3 tools/rename_en_dirs.py            # 试跑：出迁移表 + 冲突检查
python3 tools/rename_en_dirs.py --apply [--manifest ../../.scratch/en_all.json]
python3 tools/rename_cn_dirs.py --apply
python3 tools/rename_en_files.py --apply   # 英文文件名去版本/套件前缀
```
默认只报不动；先做**撞名检查**（新路径重名就直接拒绝执行），搬完顺带剪空目录、改 `markdown`/
`localPath`、重写全仓引用（跳过云端键）。两张映射表是命名口径的唯一来源：
英文取 `list_docs` 的 `product`（书名里解析），中文取 `DOMAIN_EN` + 接口给的 `productCode` / 手册 `code`。

### 2.7 脱敏（提交前后各一次，重转之后必跑）
```bash
python3 tools/redact_vendor_docs.py [markdown …]   # 可重复执行
python3 tools/check_leaks.py                        # 规则自查（不比对个人邮箱明文）
```
厂商 PDF 正文里混着真实内部邮箱、`LTAI…` AccessKeyId、AccessKeySecret 实值。规则、豁免形状都在脚本
docstring 里（example.com 域、Kerberos 主体、`user@IP`、`git@…` 克隆地址、`rm-*/pc-*/gp-*` 实例地址等不算 PII）。
**重转会把云端原始 PDF 的新正文拉回来，等于把已打码的内容冲掉** —— 所以每次重转/新接入后必须再跑一遍，
再刷新索引里的 `markdownSha256`（否则校验和被脱敏前的内容污染）。
个人邮箱与凭证由 `.git/hooks/pre-commit → check_leaks.py --cached` 拦住；
自己的地址写成 `REDACTED:<sha256 前 8 位>`。钩子只活在 `.git/` 里，换沙箱要按 `check_leaks.py`
顶部说明重新装（一行 `exec`）。

### 2.8 派生人读清单与分卷包
```bash
python3 tools/build_indexes.py       # markdown/README.md + all_docs_overview.html，并修 inScope、报失效链接
python3 tools/make_split_zip.py --plan          # 只看分组与装箱预估，不写文件
python3 tools/make_split_zip.py                 # 生成 3 个包 + 清单，并自动 --verify
python3 tools/make_split_zip.py --max-mb 40 --parts 3   # 收紧上限/强制卷数
python3 tools/make_split_zip.py --verify        # 只核验
python3 tools/ascii_paths.py --apply            # 路径里混进 NBSP/全角括号时折成 ASCII
```
`make_split_zip.py` 的口径（2026-11-18 定版）：
1. **中文树单独一个整包**：顶层 `01_…` + `02_…` 合成 `ApsaraStack_Markdown_zh_296books.zip`，
   不参与装箱；若它本身超 `--max-mb` 直接报错，不偷偷拆卷（这是 Bob 定的规则：中文看一个包就够）。
2. **其余按版本线分卷**：以顶层目录为**不可拆的最小单位**（下一卷解压就是那一版本完整可读的 Markdown），
   实测每组压缩后字节，卷数取 `ceil(总量/上限)` 后用 LPT 均衡；每卷是独立 zip（不是 `.z01` 切片），无需拼接。
3. 产物文件名**必须 ASCII**；旧的 `markdown_全量_*册.zip`、`ApsaraStack_Markdown_1247_*` 等命名会被自动清掉。
4. 清单 `ApsaraStack_Markdown_split_manifest.json`：卷名/字节/sha256/条目数/册数/包含哪些顶层目录/是中文整包还是分卷/下载顺序。
5. `--verify` 检查：每卷 sha256 与字节、`testzip`、卷内每条与盘上逐条 md5、**有没有文件没进任何卷**、
   **中文整包内容与盘上 `01_`/`02_` 是否完全相等**、文件名与卷内路径是否 ASCII、单卷是否超上限；失败退码非 0。

顺序必须是 **脱敏 → build_indexes → make_split_zip**：先打包再重建清单，卷里装的就是旧文件
（`--verify` 抓到过我一次：卷内 `markdown/README.md` 与盘上不一致）。

为什么分卷而不用 LFS：GitHub 单文件软限 50 MB、硬限 100 MB；全量约 63.5 MB 已越线。
分卷不改写历史、不要 git-lfs 环境、clone 后即可按卷取。

### 2.9 Release note 那一套
```bash
python3 tools/rn2607_pairs.py            # 证据层：V3.18.6 → V3.18.6_2607 逐册配对差异
python3 tools/build_note_2607.py         # 渲染 ApsaraStack-V3.18.6_2607-Release-Note-EN.md
python3 tools/rn3162_pairs.py            # 证据层：V3.16.2 → V3.18.6
python3 tools/build_note_3162.py         # 渲染旧口径 release note（历史保留）
python3 tools/fetch_release_corpus.py    # 只为 release note 补抓/补转的额外英文册
```
渲染脚本读的证据 JSON 与写出的 md 名字都写在脚本里；release note 里引用的册数/页数一律从索引取。

---

## 3. 典型任务怎么串

**A. 官方发了新版本线（例：又出 2608）**
```bash
export APSARA_COOKIE='…'
python3 tools/list_docs.py --langs en --out ../../.scratch/en_new.json
python3 tools/release_batch.py --manifest ../../.scratch/en_new.json --version V3.18.6_2608 --dry-run
python3 tools/release_batch.py --manifest ../../.scratch/en_new.json --version V3.18.6_2608
python3 tools/redact_vendor_docs.py markdown
python3 tools/build_indexes.py && python3 tools/make_split_zip.py
git add -A && git commit && git push
```
**B. 改了 `pdf2md` 的转换规则**：升 `converter` 标记与 `NEW_TAG` → 抽 3~5 本试点（`--limit`）→
逐本核对结构指标 → `--lang zh` / `--lang en` 全量 → 脱敏 → 刷索引 → 重打包 → 提交。
**C. 交付前的固定顺序**（踩过：打包完又重建清单 → 卷里装的是旧文件）
```bash
python3 tools/redact_vendor_docs.py markdown    # 1 脱敏
python3 tools/build_indexes.py                  # 2 人读清单（读索引）
python3 tools/make_split_zip.py --parts 2       # 3 最后才打包
python3 tools/make_split_zip.py --verify        # 4 验收
```
脱敏会改字节，所以索引里的 `markdownSha256` / `markdownKB` 必须在脱敏**之后**重算，
否则指纹记的是转换瞬间、不是交付内容。`--verify` 不是走过场：本次就是它抓到
"卷内 `markdown/README.md` 与盘上不一致"，因为我把打包排在了重建清单前面。

**D. 只想核对"有没有缺书"**：见 §2.1 的 cardItems 差集法，别看页面显示的行数。

---

## 4. 坑（都真实发生过，别再犯）

1. **PyMuPDF 版本极其敏感**：本仓库内容在 **1.28.2** 下产出；换成 2.0 同一本 PDF 少约 5% 正文
   （`get_text("dict")` 分块行为变了）。沙箱会吞 `site-packages`，而且 worker 里 `import` 失败是被
   `try/except` 吞掉的，日志会出现"重转完成 X 本，失败 0 本"却一个字没产物 —— **长跑前必须预检**
   `python3 -c "import pymupdf"`，缺了就 `pip install -q "pymupdf==1.28.2"`，失败就别开始下载。
2. **别把转换失败当成功**：`release_batch` / `reconvert_en` 末尾都会打印失败明细，`--verify`/退出码才是判据。
3. **重转 = 云端原始内容回来**：脱敏会被冲掉，跑完必补 `redact_vendor_docs.py`，再刷 `markdownSha256`。
4. **改名不碰云端键**：`mdCloudKey` / `pdfCloud` 保持中文原样。
5. **引用块后面要空行**，否则下一段被 lazy continuation 吃进引用（`_quote_blank` 负责）。
6. **中文/英文判定要显式传参**（`convert(lang=)`），不要靠"有没有汉字"。
7. **装箱别腰斩版本线**：分组超过上限直接报错，让人来决定切法。
8. **push 会跟下载抢带宽**：批量下载期间 push 常报 TLS/443 失败。要么错峰，要么在跑批前先把已完成的
   工作提交掉，别反复空试。
9. **不要往 `permissions.additionalDirectories` 写路径**（Bob 2026-10-21 明确禁止并手工清理过）；
   换目录用 Bash 的 `workdir` 参数或绝对路径。
10. **路径命名只能 ASCII**：官方英文书名里混了 NBSP 与全角括号，肉眼看不出；`cache.fold_ascii()` 在写路径处统一折叠，`ascii_paths.py` 收拾存量，`make_split_zip.py --verify` 兜底把关。
11. **交付目录里不写个人邮箱/凭证明文**；文档里的数字必须能在索引/清单里复现，改完自查一遍。

---

## 5. 脚本索引

| 脚本 | 一句话职责 | 常用参数 |
|---|---|---|
| `cache.py` | 索引读写 + 判重决策（真源） | 库，被 import |
| `list_docs.py` | 抓站点清单（英文页 cardItems / 中文接口） | `--langs --version --stacks --out` |
| `pull_docs.py` | 出决策表；`--fetch` 只补该下的 | `--langs --fetch --into-tree --limit` |
| `release_batch.py` | 新版本线整批接入 | `--manifest --version --dry-run --no-delete` |
| `pdf2md.py` | PDF→Markdown 转换内核 | `--pdf --out --url --title --prodver --docver` |
| `reconvert_en.py` | 存量整批原地重转（中英都走它） | `--lang --plan --only --force --workers` |
| `redact_vendor_docs.py` | 厂商文档 PII/凭证脱敏（可重复跑） | 路径列表，默认三棵树 |
| `check_leaks.py` | 提交前自查（pre-commit 钩子调它） | `--cached` |
| `rename_en_dirs.py` | 英文树目录改英文产品名 | `--apply [--manifest]` |
| `rename_en_files.py` | 英文树文件名去版本/套件前缀（`<产品名> <类型> <日期>.md`） | `--apply [--limit]` |
| `rename_cn_dirs.py` | 中文树目录/文件名改 ASCII | `--apply` |
| `build_indexes.py` | 从索引重生成人读清单与总览 HTML | — |
| `make_split_zip.py` | 中文单包 + 其余分卷，ASCII 命名，产清单与核验 | `--plan --parts --max-mb --prefix --verify` |
| `ascii_paths.py` | 把路径里的 NBSP/全角括号无损折成 ASCII（不碰汉字） | `--apply` |
| `rn2607_pairs.py` / `rn3162_pairs.py` | release note 的证据层（逐册配对差异） | — |
| `build_note_2607.py` / `build_note_3162.py` / `build_note.py` / `release_note.py` | 渲染 release note | — |
| `fetch_release_corpus.py` | 只为 release note 补抓补转英文册 | `[workers]` |

根目录 `AGENTS.md`（工作区常驻指令）与 `README.md`（交付索引）是另外两份必读；
本文件只讲"怎么干活"，册数/体积/覆盖情况一律看 `doc_cache_index.json`、`ApsaraStack_Markdown_split_manifest.json`。
