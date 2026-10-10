# 一次性配置（给「我不会弄」版）

云端同步 **GitHub → Notion** 只差一个 Secret：`NOTION_TOKEN`。

`NOTION_DATABASE_ID` 已由助手写入仓库 Secrets，你**不用管**。

---

## 别进错页面

| ❌ 不要 | ✅ 要 |
|--------|------|
| Notion **开发者工具 → 新连接 → OAuth** | [notion.so/my-integrations](https://www.notion.so/my-integrations) → **新建集成**（Internal Integration） |
| 连接名称填 `NOTION_DATABASE_ID` | 集成名称填 **`Fetch China GitHub Sync`** |

OAuth 是给 Cursor/网页登录用的；**GitHub Actions 必须用 Internal Integration 的 Secret**。

---

## 你只需要 3 步

### 1. 创建 Notion 集成

1. 打开 https://www.notion.so/my-integrations
2. **+ 新建集成** → 名称：`Fetch China GitHub Sync`
3. 关联工作区 → **提交**
4. 复制 **Internal Integration Secret**（形如 `ntn_...` 或 `secret_...`）

### 2. 把集成连到看板

1. 打开 Notion：[Fetch China 工程看板](https://app.notion.com/p/62d957d4c80e4876ac98ce829461ef0b)
2. 右上角 **⋯** → **连接** / **Connect to** → 选 **Fetch China GitHub Sync**

### 3. 把 Secret 交给 GitHub（二选一）

**A. 让 Cursor 助手代填（推荐）**

在本机新建文件（不要发到聊天里）：

`C:\Users\Administrator\.cursor\secrets\notion-github-sync.env`

内容一行：

```
NOTION_TOKEN=这里粘贴集成Secret
```

保存后回复助手：**「notion token 已放好」**。

**B. 自己在网页填**

https://github.com/martinyyang/fetch-china-blog-articles/settings/secrets/actions

→ **New repository secret** → Name: `NOTION_TOKEN` → Value: 粘贴 Secret。

---

## 验收

1. Actions → **Notion dashboard sync** → **Run workflow**
2. 打开 Notion **流水线看板**，应看到与 GitHub Issues 对应的行

演示 Issue：仓库 Issues 列表里标题含「仪表盘演示」的那条。

---

## 已有权限（无需你再给）

- **GitHub**：本机 `gh` 已登录 `martinyyang`，助手可写仓库 Secrets（除 token 外）
- **Notion（Cursor）**：OAuth 已连，助手可读写在 Fetch China 资料库
