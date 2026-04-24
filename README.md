# Fetch China Blog Articles

AI-generated blog articles for [fetchchina.com/blog](https://fetchchina.com/blog)

## 目录结构

```
articles/
├── published/          # 已发布的文章
├── drafts/            # 草稿
└── ideas/             # 文章选题和大纲
```

## 文章主题

- 国际物流（中国向外运费）
- 海运/空运/快递对比
- 清关指南
- 成本优化技巧
- 行业趋势分析

## 质量标准

- ✅ 英文内容
- ✅ 1000+ 字
- ✅ SEO 优化（标题、描述、关键词）
- ✅ 内部链接指向主站
- ✅ 实用性强，有行动号召（CTA）

## 发布流程

1. AI 在 `drafts/` 创建文章
2. 审核通过后移到 `published/`
3. 复制到 `~/fetch-china/blog/content/posts/`
4. 运行 `deploy.bat` 发布到网站

## 仓库地址

https://github.com/martinyyang/fetch-china-blog-articles
