from openai import OpenAI
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 🔥 跨域解决（必须加）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# AI 密钥（直接写死，稳定）
client = OpenAI(
    api_key="sk-6937850a78b34ac5acb8bd6920bfd2d1",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 首页
@app.get("/", response_class=HTMLResponse)
def root():
    return open("static/index.html", encoding="utf-8").read()

# 聊天接口（GET 方式）
@app.get("/chat")
def chat(msg: str):
    completion = client.chat.completions.create(
        model="qwen-turbo",
        messages=[{"role": "user", "content": msg}]
    )
    return {"reply": completion.choices[0].message.content}