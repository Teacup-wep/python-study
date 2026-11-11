import requests
import json 
from datetime import date
url="https://api.bilibili.com/x/web-interface/popular"
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ""(KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0"}
simple = []


for i in range(1,4):
    params={"pn":i,"ps":5}
    r=requests.get(url,headers=headers,params=params,timeout=5)
    if r.status_code!=200:
        print("出错了",r.status_code)
        continue
    data=r.json()
    if data["code"]!=0:
        print("出错了",data["code"])
        continue
    videos=data["data"]["list"]
    for v in videos:
            simple.append({
        "title": v["title"],
        "up": v["owner"]["name"],
        "view": v["stat"]["view"],
        "bvid": v["bvid"],          # 唯一 ID，留着有用
    })


filename=f"data{date.today()}.json"
def save_json(data,path):
      with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"已保存 {len(data)} 条到 {path}")
def load_json(path):
    """从 JSON 文件读出数据"""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
save_json(simple, filename)

videos = load_json(filename)
print(len(videos))  
    




    