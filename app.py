from openai import OpenAI
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# 直接写死密钥，绕过环境变量
client = OpenAI(
    api_key="sk-6937850a78b34ac5acb8bd6920bfd2d1",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 关键修复：加上 static/ 路径
@app.get("/", response_class=HTMLResponse)
def root():
    return open("static/index.html", encoding="utf-8").read()

@app.get("/chat")
def chat(msg: str):
    completion = client.chat.completions.create(
        model="qwen-turbo",
        messages=[{"role": "user", "content": msg}]
    )
    return {"reply": completion.choices[0].message.content}