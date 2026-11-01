from fastapi import FastAPI
import requests
import time
import psutil
import uvicorn
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter, Histogram

app = FastAPI()

# 自动监控 HTTP 接口
Instrumentator().instrument(app).expose(app)

# 自定义 AI 业务指标
AI_TOKEN_COUNTER = Counter('ai_generated_tokens_total', 'Total generated tokens')
AI_LATENCY_HISTOGRAM = Histogram('ai_inference_latency_seconds', 'AI inference latency')

@app.get("/system_info")
def get_system_metrics():
    return {"cpu": psutil.cpu_percent(), "mem": psutil.virtual_memory().percent}

# ================= 真实 AI 接口 =================
@app.get("/ai/chat")
def chat_with_ai(prompt: str = "请用一句话介绍一下你自己"):
    start_time = time.time()
    
    try:
        # ⚠️ 核心关键：在 Docker 容器里，必须用 host.docker.internal 才能访问你 Windows 上的 Ollama
        ollama_url = "http://host.docker.internal:11434/api/generate"
        
        payload = {
            "model": "qwen2:0.5b", 
            "prompt": prompt,
            "stream": False # 我们需要完整的返回结果来统计 Token
        }
        
        # 发送请求给本地真实的大模型
        response = requests.post(ollama_url, json=payload, timeout=30)
        response.raise_for_status() 
        
        data = response.json()
        text = data.get("response", "")
        
        # Ollama 返回的 eval_count 就是真实的 Token 数量
        token_count = data.get("eval_count", len(text)) 
        
        # 记录指标
        AI_TOKEN_COUNTER.inc(token_count)
        latency = time.time() - start_time
        AI_LATENCY_HISTOGRAM.observe(latency)
        
        return {
            "answer": text,
            "tokens_generated": token_count,
            "latency_seconds": round(latency, 2)
        }
        
    except Exception as e:
        return {"error": str(e), "message": "请检查 Ollama 是否在运行"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)