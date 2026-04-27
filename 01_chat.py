import os
from openai import OpenAI

BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
MODEL_NAME = "qwen-turbo"

api_key = os.getenv("DASHSCOPE_API_KEY")
if not api_key:
    raise RuntimeError("没有读取到 DASHSCOPE_API_KEY")

client = OpenAI(api_key=api_key, base_url=BASE_URL)

res = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[
        {"role":"system","content":"回答简洁准确"},
        {"role":"user","content":"三句话解释什么是自然语言处理"}
    ],
    temperature=0.3
)

print(res.choices[0].message.content)