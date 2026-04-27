import os
import numpy as np
from openai import OpenAI

BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
EMB_MODEL = "text-embedding-v4"

api_key = os.getenv("DASHSCOPE_API_KEY")
client = OpenAI(api_key=api_key, base_url=BASE_URL)

def get_emb(text):
    resp = client.embeddings.create(input=text, model=EMB_MODEL)
    return resp.data[0].embedding

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a,b) / (np.linalg.norm(a)*np.linalg.norm(b))

texts = [
    "我喜欢自然语言处理，尤其是大语言模型。",
    "大模型可以完成文本生成、摘要和问答任务。",
    "今天学校食堂的红烧肉很好吃。",
    "语义向量可以用来计算两个句子的相似度。",
]

vecs = [get_emb(t) for t in texts]

query = "语义向量有哪些作用"
q_vec = get_emb(query)
scores = [cosine_similarity(q_vec, v) for v in vecs]
max_idx = np.argmax(scores)

print("查询句子：", query)
print("最相似句子：", texts[max_idx])
print("相似度：", round(scores[max_idx], 4))