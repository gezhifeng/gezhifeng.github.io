import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from openai import OpenAI

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

api_key = os.getenv("DASHSCOPE_API_KEY")
client = OpenAI(
    api_key=api_key,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    msg = data.get("message", "")
    
    response = client.chat.completions.create(
        model="qwen-turbo",
        messages=[{"role": "user", "content": msg}]
    )
    return {"reply": response.choices[0].message.content}