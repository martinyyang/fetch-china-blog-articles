# 一次性配置（给「我不会弄」版）

云端同步 **GitHub → Notion** 只差一个 Secret：`NOTION_TOKEN`。

`NOTION_DATABASE_ID` 已由助手写入仓库 Secrets，你**不用管**。

---

## 你现在看到的页面是对的

路径：**设置 → 连接 → 开发者工具**（顶部有：开始 / Workers / **连接** / **个人访问令牌** / MCP 令牌）

| 标签 | 要不要点 |
|------|----------|
| **Workers**（要升级） | ❌ 不用，和本仪表盘无关 |
| **新连接 → OAuth** | ❌ 不用 |
| **个人访问令牌** | ✅ **就用这个**（最简单） |
| **连接 → 内部连接 + API 令牌** | ✅ 备选（需工作区所有者时） |

旧版入口 [notion.so/my-integrations](https://www.notion.so/my-integrations) 若打不开，**忽略**，用上面的「个人访问令牌」即可。

---

## 推荐：个人访问令牌（2 步 + 交给我）

### 1. 创建令牌

1. 在 **开发者工具** 点 **「个人访问令牌」**（Personal access tokens）
2. **新建令牌** / New token
3. 名称：`Fetch China GitHub Sync`
4. 能力勾选 **Notion API**（若有工作区选择，选 **Xiaofeng yang's…** 那个）
5. **创建** → **立刻复制**（只显示一次）

> 若看不到「新建令牌」：Business/Enterprise 可能默认禁止成员建 PAT，请工作区**所有者**在 **设置 → 连接** 里允许成员创建 PAT，或由所有者代建一条。

用 PAT **不用**再去工程看板里「连接集成」——令牌代表**你自己**，你能打开的看板 API 就能写。

### 2. 把令牌交给 GitHub（二选一）

**A. 让 Cursor 助手代填（推荐）**

文件：`C:\Users\Administrator\.cursor\secrets\notion-github-sync.env`

```
NOTION_TOKEN=这里粘贴令牌
```

保存后回复：**「notion token 已放好」**（不要粘到聊天里）。

**B. 网页自己填**

https://github.com/martinyyang/fetch-china-blog-articles/settings/secrets/actions → 新建 `NOTION_TOKEN`

---

## 备选：内部连接（团队机器人）

仅当 PAT 不可用、且你是**工作区所有者**时：

1. 开发者工具 → **连接** → **新建连接** → 验证方式选 **API 令牌**（不要 OAuth）
2. 名称 `Fetch China GitHub Sync` → 创建
3. **Configuration** 里复制 API token
4. **Content access** 或看板 ⋯ → 连接，把 **Fetch China 工程看板** 授权给该连接
5. 同样写入 GitHub Secret `NOTION_TOKEN`

---

## 验收

1. GitHub Actions → **Notion dashboard sync** → **Run workflow**
2. Notion **流水线看板** 应与 Issues 一致（含「仪表盘演示」）

---

## 已有权限（无需你再给）

- **GitHub**：本机 `gh` 已登录
- **Notion（Cursor）**：OAuth 已连
