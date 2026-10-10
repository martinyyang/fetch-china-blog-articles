# Fetch China 仪表盘（GitHub 为准）

## 你要用的界面

- **GitHub Issues**：https://github.com/martinyyang/fetch-china-blog-articles/issues
- **（可选）GitHub Project**：把本仓库 Issues 加成 Project 看板
- **Notion 工程看板**：只读镜像，**不要拖列** — 由 [notion-dashboard-sync.yml](../.github/workflows/notion-dashboard-sync.yml) 每 15 分钟 + Issue 事件同步

## 开一个任务

1. **New Issue** → 选模板 **Fetch China 任务**
2. 填 Handoff / Acceptance，默认会带 `ai:composer` 标签
3. 准备好派 AI 时，加上标签 **`ai:ready`**

## 标签 → 状态（自动进 Notion Stage）

| GitHub | Notion Stage（展示） |
|--------|----------------------|
| （无 ai:ready） | 📥 新 Issue |
| `ai:ready` | ▶️ 拖到这里→AI开工 |
| `status:in-progress` | 🔨 AI 实现中 |
| `status:blocked` | ⛔ 阻塞 |
| Issue closed | ✅ 完成 |

## AI 路由标签

- `ai:composer` → Composer (Cursor)
- `ai:glm` → GLM-5.3
- `ai:general` → General agent

## 一次性 Secrets（Repository settings → Secrets）

| Secret | 值 |
|--------|-----|
| `NOTION_TOKEN` | Notion Internal Integration secret |
| `NOTION_DATABASE_ID` | `62d957d4-c80e-4876-ac98-ce829461ef0b` |

Integration 需连接 **Fetch China 工程看板** 数据库。

## 下一步（AI 真正在云端跑）

在 `ai:ready` 上再加 workflow：触发 Cursor Cloud / 自建 Agent — 不依赖你的电脑开机。
