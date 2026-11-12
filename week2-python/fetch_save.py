import requests
import time
import json 
from datetime import date
url="https://api.bilibili.com/x/web-interface/popular"
#url="https://api.bilibili.com/x/web-interface/nonexist"
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ""(KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0"}
simple = []





filename=f"data{date.today()}.json"
def save_json(data,path):
      with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"已保存 {len(data)} 条到 {path}")
def load_json(path):
    """从 JSON 文件读出数据"""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
def fetch_json(url,params,res=3):
     for attempt in range(1,res+1):
          try :
               r=requests.get(url,params=params,timeout=5,headers=headers)
               r.raise_for_status()
               return r.json()
          except requests.exceptions.RequestException as e:
               print(f"第{attempt}次出现错误，{e}")
               if attempt<res:
                    time.sleep(2)
     return None
for i in range(1,4):
    params={"pn":i,"ps":5}
    r = fetch_json(url,params)
    if r is None:
        print(f"第{i}页出错了")
        continue
    if r["code"]!=0:
        print("出错了",r["code"])
        continue
    videos=r["data"]["list"]
    for v in videos:
            simple.append({
        "title": v["title"],
        "up": v["owner"]["name"],
        "view": v["stat"]["view"],
        "bvid": v["bvid"],          # 唯一 ID，留着有用
    })





    
save_json(simple, filename)

videos = load_json(filename)
print(len(videos))  
    




    