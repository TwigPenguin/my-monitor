import requests
import time
import random # 引入随机库

print("开始模拟真实用户疯狂提问，按 Ctrl+C 停止...")

# 准备一个真实的问题库，让脚本随机抽
prompts = [
    "请写一首关于春天的五言绝句。",
    "用 Python 写一个冒泡排序的代码。",
    "解释一下什么是云计算，控制在50字以内。",
    "大模型和传统人工智能有什么区别？",
    "今天天气真好，给我讲个冷笑话吧。",
    "1加1为什么等于2？"
]

while True:
    try:
        # 从列表里随机抽一个问题
        current_prompt = random.choice(prompts)
        # 对 URL 进行安全编码（防止中文在请求时乱码）
        import urllib.parse
        encoded_prompt = urllib.parse.quote(current_prompt)
        
        url = f"http://127.0.0.1:8000/ai/chat?prompt={encoded_prompt}"
        
        # 发送请求
        res = requests.get(url)
        data = res.json()
        
        print(f"提问: {current_prompt[:10]}... | 生成Token: {data.get('tokens_generated')} 个 | 耗时: {data.get('latency_seconds')} 秒")
        
        # 随机休息 1 到 2 秒，更像真人的操作节奏
        time.sleep(random.uniform(1.0, 2.0)) 
    except Exception as e:
        print(f"请求失败: {e}")
        time.sleep(1)