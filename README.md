# AI 服务监控与可视化平台

## 📌 项目简介
这是一个基于 Python 的轻量级服务监控系统。通过 FastAPI 提供服务接口，结合 Docker 容器化部署，最终实现 Prometheus 数据采集与 Grafana 可视化大屏。

## 🛠️ 技术栈
- 开发语言：Python 3
- Web框架：FastAPI, Uvicorn
- 监控组件：Prometheus, Grafana
- 部署工具：Docker, Docker Compose

## ⚙️ 核心功能
1. **数据采集接口**：基于 `psutil` 实时获取系统 CPU 与内存指标，并通过 FastAPI 暴露 `/system_info` 接口。
2. **标准监控指标**：集成 `prometheus-fastapi-instrumentator`，自动暴露标准 `/metrics` 接口，统计 API 请求次数与响应延迟。
3. **容器编排与网络**：编写 `docker-compose.yml`，一键启动 Web 服务、Prometheus 与 Grafana，实现容器间内网互通。
4. **可视化监控**：配置 Grafana 接入 Prometheus，通过 PromQL 语句（如 `rate(http_requests_total[1m])`）绘制 QPS 曲线，实现服务状态的实时监控。

## 🚀 运行指南
1. 克隆本仓库
2. 在项目根目录运行：`docker compose up -d --build`
3. 访问 FastAPI 接口：`http://127.0.0.1:8000/docs`
4. 访问 Grafana 大屏：`http://127.0.0.1:3000` (账号/密码: admin)

![Grafana Dashboard](这里是你的截图链接)
<img width="2852" height="1652" alt="image" src="https://github.com/user-attachments/assets/04fae2a9-15ae-4bf5-a5f0-f47fcfc9fed6" />
