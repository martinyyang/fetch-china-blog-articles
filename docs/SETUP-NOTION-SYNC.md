# 一次性配置（给「我不会弄」版）

云端同步 **GitHub → Notion** 只差一个 Secret：`NOTION_TOKEN`。

`NOTION_DATABASE_ID` 已由助手写入仓库 Secrets，你**不用管**。

---

## 链接都会进「开发者工具」——这是对的

Notion 已把旧地址（如 `notion.so/my-integrations`）**统一跳转**到：

**https://app.notion.com/developers/connections**

你不需要再找别的网站，就在这一组页面里操作即可。

顶栏标签（同一套 UI）：

| 标签 | 用途 |
|------|------|
| Workers | ❌ 本任务不用（常要升级） |
| **连接** | 备选：内部连接 + API 令牌 |
| **个人访问令牌** | ✅ **推荐** |
| MCP 令牌 | ❌ 给 Cursor MCP 用，不是 GitHub Actions |

个人访问令牌直达（若顶栏不好点）：  
**https://app.notion.com/developers/personal-access-tokens**

---

## 推荐：个人访问令牌（2 步）

1. 打开 https://app.notion.com/developers/personal-access-tokens  
   （或从 **连接** 页顶栏点 **个人访问令牌**）
2. **新建令牌** → 名称 `Fetch China GitHub Sync` → 能力 **Notion API** → 创建 → **复制**

PAT 代表**你自己**，能打开的 **Fetch China 工程看板** API 就能写，**不必**再去工程看板 ⋯ 里「连接集成」。

若 **没有「新建令牌」**：工作区可能禁止成员建 PAT → 所有者到 **设置 → 连接** 放开，或改用下面「内部连接」。

---

## 备选：内部连接（在「连接」页）

1. https://app.notion.com/developers/connections → **新建连接**
2. 验证方式选 **API 令牌**（不要 OAuth）
3. 名称 `Fetch China GitHub Sync` → 创建
4. **Configuration** 复制 API token
5. **Content access** 添加 **Fetch China 工程看板**（或看板 ⋯ → 连接该连接）

---

## 把令牌交给 GitHub

**A. 助手代填（推荐）** — 不要粘到聊天

`C:\Users\Administrator\.cursor\secrets\notion-github-sync.env`：

```
NOTION_TOKEN=粘贴令牌
```

保存后回复：**「notion token 已放好」**

**B. 网页**  
https://github.com/martinyyang/fetch-china-blog-articles/settings/secrets/actions → `NOTION_TOKEN`

---

## 验收

Actions → **Notion dashboard sync** → Run workflow → Notion **流水线看板** 与 GitHub Issues 一致。

---

## 侧边栏入口（可选）

Notion **设置** 里打开 **Developer Mode（开发者模式）** 后，左侧会出现开发者区，可点 **Personal access tokens**，与上面同一页面。
