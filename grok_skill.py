# grok_skill.py - GrokClaw Skill for OpenClaw
# Usage: openclaw skill add https://github.com/WOSHI2000/musicalcarnival

import os
import requests
import json

class GrokClawSkill:
    def __init__(self):
        self.api_key = os.getenv("XAI_API_KEY")  # 在 ~/.openclaw/.env 或 config 设置
        self.base_url = "https://api.x.ai/v1/chat/completions"  # Grok API endpoint (假设2026标准)

    def generate_post(self, topic="72小时冲GitHub Trending"):
        """生成 X/小红书推广帖文案"""
        if not self.api_key:
            return "Error: 请设置 XAI_API_KEY 环境变量！"

        prompt = f"""
        你是 Grok，现在帮我写一篇病毒式 X (Twitter) 推文，主题：用 musicalcarnival 这个 skill 把 Grok 集成到 OpenClaw，让我的 AI Agent 72小时冲上 GitHub Trending！
        钩子强：带 emoji、Star 解锁、链接仓库 https://github.com/WOSHI2000/musicalcarnival
        中文 + 英文混排，长度 < 280 字符。加 hashtag #OpenClaw #Grok #AIAgent
        """

        payload = {
            "model": "grok-beta",  # 或最新 Grok 模型
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.8,
            "max_tokens": 300
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(self.base_url, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
            return result["choices"][0]["message"]["content"].strip()
        except Exception as e:
            return f"API 调用失败: {str(e)}"

    def run(self, command):
        if "generate_post" in command:
            return self.generate_post()
        return "GrokClaw Skill 已加载！试试：generate_post"

# OpenClaw skill 入口
skill = GrokClawSkill()
