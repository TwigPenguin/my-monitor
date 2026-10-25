import psutil
from fastapi import FastAPI
import uvicorn

app=FastAPI()

@app.get("/metrics")
def get_system_metrics():
    cpu=psutil.cpu_percent(interval=0.5)
    mem=psutil.virtual_memory().percent

    if cpu > 80 or mem > 80:
        current_status = "danger"  # 危险状态
    elif cpu > 50 or mem > 50:
        current_status = "warning" # 警告状态
    else:
        current_status = "healthy" # 健康状态

    return{
        "cpu_percent":cpu,
        "memory_percent":mem,
        "status":current_status
    }

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000) 
