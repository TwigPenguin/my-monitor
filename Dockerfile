FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 8000

CMD ["python3","main.py"]