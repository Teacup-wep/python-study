import requests

r = requests.get("https://v1.hitokoto.cn/", timeout=5,
                 headers={"User-Agent": "Mozilla/5.0"})

print(f"1. 状态码：{r.status_code}")
print(f"2. 原始文本前50字：{r.text[:50]}")
print(f"3. 解析后的类型：{type(r.json())}")
print("4. 解析后的内容：", r.json())