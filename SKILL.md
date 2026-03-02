---
name: GrokClaw
description: Integrate Grok (xAI) into OpenClaw for generating viral X posts, promotion scripts, and 72h Trending strategies. Local API calls with Chinese-optimized prompts.
version: 1.0
author: Enping Waipo (@EWaipo21895) + Grok
tags: [grok, xai, trending, promotion, agent, meme]
homepage: https://github.com/WOSHI2000/musicalcarnival
requires: xai_api_key (env var)
---

# GrokClaw Skill 🦞🚀

让你的 OpenClaw Agent 用 Grok 生成病毒式推广文案、冲榜策略！Star 仓库解锁隐藏 Prompt 包。

## 快速示例
- "用 GrokClaw 生成一篇推广 musicalcarnival 的 X 推文"
- "GrokClaw: 帮我写 72 小时冲 GitHub Trending 的完整计划"
- "generate_post topic=本地AI Agent 热潮"

## 功能
- generate_post(topic: str) → str: 生成 <280 字符的 X/小红书文案（带 emoji、hashtag、链接仓库）
- 用 grok_skill.py 执行 API 调用（需设置 XAI_API_KEY 环境变量）

## 安装 & 使用
1. 设置环境：export XAI_API_KEY=sk-你的key（从 x.ai 获取）
2. 添加 skill：clone 本 repo 到 ~/.openclaw/skills/musicalcarnival/ 或在 OpenClaw chat 说 "add skill from https://github.com/WOSHI2000/musicalcarnival"
3. 测试：openclaw --prompt "用 GrokClaw 生成推广帖"

Star 后在 Issues 留言 "starred"，我发你专属 Grok 冲榜 Prompt！

Made with ❤️ by Enping Waipo + Grok
