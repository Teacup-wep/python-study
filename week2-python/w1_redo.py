import requests
r=requests.get("https://v1.hitokoto.cn/",timeout=5,headers={"user-agent":"Mozilla/5.0"})
print(r.status_code)
try:


    print(r.json()["hitokoto"])
except Exception as x:
    print("有错误",x)